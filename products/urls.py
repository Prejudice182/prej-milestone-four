from django.urls import path
from .views import Home, CategoryView, ProductDetailView, SearchResultsView
app_name = 'products'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('listing/<slug>', ProductDetailView.as_view(), name='detail'),
    path('search/', SearchResultsView.as_view(), name='search'),
]