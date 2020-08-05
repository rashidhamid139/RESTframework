from django.contrib import admin
from django.urls import path, include
from core.views import GenerateRandomUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', GenerateRandomUserView.as_view(), name='user_view' ),
]