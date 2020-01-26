from django import template
from cart.models import Cart, CartItem

register = template.Library()


@register.filter
def cart_total(user):
    cart = Cart.objects.filter(customer=user, ordered=False)
    
    if cart.exists():
        cart_items = CartItem.objects.filter(cart=cart.first())
        if cart_items.exists():
            return cart_items.count()
    return 0
