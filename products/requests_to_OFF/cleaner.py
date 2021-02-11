from .normalizer import ProductNormalizer
from .validator import ProductValidator


class Cleaner:

    def clean(self, products):
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        validator.filter(products)
        return [
            normalizer.normalize(data) for data in products if validator.is_valid(data)
        ]

    def clean1(self, products):
        validator = ProductValidator()
        normalizer = ProductNormalizer()

        filtered_products = validator.filter(products)
        normalizer.normalize_all(filtered_products)

        return products
