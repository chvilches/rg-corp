from django.db.models import Max, F
from django.http import JsonResponse, QueryDict
from django.views.generic import View
from .models import Scraper
import json

def currency_serializer(q):
    return {
        "id"              : q['id'],
        "created_at"      : q['create_at'],
        "currency"        : q['currency'],
        "frequency"       : q['frequency'],
        "value"           : q['values__value'],
        "value_updated_at": q['value_updated_at'],
    }


class ScraperAPI(View):
    def get(self, *args, **kwargs):
        currencies = Scraper.objects.annotate(
            value_updated_at=Max('values__create_at')
        ).filter(
            values__create_at=F('value_updated_at')
        ).values(
            'id', 'create_at', 'currency', 'frequency', 'value_updated_at', 'values__value'
        )

        data = {
            "scrapers": list(map(currency_serializer, currencies))
        }
        return JsonResponse(data)

    def post(self, *args, **kwargs):
        # todo faltan validaciones
        data = self.request.POST

        scraper, created = Scraper.objects.get_or_create(
            currency=data['currency'],
            frequency=data['frequency']
        )

        data = {
            "id"        : scraper.id,
            "created_at": scraper.create_at,
            "currency"  : scraper.currency,
            "frequency" : scraper.frequency
        }

        return JsonResponse(data)

    def put(self, *args, **kwargs):
        # todo faltan validaciones
        data = json.loads(self.request.body.decode().replace("\'", "\""))

        Scraper.objects.filter(
            pk=int(data['id'])
        ).update(
            frequency=int(data['frequency'])
        )

        data = {
            "msg": "Scraper updated"
        }
        return JsonResponse(data)

    def delete(self, *args, **kwargs):
        # todo faltan validaciones
        data = json.loads(self.request.body.decode().replace("\'", "\""))

        Scraper.objects.filter(
            pk=int(data['id'])
        ).delete()

        data = {
            "msg": "Scraper deleted"
        }
        return JsonResponse(data)
