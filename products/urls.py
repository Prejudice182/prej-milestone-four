from django.urls import path
from .views import Home, CategoryView, ProductDetailView
app_name = 'products'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('listing/<slug>', ProductDetailView.as_view(), name='detail'),
]