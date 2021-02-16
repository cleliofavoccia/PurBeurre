from django.contrib import admin
from .models import Favorite


# Define the admin class
class FavoriteAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Favorite, FavoriteAdmin)
