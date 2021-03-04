"""Normalizer to normalize data from OpenFoodFacts"""


def remove_unuseful_fields(product):
    """Remove fields don't use in products app"""
    useful_fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in product.keys() - useful_fields:
        del product[field]


def transform_fields_into_lowercase_letters(product):
    """Transform fields name in lowercase"""
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in fields:
        product[field] = product[field].lower()


def transform_categories_into_list(product):
    """Transforms categories fields in list with each category"""
    product['categories'] = [
        category.strip() for category in product['categories'].split(',')
    ]


def transform_field_names(product):
    """Modify fields names"""
    transformations = {
        "product_name": "name",
        "generic_name": "description",
        "nutriscore_grade": "nutriscore"
    }
    for old_field, new_field in transformations.items():
        product[new_field] = product[old_field]
        del product[old_field]


class ProductNormalizer:
    """Class to normalize product dictionnary"""

    normalizers = [
        remove_unuseful_fields,
        transform_fields_into_lowercase_letters,
        transform_categories_into_list,
        transform_field_names
    ]

    def normalize(self, product):
        """Normalize an individual product with normalizers
        provided.
        Args:
            A product
        Return:
            A product normalized"""
        for normalizer in self.normalizers:
            normalizer(product)

        return product

    def normalize_all(self, products):
        """Normalize each product with normalize
        method provided.
        Args:
            A product list
        Return:
            A product list normalized"""
        for product in products:
            self.normalize(product)
