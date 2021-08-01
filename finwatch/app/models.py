from django.db import models
from django.db.models.deletion import CASCADE


class Stock(models.Model):

    symbol = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'stock_symbols'

    def __str__(self):
        return "{}, Name {}".format(self.symbol, self.name)


class News(models.Model):

    stock = models.ForeignKey(Stock, on_delete=CASCADE)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=500, unique=True)
    published_at = models.DateTimeField()

    class Meta:
        db_table = 'stock_news'

    def __str__(self):
        return "{}, link: {}".format(self.stock.symbol, self.link)
