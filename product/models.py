from django.db import models


class Category(models.Model):
    """Categories of products"""

    # Fields
    name = models.CharField(max_length=40)

    def __str__(self):
        """Print attribute as title's object in admin"""
        return self.name


class Product(models.Model):
    """Products of OFF"""

    # Fields
    name = models.CharField(max_length=40)
    description = models.TextField()
    nutriscore = models.CharField(max_length=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        """Print attribute as title's object in admin"""
        return self.name
