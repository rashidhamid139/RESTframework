from django.urls import path
from .views import default_map

urlpatterns = [
    path('', default_map, name="default"),
]