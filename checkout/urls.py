from django.urls import path
from .views import checkout, payment, confirm, all_orders
app_name = 'checkout'

urlpatterns = [
    path('', checkout, name='home'),
    path('payment/', payment, name='payment'),
    path('confirm/<session_id>', confirm, name='confirm'),
    path('all-orders/', all_orders, name='all_orders'),
]