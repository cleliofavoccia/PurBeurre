from django.urls import path

from . import views

app_name = 'product'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:id>/', views.ProductDetailView.as_view(), name='product'),
    ]