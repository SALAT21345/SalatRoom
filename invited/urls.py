from django.contrib import admin
from django.urls import path, include
from invited import views

urlpatterns = [
    path('', views.Invited, name='inv'),
    
]
