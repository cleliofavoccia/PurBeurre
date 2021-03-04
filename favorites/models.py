"""Models of favorites app"""
from django.db import models
from django.conf import settings


class Favorite(models.Model):
    """Favorites association object
    between user, product and other product"""

    # Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites")

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_product",
    )
    substitute = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_substitute",
    )

    def __str__(self):
        """Print attribute as title's object in Django admin"""
        return '%s, %s' % (self.user.username, self.substitute.name)
