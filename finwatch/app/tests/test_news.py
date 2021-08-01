from django.test import TestCase
from app.models import News, Stock
from django.utils import timezone


class NewsTestCase(TestCase):
    def setUp(self):
        # Create Stock Symbols
        s_stock = Stock.objects.create(symbol="AAPL", name="Apple Inc")
        t_stock = Stock.objects.create(symbol="TWTR", name="Twitter")
        i_stock = Stock.objects.create(symbol="INTC", name="Intel")

        News.objects.create(stock=s_stock, description="Lorem Impus dolar sit amet",
                            link="http://apple.com", published_at=timezone.now())

        News.objects.create(stock=t_stock, description="Lorem Impus dolar sit amet",
                            link="http://twitter.com", published_at=timezone.now())

        News.objects.create(stock=i_stock, description="Lorem Impus dolar sit amet",
                            link="http://twitter.com", published_at=timezone.now())

    def test_news_can_speak(self):
        lion = News.objects.get(link="http://apple.com")
        cat = News.objects.get(link="http://twitter.com")
