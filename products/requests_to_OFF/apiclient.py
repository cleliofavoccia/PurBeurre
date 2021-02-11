import json
import requests


class APIError(Exception):
    pass


class OpenfoodfactsClient:
    """Docstring qui explique le rôle joué par la classe."""

    def __init__(self, country="fr"):
        if country not in ("fr", "en", "world"):
            raise ValueError("Country must be fr, en or world")
        self.url = f"https://{country}.openfoodfacts.org/cgi/search.pl"

    def get_products_by_popularity(self, page_size, number_of_pages):
        """Download des produits depuis openfoodfacts par ordre de popularité.

        Args:
            number_of_pages: nombre de pages de produits à télécharger
            page_size: nombre de produit à télécharger par page (optionnel,
                la valeur par défaut est 100)

        Return:
            Liste de dictionnaires contenant les informations des produits.

        Exceptions:
            APIError: Une APIError est levée si l'API de Openfoodfacts n'est pas
                joignable ou que l'utilisateur n'est pas connecté au réseau.

        """
        products = []
        for page in range(1, number_of_pages + 1):
            params = {
                "action": "process",
                "sort_by": "unique_scans_n",  # popularité
                "page_size": page_size,
                "page": page,
                "json": True,
            }
            # Toujours supposer qu'une requête à une API peut échouer
            try:
                response = requests.get(self.url, params=params)
                response.raise_for_status()
            except requests.HTTPError:
                print("Un code d'erreur HTTP a été retourné par l'API")
                continue
            except requests.exceptions.RequestException:
                print("Une erreur de connection réseau a eu lieu")
                continue
            # On est certain qu'il n'y a pas eu d'erreur réseau
            try:
                data = response.json()
            except json.JSONDecodeError:
                print("Une erreur de décodage à eu lieu")
                continue
            products.extend(data['products'])
        return products
