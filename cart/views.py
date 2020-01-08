from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, Order
from products.models import Product

# Create your views here.


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = Cart.objects.get_or_create(
        item=item, user=request.user)

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()

        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, 'This item quantity was updated.')
        else:
            order.orderitems.add(order_item)
            messages.info(request, 'This item was added to your cart.')
    else:
        order = Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, 'This item was added to your cart.')

    return redirect('cart:home')

def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)

    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs.first()

        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs.first()

        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = Cart.objects.filter(item=item, user=request.user).first()
            order.orderitems.remove(order_item)
            messages.info(request, 'This item was removed from your cart.')
        else:
            messages.info(request, 'This item was not in your cart.')
    else:
        messages.info(request, 'You do not have an active order.')
    return redirect('products:home')

def cart_view(request):
    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        order = orders.first()
        context = {
            'carts': carts,
            'order': order
        }
        return render(request, 'cart/home.html', context)
    else:
        messages.warning(request, 'You do not have an active order')
        return redirect('products:home')