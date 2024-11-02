from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from products.models import Product


def add_func(request, cart_item, exists=False):
    '''
    Function for adding an item to cart, due to repetitive code in each view
    '''
    if exists:
        if request.method == 'POST':
            cart_item.quantity += int(request.POST['quantity'])
        else:
            cart_item.quantity += 1
    else:
        if request.method == 'POST':
            cart_item.quantity = int(request.POST['quantity'])
        else:
            cart_item.quantity = 1
    cart_item.save()


def dec_or_remove(cart, product, remove=False):
    '''
    Function for decreasing or removing an item in cart, due to repetitive code in each view
    '''
    contents = cart.items.all()
    if contents.exists():
        item_in_cart = contents.filter(product=product)
        if item_in_cart.exists():
            item = item_in_cart.first()
            if remove or item.quantity == 1:
                item.delete()
            else:
                item.quantity -= 1
                item.save()


@login_required
def add_to_cart(request, slug):
    '''
    Add to cart view, checking if item exists to update current quantity
    '''
    product = get_object_or_404(Product, slug=slug)
    cart, created = Cart.objects.get_or_create(
        customer=request.user, ordered=False)
    item_in_cart = cart.items.filter(product=product)

    if created or not item_in_cart.exists():
        cart_item = CartItem.objects.create(cart=cart, product=product)
        add_func(request, cart_item)
    else:
        cart_item = item_in_cart.first()
        add_func(request, cart_item, exists=True)

    return redirect('cart:home')


@login_required
def decrease_cart(request, slug):
    '''
    Decrease cart view, using slug to look product up in DB, and lowering its quantity
    '''
    product = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs.first()
        dec_or_remove(cart, product, remove=False)
        messages.info(request, f'{product.name} quantity updated!')

    return redirect('cart:home')


@login_required
def remove_from_cart(request, slug):
    '''
    Remove from cart view, to remove an item from cart completely
    '''
    product = get_object_or_404(Product, slug=slug)
    cart_qs = Cart.objects.filter(customer=request.user, ordered=False)

    if cart_qs.exists():
        cart = cart_qs.first()
        dec_or_remove(cart, product, remove=True)
        messages.info(request, f'{product.name} removed!')

    return redirect('cart:home')


@login_required
def cart_view(request):
    '''
    Cart Home View, used to display the contents of a users cart
    '''
    user = request.user

    carts = Cart.objects.filter(customer=user, ordered=False)

    if carts.exists():
        cart = carts.first()
        cart_items = CartItem.objects.filter(cart=cart)
        if cart_items.exists():
            context = {
                'cart': carts.first(),
                'cart_items': cart_items,
            }
            return render(request, 'cart/home.html', context)

    messages.warning(request, 'You do not have an active order')
    return redirect('products:home')
