from django.http import JsonResponse
from django.views.generic import View


class ScraperAPI(View):
    def get(self, *args, **kwargs):
        data = {}
        return JsonResponse(data)

    def post(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass
