"""Models of users app"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Users of website"""
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=170)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
