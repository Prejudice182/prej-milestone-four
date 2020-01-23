from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import QuantitySelectForm, OrderByForm
from .models import Product, Category

# Create your views here.


class Home(ListView):
    model = Product
    paginate_by = 6
    template_name = 'products/home.html'


class CategoryView(SingleObjectMixin, ListView):
    template_name = 'products/category.html'
    paginate_by = 6
    VALID_ORDERS = {
        'price': 'price',
        'priced': '-price',
        'name': 'name',
        'named': '-name',
        'pk': 'pk',
        'pkd': '-pk', 
    }
    DEFAULT_ORDER = 'pk'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        order_key = self.request.GET.get('order', self.DEFAULT_ORDER)
        self.order = self.VALID_ORDERS.get(order_key, self.DEFAULT_ORDER)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderByForm()
        context['category'] = self.object
        context['order'] = self.request.GET.get('order', self.DEFAULT_ORDER)
        print(context)
        return context

    def get_queryset(self):
        return self.object.product_set.order_by(self.order)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuantitySelectForm()
        return context
