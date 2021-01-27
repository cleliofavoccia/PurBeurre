from django.urls import path

from . import views

app_name = 'site_web'
urlpatterns = [
    path('', views.index, name='index'),
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
]



