from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Favorite


class FavoriteCreateView(LoginRequiredMixin, generic.View):
    """Generic class-based view listing all products
    added to favorites by an users"""
    model = Favorite
    template_name = 'favorites/favoritebyuser_list.html'

    def post(self, request):
        if request.method == 'POST':
            print(self.request.POST)
            base_product = self.request.POST['base_product']
            substitute = self.request.POST['substitute']
            user = self.request.POST['user']

            favorite = Favorite(user=user, product=base_product, substitute=substitute)
            favorite.save()

    def get_context_data(self, request, **kwargs):
        context = super().get_context_data(**kwargs)

        if context['object_list']:
            base_product = self.request.POST['base_product']
            substitute = self.request.POST['substitute']
            user = self.request.POST['user']
            context['base_product'] = base_product
            context['substitute'] = substitute
            context['user'] = user

            return context
        else:
            context['base_product'] = 'Tu n\'as rien enregistré !'
            return context
