from django.db import models

# Create your models here.
class VIPSlot(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    for_server = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False, default=5)

    def __str__(self):
        return self.title


class Kit(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    for_server = models.CharField(max_length=300)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False, default=5)
    allowed_vips = models.ManyToManyField(VIPSlot)
    image = models.ImageField(upload_to='images', default='', blank=True)

    def __str__(self):
        return self.title