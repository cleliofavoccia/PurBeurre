from django.views import generic

from .models import Category, Product


class ProductListView(generic.ListView):
    """Generic class-based view listing all products"""
    model = Product


class ProductsByCategoryListView(generic.ListView):
    """Generic class-based view listing all products"""
    model = Product


class ProductDetailView(generic.DetailView):
    """Generic class-based view detailed all products"""
    model = Product
