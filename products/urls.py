"""URLS of products app"""
from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('results/', views.ResultsListView.as_view(), name='results')
    ]
