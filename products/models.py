from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    slug = models.SlugField(editable=False)
    name = models.CharField(max_length=300)
    mainimage = models.ImageField(upload_to='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Product, self).save(*args, **kwargs)