from django.contrib import admin

from .models import Portfolio, Item, ItemPortfolio, Category, Price

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(Item)
admin.site.register(ItemPortfolio)
admin.site.register(Category)
admin.site.register(Price)