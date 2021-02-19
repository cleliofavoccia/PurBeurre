
from django import forms

from .models import Favorite
from products.models import Product
from django.core.exceptions import ValidationError


class FavoriteForm(forms.Form):

    def clean_product(self):
        print(self.cleaned_data)
        product_id = self.cleaned_data['product']
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise forms.ValidationError("Ce produit n'existe pas !")

        return product

    def clean_substitute(self):
        substitute_id = self.cleaned_data['substitute']
        try:
            substitute = Product.objects.get(id=substitute_id)
        except Product.DoesNotExist:
            raise forms.ValidationError("Ce produit n'existe pas !")

        return substitute

    def save(self, request, commit=True):
        print(self.cleaned_data)
        product = self.cleaned_data['product']
        substitute = self.cleaned_data['substitute']
        favorite = Favorite(user=request.user,
                            product=product,
                            substitute=substitute)
        if commit:
            favorite.save()
        return favorite
