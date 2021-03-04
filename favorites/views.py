"""Views of favorites app"""
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from .forms import FavoriteForm
from .models import Favorite


class FavoriteListView(LoginRequiredMixin, generic.ListView):
    """Favorites objects generic class-based view of a user"""
    model = Favorite
    template_name = 'favorites/favoritebyuser_list.html'

    def get_context_data(self, **kwargs):
        """Generic method to construct context for template"""
        context = super().get_context_data(**kwargs)

        list_favorites = Favorite.objects.filter(user=self.request.user)

        context['list_favorites'] = list_favorites

        return context


class FavoriteCreateView(LoginRequiredMixin, generic.View):
    """Generic class-based view to add Favorite objects in
    database"""

    def post(self, request):
        """Method POST data to FavoriteForm"""
        form = FavoriteForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('favorites:well_done')
        return redirect('favorites:fail')


class WellDoneView(LoginRequiredMixin, generic.View):
    """View to print favorite well added to database"""

    def get(self, request):
        """Method GET to print well done message"""
        context = {'msg_welldone': 'Produit ajouté à vos favoris !'}

        return render(request, 'favorites/well_done.html', context)


class FailView(LoginRequiredMixin, generic.View):
    """View listing to print favorite not added to database"""

    def get(self, request):
        """Method GET to print fail message"""
        context = {'msg_fail': 'Produit pas ajouté à vos favoris !'}

        return render(request, 'favorites/fail.html', context)
