from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='list'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='detail'),
    path('results/', views.ResultsListView.as_view(), name='results')
    ]
