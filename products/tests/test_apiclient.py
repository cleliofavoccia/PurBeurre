# """Test requests on API of OpenFoodFacts"""
# import requests
#
# from django.test import TestCase
#
# from unittest.mock import MagicMock, patch, create_autospec
#
# from products.requests_to_OFF.apiclient import OpenfoodfactsClient
#
#
# # @patch('products.requests_to_OFF.apiclient.OpenfoodfactsClient')
# class OpenfoodfactsClientTest(TestCase):
#     """Tests methods from OpenfoodfactsClient class in apiclient.py"""
#
#     def test_passing_good_arguments_in_get_products_by_popularity(self):
#         page_size = 1
#         number_of_pages = 1
#         mock_function = create_autospec(
#             OpenfoodfactsClient.get_products_by_popularity,
#             return_value='OK')
#
#         self.assertEqual(
#             mock_function(self, page_size=page_size,
#                           number_of_pages=number_of_pages),
#             mock_function(self, page_size=10,
#                           number_of_pages=20)
#                         )
#
#         self.assertNotEqual(
#             mock_function(self, page_size=page_size,
#                           number_of_pages=number_of_pages),
#             mock_function(self, page_size=1)
#                         )
#
#     def test_OpenfoodfactsClient_return_products_from_database(self):
#         """Receive a number of products to download and returns a dictionnary
#          with products"""
#         # country = 'fr'
#         # url = (f"https://{country}.openfoodfacts.org/cgi/search.pl",)
#         # params = {
#         #     "action": "process",
#         #     "sort_by": "unique_scans_n",  # popularity
#         #     "page_size": page_size,
#         #     "page": page,
#         #     "json": True,
#         # }
#         results = {
#             'products':
#                 [
#                     {
#                       'product_name': 'nutella',
#                       'generic_name' : 'pate a tartiner au chocolat et a la noisette',
#                       'nutriscore_grade': 'e',
#                       'url': 'https://fr.openfoodfacts.org/produit',
#                       'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
#                       'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
#                       'categories': 'pate a tartiner, chocolat, noisette'
#                     },
#                     {
#                         'product_name': 'nutella',
#                         'generic_name': 'pate a tartiner au chocolat et a la noisette',
#                         'nutriscore_grade': 'e',
#                         'url': 'https://fr.openfoodfacts.org/produit',
#                         'image_url': 'https://fr.openfoodfacts.org/produit.jpg',
#                         'image_nutrition_url': 'https://fr.openfoodfacts.org/produit/nut.jpg',
#                         'categories': 'pate a tartiner, chocolat, noisette'
#                     }
#                 ]
#             }
#         off_client = OpenfoodfactsClient()
#         off_client.get_products_by_popularity = MagicMock(return_value=results)
#
#         self.assertEqual(off_client.get_products_by_popularity(1, 1), results)
