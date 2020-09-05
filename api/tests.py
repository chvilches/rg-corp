from django.test import TestCase, Client
from django.urls import reverse

class ApiViewTestCase(TestCase):
    def setUp(self):
        client = Client()

    def test_get_scraper_api(self):
        """ scraper api returns 200 """
        response = self.client.get(reverse('scrapers'))
        self.assertEqual(response.status_code, 200)
