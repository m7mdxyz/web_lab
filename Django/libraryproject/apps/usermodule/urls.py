from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('lab8/task7', views.lab8_task7, name="users.lab8_task7")
]