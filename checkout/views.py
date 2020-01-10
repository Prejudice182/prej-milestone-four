from django.conf import settings
from django.shortcuts import render
from .forms import BillingForm
from .models import BillingAddress
from cart.models import Order
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.


def checkout(request):
    form = BillingForm

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order = order_qs.first()

    order_items = order.orderitems.all()
    order_total = order.get_totals()

    context = {
        'form': form,
        'order_items': order_items,
        'order_total': order_total
    }

    saved_address_qs = BillingAddress.objects.filter(user=request.user)
    if saved_address_qs.exists():
        saved_address = saved_address_qs.first()
        context['saved_address'] = saved_address
    if request.method == 'POST':
        saved_address_qs = BillingAddress.objects.filter(user=request.user)
        if saved_address_qs.exists():
            saved_address = saved_address_qs.first()
            form = BillingForm(request.POST, instance=saved_address)
        else:
            form = BillingForm(request.POST)

        if form.is_valid():
            billing_address = form.save(commit=False)
            billing_address.user = request.user
            billing_address.save()

    return render(request, 'checkout/index.html', context)


def payment(request):
    key = settings.STRIPE_PUBLISHABLE
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_total = order_qs.first().get_totals()
    total = order_total * 100

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=order_total, currency='eur', description=order_qs, source=request.POST['stripeToken'])

    context = {
        'key': key,
        'total': total
    }

    return render(request, 'checkout/payment.html', context)