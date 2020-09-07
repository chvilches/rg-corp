from django.db import models


class Scraper(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=50)
    frequency = models.IntegerField(default=0)
    run = models.BooleanField(default=False)


class ScraperValues(models.Model):
    scraper = models.ForeignKey(Scraper, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(default=0, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
