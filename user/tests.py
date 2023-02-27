from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import date, timedelta
from collections import OrderedDict
from django.shortcuts import reverse
from django.contrib.auth.models import User 
# Create your tests here.


class SigninTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test3',
                                                         password='12test12',
                                                         email='test3@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test3', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test3', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)



class SignInViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test3',
                                                         password='12test12',
                                                         email='test3@example.com')

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        response = self.client.post('/user/login/', {'username': 'test3', 'password': '12test12'})
        self.assertEqual(response.status_code, 302)

    def test_wrong_username(self):
        response = self.client.post('/user/login/', {'username': 'wrong', 'password': '12test12'})
        self.assertEqual(response.status_code, 200)

    def test_wrong_pssword(self):
        response = self.client.post('/user/login/', {'username': 'test3', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)        


class SignUpPageTests(TestCase):
    
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'senha8dg'
        self.first_name = "testuser"
        self.last_name = "testuser"

    def test_signup_page_url(self):
        response = self.client.get("/user/register/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    def test_signup_page_view_name(self):
        response = self.client.get(reverse('user:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='register.html')

    
