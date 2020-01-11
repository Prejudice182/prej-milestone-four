from django.urls import path
from .views import checkout, payment, charge, all_orders
app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='home'),
    path('payment/', payment, name='payment'),
    path('charge/', charge, name='charge'),
    path('all-orders/', all_orders, name='all_orders'),
]