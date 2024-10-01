
from django.contrib import admin
from django.urls import path, include
from Game import views

urlpatterns = [
    path('', views.game, name='game'),
    
]
