from django.test import TestCase
from django.urls import reverse


class Chapter3Tests(TestCase):
    def test_index_page_exists_at_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rango says hey there partner!")

    def test_about_page_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rango says here is the about page.")

    def test_named_urls_work_if_set(self):
        # These only pass if you set app_name='rango' and named routes in rango/urls.py
        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('rango:about'))
        self.assertEqual(response.status_code, 200)
