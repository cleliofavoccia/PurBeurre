from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Favorite


class FavoritebyUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing all products
    added to favorites by an users"""
    model = Favorite
