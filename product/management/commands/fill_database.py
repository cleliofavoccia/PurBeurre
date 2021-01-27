"""Command to fill the Django database create
by models with Open Food Facts datas"""

import requests
from django.core.management.base import BaseCommand, CommandError
from jean.site_web.models import Category, Product


class FillDatabaseCommand(BaseCommand):
    """Attributes and method useful for fill
    the database with Open Food Facts datas"""

    def fetch_products_and_categories_from_OFF(self):
        """Fetch bests products on OFF"""

        request = requests.get('https://fr.openfoodfacts.org/?sort_by=popularity.json')
        response = request.json()

        # Collect 20 products

        for i in range(20):
            # Record a new Product instance
            record_product = Product(name=response['products'][i]['product_name'],
                                     description=response['products'][i]['generic_name_fr'],
                                     nutriscore=response['products'][i]['nutriscore_grade'])
            # Save this new Product instance
            record_product.save()

            # Get the Product instance recorded just before
            product = Product.objects.get(name=response['products'][i]['product_name'])
            # Transform categories of Product instance in a list of categories
            categories = response['products'][i]['categories'].split(",")

            # Iterate on categories list
            for j in range(len(categories)):
                # Record a new Category instance
                record_category = Category(name=categories[j])
                # Save this new Category instance
                record_category.save()

                # Get the Category instance recorded just before
                category = Category.objects.get(name=response['products'][i]['product_name'])
                # Associate the Product instance recorded before with
                # the Category instance recorded just before
                product.entry_set.add(category)
