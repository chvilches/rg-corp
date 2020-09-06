from django.test import TestCase, Client
from django.urls import reverse
from .models import Scraper


class ApiViewTestCase(TestCase):
    def setUp(self):
        client = Client()
        bitcoin = Scraper.objects.create(currency="Bitcoin", frequency=60)
        bitcoin.values.create(value=60)
        bitcoin.values.create(value=70)
        tether = Scraper.objects.create(currency="Tether", frequency=25)
        tether.values.create(value=50)
        tether.values.create(value=55)
        tether.values.create(value=80)

    def test_get_scraper_api(self):
        """ scraper api returns 200 """

        response = self.client.get(reverse('scrapers'))
        data = response.json()['scrapers']

        self.assertEqual(data[0]['currency'], 'Bitcoin')
        self.assertEqual(data[0]['value'], 70)
        self.assertEqual(data[1]['currency'], 'Tether')
        self.assertEqual(data[1]['value'], 80)
        self.assertEqual(response.status_code, 200)

    def test_post_screaper_api(self):
        """  api created  scraper """
        response = self.client.post(reverse('scrapers'), {'currency': 'Bitcoin', 'frequency': 25})
        data = response.json()
        scraper = Scraper.objects.get(pk=3)

        self.assertEqual(data['currency'], scraper.currency)
        self.assertEqual(data['frequency'], str(scraper.frequency))

        self.assertEqual(response.status_code,200)

    def test_put_screaper_api(self):
        """  api created  scraper """
        response = self.client.put(reverse('scrapers'), {'id': 1, 'frequency': 25})
        data = response.json()

        scraper = Scraper.objects.get(pk=1)
        self.assertEqual(data['msg'], "Scraper updated")
        self.assertEqual(scraper.frequency, 25)
        self.assertEqual(response.status_code, 200)

    def test_delete_screaper_api(self):
        """  api created  scraper """
        response = self.client.delete(reverse('scrapers'), {'id': 1})
        data = response.json()

        scraper = Scraper.objects.filter(pk=1)
        self.assertEqual(data['msg'], "Scraper deleted")
        self.assertEqual(len(scraper), 0)
        self.assertEqual(response.status_code, 200)
