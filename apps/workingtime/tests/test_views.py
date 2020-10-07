from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.userprofile.models import UserProfile


class TestViewsWorkingTime(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.working_url = reverse('working')
        self.credentials = {
            'username': 'Testuser',
            'password': 'Testing123'
        }

        self.user = User.objects.create(**self.credentials)
        self.user_profile = UserProfile.objects.create(user=self.user)

    def test_view_working(self):
        self.client.login(username=self.credentials['username'], password=self.credentials['password'])
        response = self.client.head(self.working_url, follow=True)
        print(self.user_profile.user)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workingtime/working.html')
