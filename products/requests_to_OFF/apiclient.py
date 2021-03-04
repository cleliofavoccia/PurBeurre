"""File with class OpenfoodfactsClient
to communicate with Open Food Facts API"""
import json
import requests


# class APIError(Exception):
#     pass
class OpenfoodfactsClient:
    """Attributes and methods to do things with Open Food Facts API"""

    def __init__(self, country="fr"):
        """Attribute of OpenFoodFactsClient, here the URL to call the API"""
        if country not in ("fr", "en", "world"):
            raise ValueError("Country must be fr, en or world")
        self.url = f"https://{country}.openfoodfacts.org/cgi/search.pl"

    def get_products_by_popularity(self, page_size, number_of_pages):
        """Download products from Open Food Facts database order by popularity

        Args:
            number_of_pages: number of pages to download
            page_size: number of products per pages to download

        Return:
            Dictionnary with product informations

        Exceptions:
            Return messages if Openfoodfacts API is down
            or the user is not connected.

        """
        products = []
        for page in range(1, number_of_pages + 1):
            params = {
                "action": "process",
                "sort_by": "unique_scans_n",  # popularity
                "page_size": page_size,
                "page": page,
                "json": True,
            }

            try:
                response = requests.get(self.url, params=params)
                response.raise_for_status()
            except requests.HTTPError:
                print("Un code d'erreur HTTP a été retourné par l'API")
                continue
            except requests.exceptions.RequestException:
                print("Une erreur de connection réseau a eu lieu")
                continue

            try:
                data = response.json()
            except json.JSONDecodeError:
                print("Une erreur de décodage à eu lieu")
                continue
            products.extend(data['products'])
        return products
