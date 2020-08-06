from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('hv', views.HomeView.as_view(), name='home'),
    path('task/<str:task_id>/', views.TaskView.as_view(), name='task'),
]