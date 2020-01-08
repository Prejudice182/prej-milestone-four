from django.urls import path
from .views import all_products, get_product_detail

urlpatterns = [
    path('', all_products, name='products'),
    path('<product_type>/<slug>/', get_product_detail, name='product_detail'),
]