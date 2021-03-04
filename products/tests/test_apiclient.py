"""Test requests on API of OpenFoodFacts"""

from django.test import TestCase
from unittest.mock import patch

from products.requests_to_OFF.apiclient import OpenfoodfactsClient


class OpenFoodFactsClientTest(TestCase):
    """Class to test OpenFoodFacts client"""
    url = (
        "https://fr.openfoodfacts.org/cgi/search.pl"
    )
    page_size = 2
    number_of_pages = 1
    params = {
                "action": "process",
                "sort_by": "unique_scans_n",  # popularity
                "page_size": page_size,
                "page": number_of_pages,
                "json": True,
            }
    response = {
        'products':
            [
                {
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
                },
                {
                    'product_name': 'eau de source cristalline',
                    'generic_name': 'eau de source',
                    'nutriscore_grade': 'a',
                    'url': 'https://fr.openfoodfacts.org/produit2',
                    'image_url': 'https://fr.openfoodfacts.org/produit2.jpg',
                    'image_nutrition_url': (
                        'https://fr.openfoodfacts.org/produit/eau.jpg'
                    ),
                    'categories': 'eau, boisson, source'
                }

            ]
    }

    results = [
                {
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
                },
                {
                    'product_name': 'eau de source cristalline',
                    'generic_name': 'eau de source',
                    'nutriscore_grade': 'a',
                    'url': 'https://fr.openfoodfacts.org/produit2',
                    'image_url': 'https://fr.openfoodfacts.org/produit2.jpg',
                    'image_nutrition_url': (
                        'https://fr.openfoodfacts.org/produit/eau.jpg'
                    ),
                    'categories': 'eau, boisson, source'
                }

            ]

    @patch('requests.get')
    def test_get_products(self, mock_request):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.return_value.json.return_value = self.response

        client = (
            OpenfoodfactsClient()
            .get_products_by_popularity(self.page_size,
                                        self.number_of_pages)
                  )

        self.assertEqual(self.results, client)
        print(mock_request.assert_called_with(self.url, params=self.params))
