"""Models of products app"""
from django.db import models


class Category(models.Model):
    """Products Categories"""

    # Fields
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """Print attribute as title's object in Django admin"""
        return self.name


class Product(models.Model):
    """Products with a name, description, nutriscore
    categories, url on page product of OpenFoodFacts,
    image url from OpenFoodFacts and nutrition image url
    from OpenFoodFacts"""

    # Fields
    name = models.CharField('product name', max_length=100)
    description = models.TextField('product description')
    nutriscore = models.CharField('product nutriscore', max_length=1)
    categories = models.ManyToManyField('Category', related_name='products')
    url = models.URLField('product url')
    image_url = models.URLField('product image url')
    nutrition_image_url = models.URLField('product nutrition image url')

    def __str__(self):
        """Print attribute as title's object in Django admin"""
        return self.name
