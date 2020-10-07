from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

from apps.core.views import frontpage
from apps.core.views import signup
from apps.core.views import delete_workingtime
from apps.workingtime.views import working
from apps.workingtime.views import start_working
from apps.workingtime.views import end_working
from apps.tips.views import views_employees
from apps.tips.views import tips_shared


class TestUrls(TestCase):

    def test_url_frontpage_is_resolved(self):
        url = reverse('frontpage')
        self.assertEqual(resolve(url).func, frontpage)

    def test_url_signup_is_resolved(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, signup)

    def test_url_delete_workingtime_is_resolved(self):
        url = reverse('delete_workingtime')
        self.assertEqual(resolve(url).func, delete_workingtime)

    def test_url_working_is_resolved(self):
        url = reverse('working')
        self.assertEqual(resolve(url).func, working)

    def test_url_start_working_is_resolved(self):
        url = reverse('start_working')
        self.assertEqual(resolve(url).func, start_working)

    def test_url_end_working_is_resolved(self):
        url = reverse('end_working')
        self.assertEqual(resolve(url).func, end_working)

    def test_url_tips_is_resolved(self):
        url = reverse('views_employees')
        self.assertEqual(resolve(url).func, views_employees)

    def test_url_tips_shared_is_resolved(self):
        url = reverse('tips_shared')
        self.assertEqual(resolve(url).func, tips_shared)

