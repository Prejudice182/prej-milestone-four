from django.test import TestCase
from django.urls import reverse, resolve
from .models import BillingAddress, Order
from .views import checkout, payment, all_orders
# Create your tests here.

class TestUrls(TestCase):
    def test_checkout_url(self):
        url = reverse('checkout:home')
        self.assertEqual(resolve(url).func, checkout)

    def test_payment_url(self):
        url = reverse('checkout:payment')
        self.assertEqual(resolve(url).func, payment)

    def test_orders_url(self):
        url = reverse('checkout:all_orders')
        self.assertEqual(resolve(url).func, all_orders)