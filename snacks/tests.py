from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.
class SnacksTests(SimpleTestCase):
    def test_home_url_status_codes(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_url_status_codes(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_url_template_use(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")

    def test_about_url_template_use(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about.html")
