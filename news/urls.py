from django.urls import path
from .views import NewsHomeView, NewsCreateView, NewsDetailView
app_name = 'news'

urlpatterns = [
    path('', NewsHomeView.as_view(), name='home'),
    path('create/', NewsCreateView.as_view(), name='create'),
    path('details/<pk>', NewsDetailView.as_view(), name='details'),
]