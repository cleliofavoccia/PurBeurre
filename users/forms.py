"""Forms of users app"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms


class CreateUserForm(UserCreationForm):
    """ Sign in forms to permit the users to register him"""
    class Meta:
        model = get_user_model()
        fields = ['email']
