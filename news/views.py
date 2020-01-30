from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Article

# Create your views here.


class NewsHomeView(ListView):
    paginate_by = 10
    template_name = 'news/index.html'
    queryset = Article.objects.all().order_by('-updated')
    context_object_name = 'articles'


class NewsCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['headline', 'tag_line', 'banner_image', 'content']
    template_name = 'news/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/details.html'
    context_object_name = 'article'