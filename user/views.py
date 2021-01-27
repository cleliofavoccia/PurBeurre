from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def user_account(request):
    """Print user_account.html in website"""
    return render(request, 'user_account.html')


def login(request):
    return render(request, 'login.html')


def logged_out(request):
    return render(request, 'logged_out.html')
