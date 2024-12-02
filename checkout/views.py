from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.utils.crypto import get_random_string
from .forms import BillingForm
from .models import BillingAddress, Order, OrderItem
from cart.models import Cart, CartItem
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.


def checkout(request):
    '''
    View to display the initial checkout page, asking user for billing address
    or using a saved one if available
    '''
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
    '''
    View called on validation of address, used to verify details are correct,
    before continuing to Stripe for payment
    '''
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)
    cart = cart_qs.first()
    cart_items = cart.items.all()
    cart_total = cart.get_total()

    line_items = []
    for item in cart_items:
        item_dict = {
            'price_data': {
                'product_data': {
                    'name': item.product.name,
                },
                'unit_amount': int(item.product.price * 100),
                'currency': 'eur',
            },
            'quantity': item.quantity,
        }
        line_items.append(item_dict)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=settings.STRIPE_SUCCESS_URL,
        cancel_url=settings.STRIPE_CANCEL_URL
    )

    saved_address = BillingAddress.objects.filter(user=request.user).first()

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'saved_address': saved_address,
        'session_id': session.id
    }

    return render(request, 'checkout/payment.html', context)


def confirm(request, session_id):
    '''
    View called after Stripe returns to site, making sure a valid
    session is provided, if not, redirect to home
    '''
    try:
        session = stripe.checkout.Session.retrieve(session_id)
    except:
        return redirect('home')
    else:
        cart = Cart.objects.filter(
            customer=request.user, ordered=False).first()
        cart_items = cart.items.all()
        total = int(cart.get_total() * 100)

        order_id = get_random_string(length=16)
        order = Order.objects.create(
            user=request.user, total=total, payment_id=session.payment_intent, order_id=f'#{request.user}{order_id}')
        saved_address = BillingAddress.objects.filter(
            user=request.user).first()
        for item in cart_items:
            OrderItem.objects.create(
                order=order, product=item.product, quantity=item.quantity)
        order.save()
        cart.ordered = True
        cart.save()
        context = {
            'saved_address': saved_address,
            'items': order.items,
            'order': order
        }
        return render(request, 'checkout/confirm.html', context)


def all_orders(request):
    '''
    View to display all of a users successful orders
    '''
    try:
        orders = Order.objects.filter(user=request.user)
        context = {
            'orders': orders
        }
    except:
        messages.warning(request, 'You do not have any completed orders')
        return redirect('checkout:home')

    return render(request, 'checkout/orders.html', context)
