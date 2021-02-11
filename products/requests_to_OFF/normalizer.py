
def remove_unuseful_fields(product):
    useful_fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in product.keys() - useful_fields:
        del product[field]


def transform_fields_into_lowercase_letters(product):
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in fields:
        product[field] = product[field].lower()


def transform_categories_into_list(product):
    product['categories'] = [
        category.strip() for category in product['categories'].split(',')
    ]


def transform_field_names(product):
    transformations = {
        "product_name": "name",
        "generic_name": "description",
        "nutriscore_grade": "nutriscore"
    }
    for old_field, new_field in transformations.items():
        product[new_field] = product[old_field]
        del product[old_field]


class ProductNormalizer:
    """Objet permettant de normaliser les dictionnaires de produits."""

    normalizers = [
        remove_unuseful_fields,
        transform_fields_into_lowercase_letters,
        transform_categories_into_list,
        transform_field_names
    ]

    def normalize(self, product):
        """Normalise un produit individuel en utilisant les
        normaliseurs fournis.
        """
        for normalizer in self.normalizers:
            normalizer(product)

    def normalize_all(self, products):
        """Normalise chaque produit présent dans la liste de produits
        fournie.
        """
        for product in products:
            self.normalize(product)
