from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views
from . import views

urlpatterns = [
path('', views.vacsheds, name='vacshed_url'),
path('create/<int:vs>/', views.vacshed_create, name='vacshed_create_url'),
path('getvacshed/<int:vs>/', views.getvacshed_json, name='vacshed_json'),
path('itemadd/<int:id>', views.vacshed_addItem, name='additem_url')
]
