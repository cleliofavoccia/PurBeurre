"""Forms to search and find products"""
from django import forms


class SubstituteForm(forms.Form):
    """Form that send a product to find his substitutes"""
    research = forms.CharField(max_length=100,
                               label='',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'nutella'}
                               )
                               )
