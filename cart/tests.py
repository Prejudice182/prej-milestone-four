from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from .views import add_to_cart, decrease_cart, remove_from_cart, cart_view
from .models import Cart, CartItem
from products.models import Category, Product
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

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_response_logged_out_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/users/login/?next=/cart/')

    def test_response_logged_in_cart(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='TestUser', email='test@mail.com', password='testing1234')

        self.client.login(username='TestUser', password='testing1234')
        
        category = Category(slug='medical', title='Medical')
        category.save()
        product = Product(slug='bandage', name='Bandage', category=category, preview_text='test', detail_text='test', mainimage='blank.jpg')
        product.save()

        response = self.client.get(reverse('cart:add', args=['bandage']))
        self.assertEqual(response.url, '/cart/')