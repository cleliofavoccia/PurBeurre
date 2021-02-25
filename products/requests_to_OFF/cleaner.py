from .normalizer import ProductNormalizer
from .validator import ProductValidator


class Cleaner:

    def clean(self, products):
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        filtered_products = validator.filter(products)
        normalizer.normalize_all(filtered_products)

        return filtered_products
