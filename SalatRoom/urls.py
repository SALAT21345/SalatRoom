
from django.contrib import admin
from django.urls import path, include
from SalatSite import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='home'),
    path('news', include('news.urls')),
    path('members', include('allmembers.urls')),
    path('invited', include('invited.urls')),
]
