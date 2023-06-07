from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Item
import os


@receiver(post_delete, sender=Item)
def delete_item_photo(sender, instance, **kwargs):
    # Видалення файлу фотографії після видалення екземпляру Item
    if instance.image:
        # Отримати шлях до файлу
        file_path = instance.image.path
        # Видалити файл
        if os.path.exists(file_path):
            os.remove(file_path)