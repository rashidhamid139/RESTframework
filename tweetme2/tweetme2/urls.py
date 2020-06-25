
from django.contrib import admin
from django.urls import path, include
from tweets.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('api/tweets/', include('tweets.urls')),
]

