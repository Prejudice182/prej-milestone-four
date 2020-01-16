from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product

# Create your views here.


def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(
        customer=request.user, ordered=False)

    cart_item_qs = CartItem.objects.filter(cart=cart, product=product)
    if cart_item_qs.exists():
        cart_item = cart_item_qs.first()
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, 'This item quantity was updated.')
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)
        cart_item.save()
        messages.info(request, 'This item was added to your cart.')
    return redirect('cart:home')


def decrease_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs.first()
        cart_item_qs = CartItem.objects.filter(cart=cart, product=product)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                messages.info(request, f'{product.name} quantity was updated.')
            elif cart_item_qs.count() == 1:
                cart_item.delete()
                cart.delete()
                messages.info(request, 'Your cart is now empty.')
                return redirect('products:home')
        else:
            messages.info(
                request, f'{product.name} was not found in your cart.')
    else:
        messages.info(request, 'You do not have anything in your cart.')

    return redirect('cart:home')


def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs.first()
        cart_item_qs = CartItem.objects.filter(cart=cart, product=product)
        if cart_item_qs.exists():
            cart_item = cart_item_qs.first()
            cart_item.delete()
            messages.info(
                request, f'{product.name} was removed from your cart.')
            if cart_item_qs.count() == 1:
                cart.delete()
                messages.info(request, 'Your cart is now empty.')
                return redirect('products:home')
        else:
            messages.info(
                request, f'{product.name} was not found in your cart.')
    else:
        messages.info(request, 'You do not have anything in your cart.')

    return redirect('products:home')


def cart_view(request):
    user = request.user

    carts = Cart.objects.filter(customer=user, ordered=False)

    if carts.exists():
        cart_items = CartItem.objects.filter(cart=carts.first())
        context = {
            'cart': carts.first(),
            'cart_items': cart_items,
        }
        return render(request, 'cart/home.html', context)
    else:
        messages.warning(request, 'You do not have an active order')
        return redirect('products:home')
