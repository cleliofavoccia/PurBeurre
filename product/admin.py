from django.contrib import admin
from .models import Product, Category


# Define the admin class
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'nutriscore')


class CategoryAdmin(admin.ModelAdmin):
    pass


# Register the admin class with the associated model
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)