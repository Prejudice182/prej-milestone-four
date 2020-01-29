from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from .forms import QuantitySelectForm, OrderByForm
from .models import Product, Category

# Create your views here.

VALID_ORDERS = {
    'pk': 'pk',
    'pkd': '-pk',
    'price': 'price',
    'priced': '-price',
    'name': 'name',
    'named': '-name',
}
DEFAULT_ORDER = 'pk'


class Home(ListView):
    '''
    Products home view, implementing a list view for all available products
    '''
    paginate_by = 6
    template_name = 'products/category.html'
    queryset = Product.objects.all()

    def get(self, request, *args, **kwargs):
        order_key = self.request.GET.get('order', DEFAULT_ORDER)
        self.order = VALID_ORDERS.get(order_key, DEFAULT_ORDER)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderByForm(self.request.GET)
        context['order'] = self.request.GET.get('order', DEFAULT_ORDER)
        context['category'] = 'All Products'
        return context

    def get_queryset(self):
        return self.queryset.order_by(self.order)


class CategoryView(SingleObjectMixin, Home):
    '''
    Individual category view, inheriting ListView from Home view, showing
    products pertaining to the selected category
    '''

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return self.object.product_set.order_by(self.order)


class ProductDetailView(DetailView):
    '''
    Product Detail View, using a detail view to display data about a particular
    product
    '''
    model = Product
    template_name = 'products/details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuantitySelectForm()
        return context
