import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from .models import News


def save_function(article_list):
    with open('articles.txt', 'w') as outfile:
        json.dump(article_list, outfile)


def yahoo_fin_rss(symbol):
    news_list = []

    try:
        url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s={}&region=US&lang=en-US'.format(
            symbol)
        r = requests.get(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(r.content, features='xml')

        news_soup = soup.findAll('item')

        for n in news_soup:
            description = n.find('description').text
            link = n.find('link').text
            pubDate = n.find('pubDate').text

            news = {
                'description': description,
                'link': link,
                'published': str(datetime.strptime(pubDate, '%a, %d %b %Y %H:%M:%S +0000'))
            }

            News(description=description, link=link, published_at=datetime.strptime(
                pubDate, '%a, %d %b %Y %H:%M:%S +0000'))
            news_list.append(news)

        return save_function(news_list)
    except Exception as e:
        print('The scraping job failed. See exception:')
        print(e)


yahoo_fin_rss('AAPL')
print('done')
