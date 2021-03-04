"""Test the data cleaner of Open Food Facts recovered data """

from django.test import TestCase

from products.requests_to_OFF.cleaner import Cleaner


class CleanerTest(TestCase):
    """Test Cleaner to clean product form Open Food Facts database"""
    maxDiff = None

    final_good_product = {
     'name': 'nutella',
     'description': 'pate a tartiner au chocolat et a la noisette',
     'nutriscore': 'e',
     'url': 'https://fr.openfoodfacts.org/produit',
     'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
     'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
     'categories': ['pate a tartiner', 'chocolat', 'noisette']
    }

    good_product = {
        'product_name': 'nutella',
        'generic_name': 'pate a tartiner au chocolat et a la noisette',
        'nutriscore_grade': 'e',
        'url': 'https://fr.openfoodfacts.org/produit',
        'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
        'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
        'categories': 'pate a tartiner, chocolat, noisette'
    }

    bad_product_no_valid = {
     'product_name': 'nutella',
     'generic_name': 'pate a tartiner au chocolat et a la noisette',
     'url': 'https://fr.openfoodfacts.org/produit',
     'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
     'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
     'categories': 'pate a tartiner, chocolat, noisette'
    }

    bad_product_valid = {
              'product_name': 'nutella',
              'generic_name': 'Pate a Tartiner au Chocolat et a la Noisette',
              'nutriscore_grade': 'e',
              'url': 'https://fr.openfoodfacts.org/produit',
              'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
              'image_nutrition_url': (
                  'https://fr.openfoodfacts.org/produit/nut.jpg'
              ),
              'categories': 'pate a tartiner, chocolat, noisette',
              'popularity': 'Very Good'
    }

    list_of_products = [good_product, bad_product_no_valid, bad_product_valid]

    def test_clean_return_only_good_product(self):
        """Test if method clean receive a list of products and
        execute validator and normalizer class to return datas
        validates and normalized"""
        list_of_products_cleaned = [self.final_good_product,
                                    self.final_good_product]
        # print(Cleaner().clean(self.list_of_products))
        self.assertEqual(
            Cleaner().clean(self.list_of_products),
            list_of_products_cleaned)
