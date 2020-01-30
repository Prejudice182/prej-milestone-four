from django.contrib.auth import get_user_model
from django.db import models
from products.models import Product

User = get_user_model()

# Create your models here.


class CartItem(models.Model):
    '''
    Cart item model, with a foreign key to the Cart model
    '''
    cart = models.ForeignKey(
        'Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'

    def get_total(self):
        return self.product.price * self.quantity


class Cart(models.Model):
    '''
    Cart model, with a foreign key to the User model
    '''
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='customer')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer.username} - {self.ordered}'

    def get_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_total()
        return total
