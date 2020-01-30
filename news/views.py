from django.shortcuts import render
from django.views.generic import ListView
from .models import Article

# Create your views here.


class NewsHomeView(ListView):
    paginate_by = 10
    template_name = 'news/index.html'
    queryset = Article.objects.all().order_by('-updated')
    context_object_name = 'articles'
