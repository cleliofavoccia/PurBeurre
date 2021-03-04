"""Views of users app, all that concern users
(authentification and other things)"""

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateUserForm


class UserDetailView(LoginRequiredMixin, View):
    """View detailed user profile"""

    def get(self, request):
        """Method GET to print user informations"""
        return render(request, 'users/user_account.html')


class SignIn(View):
    """View to sign in an user with CreateUserForm"""
    form = CreateUserForm()

    def get(self, request):
        """Method GET to print the CreateUserForm
        to permit at the user to sign in"""
        return render(request, 'users/sign_in.html', {'form': self.form})

    def post(self, request):
        """Method POST to send datas input by user
        and create a User object (user account)"""
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and
            # populate it with data from the request:
            form = CreateUserForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                form.save()
                # redirect to a new URL:
                return redirect('website:index')
            else:
                return render(request, 'users/sign_in.html', {'form': form})
