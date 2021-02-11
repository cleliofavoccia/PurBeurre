"""Command to fill the Django database create
by models with Open Food Facts datas"""

import requests
from django.core.management.base import BaseCommand, CommandError
from products.models import Product, Category


class Command(BaseCommand):
    """Attributes and method useful for fill
    the database with Open Food Facts datas"""

    def download(self, i):

        number_of_products = 1000

        request = requests.get('https://fr.openfoodfacts.org/?sort_by=popularity&page_size=%s.json'
                               % number_of_products)
        response = request.json()
        try:
            product = [
                        response['products'][i]['product_name'],
                        response['products'][i]['generic_name_fr'],
                        response['products'][i]['nutriscore_grade'],
                        response['products'][i]['url'],
                        response['products'][i]['image_url'],
                        response['products'][i]['image_nutrition_url'],
                        response['products'][i]['categories']
                        ]
        except KeyError:
            return None
        return product

    def clean(self, product):
        """Delete products that don't respect the product format"""
        for i in product:
            if i is None or i == "":
                pass
            else:
                return i

    def handle(self, *args, **kwargs):
        """Fetch bests products on OFF"""

        # request = requests.get('https://fr.openfoodfacts.org/?sort_by=popularity&page_size=1000.json')
        # response = request.json()

        # Collect 1000 products

        # for i in range(1000):
        #     # Record a new Product instance
        #     record_product = Product(name=response['products'][i]['product_name'],
        #                              description=response['products'][i]['generic_name_fr'],
        #                              nutriscore=response['products'][i]['nutriscore_grade'],
        #                              url=response['products'][i]['url'],
        #                              image_url=response['products'][i]['image_url'],
        #                              nutrition_image_url=response['products'][i]['image_nutrition_url'])

        for i in range(1000):
            product = self.download(i)
            if product is None:
                continue
            else:
                self.clean(product)

            record_product = Product(name=product[0],
                                     description=product[1],
                                     nutriscore=product[2],
                                     url=product[3],
                                     image_url=product[4],
                                     nutrition_image_url=product[5])

            # Save this new Product instance
            record_product.save()

            # Transform categories of Product instance in a list of categories
            categories = product[6].split(",")

            # Iterate on categories list
            for j in range(len(categories)):
                # Record a new Category instance
                record_category = Category(name=categories[j])
                # Save this new Category instance
                record_category.save()

                # Get the Product instance recorded just before
                # products = Product.objects.filter(name=response['products'][i]['product_name'])

                # Associate the Product instance recorded before with
                # the Category instance recorded just before
                record_product.categories.add(record_category)

            self.stdout.write(self.style.SUCCESS('"%s" is successfully added' % product[0]))

            # class Cleaner:
            #     validators = []
            #     normalizers = []
            #
            #     def is_valid(self, data):
            #         for validator in self.validators:
            #             if not validator(data):
            #                 return False
            #         return True
            #
            #     def normalize(self, data):
            #         for normalizer in self.normalizers:
            #             data = normalizer(data)
            #         return data
            #
            #     def clean(self, collection):
            #         return [
            #             self.normalize(data) for data in collection if self.is_valid(data)
            #         ]