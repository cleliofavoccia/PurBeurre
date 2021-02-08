from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm


class User(AbstractUser):
    """Users of website"""
    pass


class CreateUserForm(UserCreationForm):
    """ Sign in forms to permit the user to register him"""
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

# 'password1', 'password2'