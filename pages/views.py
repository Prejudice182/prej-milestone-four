from django.views.generic import ListView
from products.models import Category

# Create your views here.


class HomeView(ListView):
    template_name = 'pages/home.html'
    queryset = Category.objects.filter(featured=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.filter(featured=True)
        context['featured'] = []
        for category in categories:
            context['featured'] += category.product_set.all().order_by('?')[:1]
        return context
