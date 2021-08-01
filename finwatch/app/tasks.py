from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError
import datetime
from .models import News, Stock


@shared_task(name="scrape_stocks")
def scrape_stocks():
    # fetch all stock symbols
    stocks = Stock.objects.all()

    for stock in stocks:
        try:
            url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s={}&region=US&lang=en-US'.format(
                stock.symbol)
            r = requests.get(
                url, headers={'User-Agent': 'Mozilla/5.0'})

            soup = BeautifulSoup(r.content, features='xml')

            news_soup = soup.findAll('item')

            for n in news_soup:
                description = n.find('description').text
                link = n.find('link').text
                pubDate = n.find('pubDate').text

                try:
                    # create news if not exist
                    News.objects.update_or_create(stock=stock, description=description, link=link, published_at=datetime.datetime.strptime(
                        pubDate, '%a, %d %b %Y %H:%M:%S +0000').replace(tzinfo=datetime.timezone.utc))

                except IntegrityError as e:
                    pass

        except Exception as e:
            print('The scraping job failed. See exception:')
            print(e)
            return e

    return "Scheduled task done"
