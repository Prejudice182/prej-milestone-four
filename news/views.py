from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Article

# Create your views here.


class NewsHomeView(ListView):
    '''
    Get all articles, order by last updated descending, paginate 10 per page
    '''
    paginate_by = 10
    template_name = 'news/index.html'
    queryset = Article.objects.all().order_by('-updated')
    context_object_name = 'articles'


class NewsCreateView(LoginRequiredMixin, CreateView):
    '''
    Create an article, user must be logged in to do so
    '''
    model = Article
    fields = ['headline', 'tag_line', 'banner_image', 'content']
    template_name = 'news/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsDetailView(DetailView):
    '''
    View more details about an article
    '''
    model = Article
    template_name = 'news/details.html'
    context_object_name = 'article'