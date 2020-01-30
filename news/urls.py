from django.urls import path
from .views import NewsHomeView
app_name = 'news'

urlpatterns = [
    path('', NewsHomeView.as_view(), name='home'),
]