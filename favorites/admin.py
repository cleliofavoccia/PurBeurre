"""Manager of Favorites objects in Django admin"""
from django.contrib import admin
from .models import Favorite


# Define the admin class
class FavoriteAdmin(admin.ModelAdmin):
    """Class that manage Favorites objects in Django admin """
    pass


# Register the admin class with the associated model
admin.site.register(Favorite, FavoriteAdmin)
