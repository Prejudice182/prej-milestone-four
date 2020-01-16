from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Product, Category

# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'products/home.html'


class CategoryView(SingleObjectMixin, ListView):
    template_name = 'products/category.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return self.object.product_set.all()