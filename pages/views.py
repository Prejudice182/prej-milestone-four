from django.views.generic import ListView
from products.models import Category

# Create your views here.


class HomeView(ListView):
    '''
    Home Page view, using a list view to display the featured categories
    '''
    template_name = 'pages/home.html'
    queryset = Category.objects.filter(featured=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get 3 featured categories
        categories = Category.objects.filter(featured=True).order_by('?').prefetch_related('product_set')[:3]
        context['featured'] = []
        for category in categories:
            context['featured'] += category.product_set.all().order_by('?')[:1]
        return context
