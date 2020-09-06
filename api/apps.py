from django.apps import AppConfig

from api.scraper import init_worker
import os

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        if os.environ.get('RUN_WORKER', None) != 'true':
            os.environ["RUN_WORKER"] = 'true'
            from .models import Scraper
            if Scraper.objects.count() > 0:
                init_worker()