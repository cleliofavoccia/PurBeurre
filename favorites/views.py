from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Favorite


class FavoritebyUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing all products
    added to favorites by an users"""
    model = Favorite
    template_name = 'favorites/favoritebyuser_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if context['object_list']:
            base_product = self.kwargs['base_product']
            substitute = self.kwargs['substitute']
            user = self.kwargs['user']

            context['base_product'] = base_product
            context['substitute'] = substitute
            context['user'] = user

            favorite = Favorite(user=user, product=base_product, substitute=substitute)
            favorite.save()

            print(favorite)
            return context
        else:
            context['base_product'] = 'Tu n\'as rien enregistré !'
            return context
