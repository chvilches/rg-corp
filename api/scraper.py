from time import sleep
import threading
import requests
from .parser_html import Parser


def scraper_worker(id, name):
    from .models import Scraper, ScraperValues

    print(f"init scraping {name}")
    while True:
        scraper = Scraper.objects.get(pk=id)
        html = requests.get('https://coinmarketcap.com/').content.decode()
        x = html.index("<tbody>") + 7
        y = html.index("</tbody>") + 8
        html = html[x:y]
        p = Parser()
        p.feed(html)
        value = p.get_currency(scraper.currency)[1:]

        ScraperValues.objects.create(scraper_id=scraper.id, value=value)

        sleep(scraper.frequency)
        if Scraper.objects.filter(pk=id).count() == 0:
            print(f"stop scraping {scraper.currency}")
            break


class Worker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name='worker', daemon=True)

    def run(self):
        print("sleep init worker 5 seconds")
        sleep(5)
        print("init worker scraping")
        from .models import Scraper
        Scraper.objects.update(run=False)

        while True:
            currencies = Scraper.objects.filter(run=False)

            for currency in currencies:
                Scraper.objects.filter(pk=currency.id).update(run=True)
                thread = threading.Thread(
                    target=scraper_worker,
                    name=currency.currency,
                    args=(currency.id, currency.currency,)
                )
                thread.start()

            sleep(10)


def init_worker():
    scheduler = Worker()
    scheduler.start()
