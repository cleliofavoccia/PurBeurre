
def validate_fields_are_present_in_product(product):
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    if fields - product.keys():
        return False
    return True


def validate_fields_are_not_empty_in_product(product):
    fields = {
        'product_name', 'generic_name', 'nutriscore_grade', 'url',
        'image_url', 'image_nutrition_url', 'categories'
    }
    for field in fields:
        if isinstance(product[field], str) and not product[field].strip():
            return False
    return True


class ProductValidator:
    """Objet responsable de valider les produits par rapport aux règles
    dans validators et de ne conserver que ceux qui sont valides.
    """

    validators = [
        validate_fields_are_present_in_product,
        validate_fields_are_not_empty_in_product
    ]

    def is_valid(self, product):
        """Retourne True si le product passé en argument est valide.
        Args:
            product (dict): dictionnaire contenant les données d'un produit
        Return:
            True si le produit est valide.
        """
        for validator in self.validators:
            if not validator(product):
                return False
        return True

    def filter(self, products):
        """Elimine les produits invalides depuis la listes de produits passée
        en argument.
        Args:
            products (list): liste de produits à filtrer.
        Return:
            Liste de produits considérés comme valides.
        """
        filtered_products = []
        for product in products:
            if self.is_valid(product):
                filtered_products.append(product)
        return filtered_products
