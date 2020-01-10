from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, decrease_cart
app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='home'),
    path('add/<slug>', add_to_cart, name='add'),
    path('remove/<slug>', remove_from_cart, name='remove'),
    path('decrease/<slug>', decrease_cart, name='decrease'),
]
