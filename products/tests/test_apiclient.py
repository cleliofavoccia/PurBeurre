"""Test requests on API of OpenFoodFacts"""

import requests

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

    no_response = []

    @patch('requests.get')
    def test_get_products_by_popularity_return_good_results(
            self, mock_request
    ):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.return_value.json.return_value = self.response

        client = (
            OpenfoodfactsClient()
            .get_products_by_popularity(self.page_size,
                                        self.number_of_pages)
                  )

        self.assertEqual(self.results, client)

    @patch('requests.get')
    def test_get_products_by_popularity_have_good_parameters(
            self, mock_request
    ):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.return_value.json.return_value = self.response

        OpenfoodfactsClient().get_products_by_popularity(
            self.page_size,
            self.number_of_pages
        )

        mock_request.assert_called_with(
            self.url, params=self.params
        )

    @patch('requests.get')
    def test_get_products_by_popularity_return_HTTP_error(
            self, mock_request
    ):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.return_value.raise_for_status.side_effect = (
            requests.HTTPError
        )

        client = (
            OpenfoodfactsClient()
            .get_products_by_popularity(self.page_size,
                                        self.number_of_pages)
        )

        self.assertEqual(self.no_response, client)

    @patch('requests.get')
    def test_get_products_by_popularity_return_request_exception(
            self, mock_request
    ):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.side_effect = requests.RequestException

        client = (
            OpenfoodfactsClient()
            .get_products_by_popularity(self.page_size,
                                        self.number_of_pages)
        )

        self.assertEqual(self.no_response, client)

    @patch('requests.get')
    def test_get_products_by_popularity_return_JSONDecodeError(
            self, mock_request
    ):
        """Method to test get_products_by_popularity method
        from OpenFoodFactsClient with a mock on requests.get"""
        mock_request.return_value.json.side_effect = (
            mock_request.json.JSONDecodeError(
                "msg", "nofile", 0
            )
        )

        client = (
            OpenfoodfactsClient()
            .get_products_by_popularity(self.page_size,
                                        self.number_of_pages)
        )

        self.assertEqual(self.no_response, client)
