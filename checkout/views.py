from django.shortcuts import render
from .forms import BillingForm
from cart.models import Order

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

    return render(request, 'checkout/index.html', context)