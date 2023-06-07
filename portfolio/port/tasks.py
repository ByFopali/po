# tasks.py
from datetime import datetime, timedelta
from celery import shared_task
from .models import Item, Price
from steam_community_market import Market, AppID

@shared_task
def create_price_records():
    items = Item.objects.all()
    for item in items:

        market = Market("USD")
        current_price = market.get_lowest_price(item.name, AppID.CSGO)
        sold_amount = market.get_volume(item.name, AppID.CSGO)

        price = Price(item=item, current_price=current_price, sold_amount=sold_amount, date=datetime.now())
        print(f"Created price record for item: {item.name}")
        price.save()
