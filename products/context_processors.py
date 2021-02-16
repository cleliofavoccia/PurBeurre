
from django.shortcuts import redirect, render, get_object_or_404, reverse
from .forms import SubstituteForm
from .models import Product


def get_substitute_form(request):
    form = SubstituteForm(request.POST or None)
    return {'substitute_form': form}
