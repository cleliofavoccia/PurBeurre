"""URLS of website app"""
from django.urls import path

from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
]
