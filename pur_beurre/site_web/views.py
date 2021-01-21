from django.shortcuts import render
from django.http import HttpResponse

from models import User, Category, Product, Favorite
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class ProductListView(generic.ListView):
    """Generic class-based view listing all products"""
    model = Product


class ProductsByCategoryListView(generic.ListView):
    """Generic class-based view listing all products"""
    model = Product


class ProductDetailView(generic.DetailView):
    """Generic class-based view detailed all products"""
    model = Product


class FavoritebyUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing all products
    added to favorite by an user"""
    model = Favorite


def index(request):
    """Print index.html in website"""
    return render(request, 'index.html')


@login_required
def user_account(request):
    """Print user_account.html in website"""
    return render(request, 'user_account.html')


def legal_mentions(request):
    """Print legal_mentions.html in website"""
    return render(request, 'legal_mentions.html')


def login(request):
    return render(request, 'login.html')


def logged_out(request):
    return render(request, 'logged_out.html')