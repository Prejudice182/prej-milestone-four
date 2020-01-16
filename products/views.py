from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Product, Category

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'products/home.html'


class CategoryView(ListView):
    template_name = 'products/home.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)