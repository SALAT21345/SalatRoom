
from django.contrib import admin
from django.urls import path, re_path
from SalatSite import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path('news', views.news, name='news')
]
