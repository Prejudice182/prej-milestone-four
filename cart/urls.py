from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart
app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='home'),
    path('add/<slug>', add_to_cart, name='add_cart'),
    path('remove/<slug>', remove_from_cart, name='remove_cart'),
]