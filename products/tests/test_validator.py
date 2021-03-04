"""Test the data validator of Open Food Facts recovered data """

from django.test import TestCase

from products.requests_to_OFF.validator import ProductValidator


class ProductValidatorTest(TestCase):
    """Tests of methods from ProductValidator class in validator.py"""

    good_product = {
                  'product_name': 'nutella',
                  'generic_name': (
                      'pate a tartiner au chocolat et a la noisette'
                  ),
                  'nutriscore_grade': 'e',
                  'url': 'https://fr.openfoodfacts.org/produit',
                  'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
                  'image_nutrition_url': (
                      'https://fr.openfoodfacts.org/produit/nut.jpg'
                  ),
                  'categories': 'pate a tartiner, chocolat, noisette'
                }

    bad_product = {
                  'product_name': 'nutella',
                  'generic_name': (
                      'pate a tartiner au chocolat et a la noisette'
                  ),
                  'url': 'https://fr.openfoodfacts.org/produit',
                  'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
                  'image_nutrition_url': (
                      'https://fr.openfoodfacts.org/produit/nut.jpg'
                  ),
                  'categories': 'pate a tartiner, chocolat, noisette',
                }

    def test_is_valid_return_only_good_products(self):
        """Test if method is_valid receive a product and verify
        his dictionnary datas and return True if the product
        has all is wanted, no more, no less"""
        self.assertTrue(ProductValidator().is_valid(self.good_product))
        self.assertFalse(ProductValidator().is_valid(self.bad_product))

    def test_filter_remove_only_bad_products(self):
        """Receive products and remove bad products"""
        list_of_products = [self.good_product, self.bad_product]
        self.assertEqual(
            ProductValidator().filter(list_of_products),
            [self.good_product])
