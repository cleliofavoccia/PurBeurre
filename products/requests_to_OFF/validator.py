"""Validator to validate datas from OpenFoodFacts"""


def validate_fields_are_present_in_product(product):
    """Return True if all fields wanted are present in product
    dictionnary. If not return False"""
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    if fields - product.keys():
        return False
    return True


def validate_fields_are_not_empty_in_product(product):
    """Return True if fields wanted are not empty.
    If it is return False."""
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in fields:
        if isinstance(product[field], str) and not product[field].strip():
            return False
    return True


class ProductValidator:
    """Class that validates products with certain parameters and
    remove from recovered datas from Open Food Facts those aren't
    validates"""

    validators = [
        validate_fields_are_present_in_product,
        validate_fields_are_not_empty_in_product
    ]

    def is_valid(self, product):
        """
        Args:
            product (dict)
        Return:
            True if the product is valid.
        """
        for validator in self.validators:
            if not validator(product):
                return False
        return True

    def filter(self, products):
        """Remove non validates products from list of products
        Args:
            products (list): list of products to filtrate.
        Return:
            All products from the list that valid.
        """
        filtered_products = []
        for product in products:
            if self.is_valid(product):
                filtered_products.append(product)
        return filtered_products
