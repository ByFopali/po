from datetime import datetime

from django.shortcuts import render
from steam_community_market import Market, AppID
from rest_framework import generics, status
from rest_framework.response import Response
import schedule
import time
from .models import Item, Price, Category
from .serializers import ItemSerializer


# Create your views here.

class AllItemsAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    # def post(self, request):
    #     name = request.data['name']
    #     image = request.data['image']
    #     category_id = request.data['category']
    #
    #     try:
    #         category = Category.objects.get(id=category_id)
    #     except Category.DoesNotExist:
    #         return Response({'error': 'Invalid category'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     item = Item.objects.create(name=name, image=image, category=category)
    #
    #     # Серіалізувати об'єкт Item за допомогою серіалізатора
    #     serializer = ItemSerializer(item)
    #
    #     data = {
    #         'message': 'Resource created successfully',
    #         'data': serializer.data  # використовувати серіалізовані дані
    #     }
    #
    #     return Response(data, status=status.HTTP_201_CREATED)

class SpecificItemAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# def create_price_record(item):
#     market = Market("USD")
#     item_name = item.name
#     current_price = market.get_lowest_price(item_name, AppID.CSGO)
#     sold_amount = market.get_volume(item_name, AppID.CSGO)
#     price = Price.objects.create(item=item, current_price=current_price, sold_amount=sold_amount, date=datetime.now())
#
#     print(f"Created price record for item: {item_name}")

# Запустити планувальник
# def run_scheduler():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)
#
# # Запуск планувальника
# run_scheduler()
