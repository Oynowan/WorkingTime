from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.credentials = {
            'username': 'testuser',
            'password': 'Testing123'
        }

        User.objects.create(**self.credentials)

    def test_login(self):

        response = self.client.post(self.login_url, self.credentials)
        self.assertEqual(response.status_code, 200)

