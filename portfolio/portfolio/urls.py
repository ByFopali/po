
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from port.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/items/', AllItemsAPIView.as_view()),
    path('api/v1/items/<int:pk>/', SpecificItemAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
