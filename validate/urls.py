from django.urls import path
from . import views

urlpatterns = [
    path('api/upload', views.inputexcel, name='inputexcel'),
    ]
