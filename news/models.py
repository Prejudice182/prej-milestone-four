from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    tag_line = models.CharField(max_length=100)
    content = models.TextField()
    banner_image = models.ImageField(upload_to='media/news/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('news:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.headline