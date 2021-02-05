from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import CreateUserForm


@login_required
def user_account(request):
    """Print user_account.html in website"""
    return render(request, 'user_account.html')


def sign_in(request):
    form = CreateUserForm()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CreateUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')
    # if this is a GET request we need to print form
    else:
        return render(request, 'sign_in.html', {'form': form})
