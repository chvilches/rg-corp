import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import TestCase, Client
from django.urls import reverse
from .models import Scraper


class ApiViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        bitcoin = Scraper.objects.create(currency="Bitcoin", frequency=60)
        bitcoin.values.create(value=60)
        bitcoin.values.create(value=70)
        tether = Scraper.objects.create(currency="Tether", frequency=25)
        tether.values.create(value=50)
        tether.values.create(value=55)
        tether.values.create(value=80)

    def test_get_scraper_api(self):
        """ scraper api returns 200 """

        response = self.client.get(reverse('scrapers'), content_type="application/json")
        data = response.json()['scrapers']
        self.assertEqual(data[0]['currency'], 'Bitcoin')
        self.assertEqual(data[1]['currency'], 'Tether')
        # todo en al json llega un integer y acá string
        self.assertEqual(data[0]['value'], '70')
        self.assertEqual(data[1]['value'], '80')
        self.assertEqual(response.status_code, 200)

    def test_post_screaper_api(self):
        """  api created  scraper """
        response = self.client.post(
            reverse('scrapers'),
            json.dumps({'currency': 'Cosmos', 'frequency': 25}),
            content_type="application/json"
        )
        data = response.json()
        scraper = Scraper.objects.all().last()

        self.assertEqual(data['currency'], scraper.currency)
        self.assertEqual(data['frequency'], scraper.frequency)
        self.assertEqual(response.status_code, 200)

    def test_post_invalid_screaper_api(self):
        """  api created  scraper """
        response_invalid_currency = self.client.post(
            reverse('scrapers'), {'currency': 'Bidtcoin', 'frequency': 25}, content_type="application/json"
        )
        data_invalid_currency = response_invalid_currency.json()

        response_invalid_frequency = self.client.post(
            reverse('scrapers'), {'currency': 'Bitcoin', 'frequency': 0}, content_type="application/json"
        )
        data_invalid_frequency = response_invalid_frequency.json()

        response_invalid_exists = self.client.post(
            reverse('scrapers'), {'currency': 'Bitcoin', 'frequency': 20}, content_type="application/json"
        )
        data_invalid_exists = response_invalid_exists.json()

        self.assertEqual(data_invalid_currency['error'], "Invalid currency, see https://coinmarketcap.com")
        self.assertEqual(data_invalid_frequency['error'], "Invalid frequency")
        self.assertEqual(data_invalid_exists['error'], "This currency already exists")
        self.assertEqual(response_invalid_exists.status_code, 400)
        self.assertEqual(response_invalid_frequency.status_code, 400)
        self.assertEqual(response_invalid_currency.status_code, 400)

    def test_put_screaper_api(self):
        """  api created  scraper """
        response = self.client.put(reverse('scrapers'), {'id': 1, 'frequency': 25}, content_type="application/json")
        data = response.json()

        scraper = Scraper.objects.get(pk=1)
        self.assertEqual(data['msg'], "Scraper updated")
        self.assertEqual(scraper.frequency, 25)
        self.assertEqual(response.status_code, 200)

    def test_put_screaper_api(self):
        """  api created  scraper """
        response = self.client.put(reverse('scrapers'), {'id': 20, 'frequency': 25}, content_type="application/json")
        data = response.json()

        self.assertEqual(data['error'], "This Scraper not exists")
        self.assertEqual(response.status_code, 400)

    def test_delete_screaper_api(self):
        """  api delete  scraper """
        response = self.client.delete(reverse('scrapers'), {'id': 1}, content_type="application/json")
        data = response.json()
        scraper = Scraper.objects.filter(pk=1)
        self.assertEqual(data['msg'], "Scraper deleted")
        self.assertEqual(len(scraper), 0)
        self.assertEqual(response.status_code, 200)

    def test_delete_invalid_screaper_api(self):
        """  api delete  scraper """
        response_a = self.client.delete(reverse('scrapers'), {'id': 0}, content_type="application/json")
        response_b = self.client.delete(reverse('scrapers'), {'id': 500}, content_type="application/json")
        data_a = response_a.json()
        data_b = response_b.json()
        self.assertEqual(data_a['error'], "Invalid id")
        self.assertEqual(response_a.status_code, 400)
        self.assertEqual(data_b['error'], "This Scraper not exists")
        self.assertEqual(response_b.status_code, 400)
