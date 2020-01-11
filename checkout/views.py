from django.conf import settings
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .forms import BillingForm
from .models import BillingAddress, Order
from cart.models import Cart, CartItem
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.


def checkout(request):
    form = BillingForm

    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)
    cart = cart_qs.first()

    cart_items = cart.items.all()
    cart_total = cart.get_total()

    context = {
        'form': form,
        'cart_items': cart_items,
        'cart_total': cart_total
    }

    saved_address_qs = BillingAddress.objects.filter(user=request.user)
    if saved_address_qs.exists():
        saved_address = saved_address_qs.first()
        context['saved_address'] = saved_address
    if request.method == 'POST':
        if saved_address_qs.exists():
            form = BillingForm(request.POST, instance=saved_address)
        else:
            form = BillingForm(request.POST)

        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.user = request.user
            billing_address.save()
            return redirect('checkout:payment')

    return render(request, 'checkout/index.html', context)


def payment(request):
    key = settings.STRIPE_PUBLISHABLE

    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)
    cart = cart_qs.first()

    cart_total = cart.get_total()
    total = cart_total * 100

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=order_total, currency='eur', description=cart, source=request.POST['stripeToken'])

    context = {
        'key': key,
        'total': total
    }

    return render(request, 'checkout/payment.html', context)

def charge(request):
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)
    cart = cart_qs.first()

    cart_items = cart.items.all()
    cart_total = cart.get_total()
    total = int(cart_total * 100)

    if request.method == 'POST':
        charge = stripe.Charge.create(amount=total, currency='eur', description=cart, source=request.POST['stripeToken'])
        
        if charge.status == 'succeeded':
            order_id = get_random_string(length=16)
            order = Order.objects.create(user=request.user, total=cart_total, payment_id=charge.id, order_id=f'#{request.user}{order_id}')
            print(order)
            for item in cart_items:
                order.order_items.add(item)
                print(item)
            order.save()
            cart.ordered = True
            cart.save()

        context = {
            'items': order.order_items,
            'order': order
        }

        return render(request, 'checkout/charge.html', context)

def all_orders(request):
    try:
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders
        }
    except:
        messages.warning(request, 'You do not have any completed orders')
        return redirect('checkout:home')

    return render(request, 'checkout/orders.html', context)
