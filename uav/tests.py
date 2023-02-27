from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from datetime import date, timedelta
from .models import Uav
from collections import OrderedDict
from django.utils import timezone
import datetime



class UavTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test3',
                                                         password='12test12',
                                                         email='test@example.com')
        self.user.save()
        self.timestamp = date.today()
        self.uav = Uav(author=self.user,
                         title='title',
                         brand='brand',
                         model='model',
                         weight=111,
                         category='category',
                         price=111,
                         content='content',
                         created_date=datetime.datetime.now(tz=timezone.utc))
        self.uav.save()

    def tearDown(self):
        self.user.delete()

    def test_read_uav(self):
        self.assertEqual(self.uav.author, self.user)
        self.assertEqual(self.uav.title, 'title')
        self.assertEqual(self.uav.brand, 'brand')
        self.assertEqual(self.uav.model, 'model')
        self.assertEqual(self.uav.weight, 111)
        self.assertEqual(self.uav.category, 'category')
        self.assertEqual(self.uav.price, 111)
        self.assertEqual(self.uav.content, 'content')

    def test_update_uav_title(self):
        self.uav.title = 'new title'
        self.uav.save()
        self.assertEqual(self.uav.title, 'new title')





