from django.test import TestCase, Client
from django.urls import reverse
from .models import Scraper


class ApiViewTestCase(TestCase):
    def setUp(self):
        client = Client()
        bitcoin = Scraper.objects.create(currency="bitcoin", frequency=60)
        bitcoin.values.create(value=60)
        bitcoin.values.create(value=70)
        tether = Scraper.objects.create(currency="tether",frequency=25 )
        tether.values.create(value=50)
        tether.values.create(value=55)
        tether.values.create(value=80)

    def test_get_scraper_api(self):
        """ scraper api returns 200 """

        response = self.client.get(reverse('scrapers'))

        self.assertEqual(response.json()['scrapers'][0]['currency'], 'bitcoin')
        self.assertEqual(response.json()['scrapers'][0]['value'], 70)
        self.assertEqual(response.json()['scrapers'][1]['currency'], 'tether')
        self.assertEqual(response.json()['scrapers'][1]['value'], 80)
        self.assertEqual(response.status_code, 200)
