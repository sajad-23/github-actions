from django.test import TestCase
from django.contrib.auth.models import User



class UserTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='username', password='password')
    
    def test_user(self):
        user:User = User.objects.get(username='username')
        self.assertEqual(user.username, self.user.username)

