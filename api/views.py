from django.http import JsonResponse
from django.views.generic import View
from .models import Scraper
from .validators import currency_serializer, get_valid_data


class ScraperAPI(View):

    def get(self, *args, **kwargs):

        currencies = Scraper.objects.all()
        data = {"scrapers": list(map(currency_serializer, currencies))}

        return JsonResponse(data)

    def post(self, *args, **kwargs):

        data, is_valid = get_valid_data('POST', self.request.body)

        if not is_valid:
            return JsonResponse(data, status=400)

        if Scraper.objects.filter(currency=data['currency']).count() != 0:
            return JsonResponse({"error": "This currency already exists"}, status=400)

        scraper = Scraper.objects.create(currency=data['currency'], frequency=data['frequency'])
        scraper.values.create(value=0)
        data = {
            "id"        : scraper.id,
            "created_at": scraper.create_at,
            "currency"  : scraper.currency,
            "frequency" : scraper.frequency
        }

        return JsonResponse(data)

    def put(self, *args, **kwargs):
        data, is_valid = get_valid_data('PUT', self.request.body)

        if not is_valid:
            return JsonResponse(data, status=400)

        if Scraper.objects.filter(pk=data['id']).count() == 0:
            return JsonResponse({"error": "This Scraper not exists"}, status=400)



        Scraper.objects.filter(pk=int(data['id'])).update(frequency=int(data['frequency']))

        data = {"msg": "Scraper updated"}
        return JsonResponse(data)

    def delete(self, *args, **kwargs):
        data, is_valid = get_valid_data('DELETE', self.request.body)

        if not is_valid:
            return JsonResponse(data, status=400)

        if Scraper.objects.filter(pk=data['id']).count() == 0:
            return JsonResponse({"error": "This Scraper not exists"}, status=400)

        Scraper.objects.filter(pk=data['id']).delete()
        data = {"msg": "Scraper deleted"}
        return JsonResponse(data)
