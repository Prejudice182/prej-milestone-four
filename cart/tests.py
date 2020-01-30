from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from .views import add_to_cart, decrease_cart, remove_from_cart, cart_view
from .models import Cart, CartItem
import datetime

User = get_user_model()
# Create your tests here.

class TestUrls(TestCase):
    '''
    Test that all URLs resolve correctly
    '''
    def test_cart_url_correct(self):
        url = reverse('cart:home')
        self.assertEqual(resolve(url).func, cart_view)

    def test_add_url_correct(self):
        url = reverse('cart:add', args=['bandage'])
        self.assertEqual(resolve(url).func, add_to_cart)

    def test_decrease_url_correct(self):
        url = reverse('cart:decrease', args=['bandage'])
        self.assertEqual(resolve(url).func, decrease_cart)

    def test_remove_url_correct(self):
        url = reverse('cart:remove', args=['bandage'])
        self.assertEqual(resolve(url).func, remove_from_cart)

class TestModels(TestCase):
    def test_create_cart(self):
        user = User(username='TestUser')
        cart = Cart(customer=user)

        expected_result = 'TestUser - False'

        self.assertEqual(str(cart), expected_result)

    def test_default_values(self):
        user = User(username='TestUser')
        cart = Cart(customer=user)

        self.assertEqual(cart.ordered, False)