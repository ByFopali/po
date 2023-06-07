from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

class ItemPortfolio(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'ItemPortfolios'

class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_amount = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Prices'
