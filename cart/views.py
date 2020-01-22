from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import SingleObjectMixin
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
        if request.method == 'POST':
            cart_item.quantity += int(request.POST['quantity'])
        else:
            cart_item.quantity += 1
        cart_item.save()
        messages.info(request, 'This item quantity was updated.')
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product)
        if request.method == 'POST':
            cart_item.quantity = int(request.POST['quantity'])
        else:
            cart_item.quantity = 1
        cart_item.save()
        messages.info(request, 'This item was added to your cart.')
    return redirect('cart:home')


def decrease_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs.first()
        cart_contents_qs = CartItem.objects.filter(cart=cart)
        if cart_contents_qs.exists():
            line_count = cart_contents_qs.count()
            item_qs = cart_contents_qs.filter(product=product)
            if item_qs.exists():
                item = item_qs.first()
                if item.quantity > 1:
                    item.quantity -= 1
                    item.save()
                    messages.info(request, f'{product.name} quantity was decreased by 1.')
                else:
                    item.delete()
                    messages.info(request, f'{product.name} was removed from your cart.')
                if line_count == 1:
                    cart.delete()
                    messages.info(request, 'Your cart is now empty.')
                    return redirect('products:home')
            else:
                messages.warning(request, f'{product.name} was not found in your cart.')
                return redirect('products:home')
    else:
        messages.warning(request, 'You do not have an active cart.')
        return redirect('products:home')

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
            messages.warning(
                request, f'{product.name} was not found in your cart.')
    else:
        messages.warning(request, 'You do not have anything in your cart.')

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
