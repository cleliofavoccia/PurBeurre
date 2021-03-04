"""Test the data normalizer of Open Food Facts recovered data """

from django.test import TestCase

from products.requests_to_OFF.normalizer import ProductNormalizer


class ProductNormalizerTest(TestCase):
    """Test ProductNormalizer to normalize product dictionnaries"""
    maxDiff = None

    good_product = {
                  'name': 'nutella',
                  'description': (
                      'pate a tartiner au chocolat et a la noisette'
                  ),
                  'nutriscore': 'e',
                  'url': 'https://fr.openfoodfacts.org/produit',
                  'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
                  'image_nutrition_url': (
                      'https://fr.openfoodfacts.org/produit/nut.jpg'
                  ),
                  'categories': ['pate a tartiner', 'chocolat', 'noisette']
                }

    bad_product = {
                  'product_name': 'nutella',
                  'generic_name': (
                      'Pate a Tartiner au Chocolat et a la Noisette'
                  ),
                  'nutriscore_grade': 'e',
                  'url': 'https://fr.openfoodfacts.org/produit',
                  'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
                  'image_nutrition_url': (
                      'https://fr.openfoodfacts.org/produit/nut.jpg'
                  ),
                  'categories': 'pate a tartiner, chocolat, noisette',
                  'popularity': 'Very Good'
                }

    def test_normalize_return_a_normalized_product(self):
        """Test if method normalize receive a product and
        remove unuseful fields, transform fields into
        lowercase letters, transform categories into list,
        transform_field_names"""
        self.assertEqual(
            ProductNormalizer().normalize(self.bad_product),
            self.good_product)
