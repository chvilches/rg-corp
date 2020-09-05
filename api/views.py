from django.db.models import Max, F
from django.http import JsonResponse
from django.views.generic import View
from .models import Scraper


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
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
