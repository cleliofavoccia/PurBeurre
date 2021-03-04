"""Manager of Products objects in Django admin"""
from django.contrib import admin
from .models import Product, Category


# Define the admin class
class ProductAdmin(admin.ModelAdmin):
    """Class that manage Products objects in Django admin """
    list_display = ('name', 'nutriscore')


class CategoryAdmin(admin.ModelAdmin):
    """Class that manage Category objects in Django admin """
    pass


# Register the admin class with the associated model
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
