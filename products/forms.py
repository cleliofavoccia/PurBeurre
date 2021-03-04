"""Forms of products app"""
from django import forms


class SubstituteForm(forms.Form):
    """Form that send a product to find his substitutes
    (product with a better nutriscore than the product
    requested)"""
    research = forms.CharField(max_length=100,
                               label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'nutella'}
                                )
                               )
