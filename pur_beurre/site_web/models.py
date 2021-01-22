from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Categories of products"""

    # Fields
    name = models.CharField()

    def __str__(self):
        """Print attribute as title's object in admin"""
        return self.name


class Product(models.Model):
    """Products of OFF"""

    # Fields
    name = models.CharField()
    description = models.TextField()
    nutriscore = models.CharField(max_length=1)
    categories = models.ManyToManyField(Category, on_delete=models.CASCADE)

    def __str__(self):
        """Print attribute as title's object in admin"""
        return self.name


class Favorite(models.Model):
    """Favorites products added by users"""

    # Fields
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE, realted_name="favorites_as_product")
    substitute = models.ForeignKey(Product,
                                   on_delete=models.CASCADE, realted_name="favorites_as_substitute")

    def __str__(self):
        """Print attribute as title's object in admin"""
        return {'user': self.user, 'product': self.product}