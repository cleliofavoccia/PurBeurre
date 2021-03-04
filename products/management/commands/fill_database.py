"""Command to fill the Django database create
by models with Open Food Facts datas"""

from django.core.management.base import BaseCommand
from products.models import Product, Category
from products.requests_to_OFF import apiclient, cleaner


class Command(BaseCommand):
    """Attributes and method useful for fill
    the database with Open Food Facts datas"""

    def handle(self, *args, **kwargs):
        """Fetch bests products on OFF"""
        off_request = apiclient.OpenfoodfactsClient()
        cleaner_request = cleaner.Cleaner()

        products_list = (
            off_request
            .get_products_by_popularity(
                page_size=1000,
                number_of_pages=1
            )
        )

        products_list = cleaner_request.clean(products_list)

        for product in products_list:
            record_product = Product(name=product['name'],
                                     description=product['description'],
                                     nutriscore=product['nutriscore'],
                                     url=product['url'],
                                     image_url=product['image_url'],
                                     nutrition_image_url=product[
                                         'image_nutrition_url'
                                     ]
                                     )

            # Save this new Product instance
            record_product.save()

            # Iterate on categories list
            for category in product['categories']:
                # Record a new Category instance
                record_category, created = (
                    Category.objects.get_or_create(
                        name=category
                    )
                )
                # Save this new Category instance
                record_category.save()

                # Associate the Product instance recorded before with
                # the Category instance recorded just before
                record_product.categories.add(record_category)

            self.stdout.write(
                self.style.SUCCESS(
                    '"%s" is successfully added' % product['name']
                )
            )
