
from django import forms


class SubstituteForm(forms.Form):
    research = forms.CharField(max_length=100)
