"""Test requests on API of OpenFoodFacts"""
import requests

from django.test import TestCase
from unittest.mock import patch


class OpenFoodFactsClientTest(TestCase):
    results = {
        'products':
            [
                {
                    'product_name': 'nutella',
                    'generic_name': 'pate a tartiner au chocolat et a la noisette',
                    'nutriscore_grade': 'e',
                    'url': 'https://fr.openfoodfacts.org/produit',
                    'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
                    'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
                    'categories': 'pate a tartiner, chocolat, noisette'
                },
                {
                    'product_name': 'eau de source cristalline',
                    'generic_name': 'eau de source',
                    'nutriscore_grade': 'a',
                    'url': 'https://fr.openfoodfacts.org/produit2',
                    'image_url': 'https://fr.openfoodfacts.org/produit2.jpg',
                    'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/eau.jpg',
                    'categories': 'eau, boisson, source'
                }

            ]
    }

    @patch('requests.get')
    def test_get_products(self, mock_request):
        mock_request.return_value.json.return_value = self.results

        self.assertEqual(self.results, self.test_get_products())
