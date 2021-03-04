"""Cleaner to make usable data from OpenFoodFacts"""
from .normalizer import ProductNormalizer
from .validator import ProductValidator


class Cleaner:
    """Class to make usable data from OpenFoodFacts"""

    def clean(self, products):
        """Method to validate and normalize
        data from OpenFoodFacts"""
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        filtered_products = validator.filter(products)
        normalizer.normalize_all(filtered_products)

        return filtered_products
