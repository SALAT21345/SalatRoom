
from django.contrib import admin
from django.urls import path, include
from allmembers import views

urlpatterns = [
    path('', views.Members, name='members'),
    
    
]
