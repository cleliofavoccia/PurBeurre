from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

@login_required
def user_account(request):
    """Print user_account.html in website"""
    return render(request, 'user_account.html')


class SignIn(View):
    """Generic class-based view detailed CreateUserForm"""
    form = CreateUserForm()

    def get(self, request):
        return render(request, 'users/sign_in.html', {'form': self.form})

    def post(self, request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = CreateUserForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                form.save()
                # redirect to a new URL:
                return redirect('website:index')
            else:
                return render(request, 'users/sign_in.html', {'form': form})
