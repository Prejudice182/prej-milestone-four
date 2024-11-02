from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

# Create your models here.


class BillingAddress(models.Model):
    '''
    Billing Address model, with foreign key to User
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address1 = models.CharField(
        max_length=200, verbose_name='Address Line 1')
    street_address2 = models.CharField(
        max_length=200, blank=True, verbose_name='Address Line 2')
    town_or_city = models.CharField(max_length=50, verbose_name='Town / City')
    county_or_state = models.CharField(
        max_length=50, blank=True, verbose_name='County / State')
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f'{self.user.username} billing address'

    class Meta:
        verbose_name_plural = 'Billing Addresses'


class OrderItem(models.Model):
    '''
    Order Item model, with foreign keys to an order, and a product
    '''
    order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class Order(models.Model):
    '''
    Order model, with a foreign key to a user
    '''
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=200, blank=True, null=True)
    order_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
