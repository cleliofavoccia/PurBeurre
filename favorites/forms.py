"""Forms of favorites app"""
from django import forms

from .models import Favorite
from products.models import Product
from django.core.exceptions import ValidationError


class FavoriteForm(forms.Form):
    """Form to add Favorites objects in favorite user list"""
    product = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    substitute = forms.IntegerField(widget=forms.HiddenInput(), required=True)

    def clean_product(self):
        """Return the Product object since the id input
        by user, if it exists"""
        product_id = self.cleaned_data['product']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise forms.ValidationError("Ce produit n'existe pas !")

        return product

    def clean_substitute(self):
        """Return the Product object (here the substitute)
        since the id input by user, if it exists"""
        substitute_id = self.cleaned_data['substitute']
        try:
            substitute = Product.objects.get(id=substitute_id)
        except Product.DoesNotExist:
            raise forms.ValidationError("Ce produit n'existe pas !")

        return substitute

    def save(self, user, commit=True):
        """Save the object Favorite build by
        user's profil and the products input by user"""
        product = self.cleaned_data['product']
        substitute = self.cleaned_data['substitute']
        favorite = Favorite(
            user=user, product=product, substitute=substitute
        )
        if commit:
            favorite.save()
        return favorite
