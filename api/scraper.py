from time import sleep
import threading
import requests
from .parser_html import Parser


def scraper(id):
    from .models import Scraper
    screaper = Scraper.objects.get(pk=id)
    while True:

        html = requests.get('https://coinmarketcap.com/').content.decode()
        x = html.index("<tbody>") + 7
        y = html.index("</tbody>") + 8
        html = html[x:y]

        p = Parser()
        p.feed(html)
        value = p.get_currency(screaper.currency)[1:]
        screaper.values.create(value=value)

        if Scraper.objects.filter(pk=id).count() == 0:
            break
        sleep(screaper.frequency)


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='worker', daemon=True)

    def run(self):
        from .models import Scraper
        Scraper.objects.update(run=False)

        while True:
            currencies = Scraper.objects.filter(run=False)

            for currency in currencies:
                Scraper.objects.filter(pk=currency.id).update(run=True)
                thread = threading.Thread(target=scraper, name=currency.currency, args=(currency.id,))
                thread.start()

            sleep(25)


def init_worker():
    scheduler = Worker()
    scheduler.start()
