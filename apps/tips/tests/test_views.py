from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse, resolve


class TestTipsView(TestCase):

    def setUp(self):
        self.tips_url = reverse('views_employees')
        self.user = User.objects.create(username='TestUser', password='Testing123', is_staff=True)
        self.client = Client()

    def test_tips_view(self):
        response = self.client.get(self.tips_url, follow=True)
        self.client.login(username='TestUser', password='Testing123')
        self.assertEqual(response.status_code, 200)
