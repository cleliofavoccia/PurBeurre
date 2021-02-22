from django.test import TestCase

from products.models import Product, Category


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        # Set up non-modified objects used by all test methods
        nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='e',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
               'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                     '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                               '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)

    def test_name_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'product name')

    def test_description_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'product description')

    def test_nutriscore_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('nutriscore').verbose_name
        self.assertEqual(field_label, 'product nutriscore')

    def test_categories_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('categories').verbose_name
        self.assertEqual(field_label, 'categories')

    def test_url_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'product url')

    def test_image_url_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEqual(field_label, 'product image url')

    def test_nutrition_image_url_label(self):
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('nutrition_image_url').verbose_name
        self.assertEqual(field_label, 'product nutrition image url')

    def test_name_max_length(self):
        product = Product.objects.get(name='nutella')
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_nutriscore_max_length(self):
        product = Product.objects.get(name='nutella')
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEqual(max_length, 1)

    def test_categories_related_name(self):
        product = Product.objects.get(name='nutella')
        related_name = product._meta.get_field('categories').related_name
        self.assertEqual(related_name, 'products')

    def test_object_name_is_name(self):
        product = Product.objects.get(name='nutella')
        expected_object_name = product.name
        self.assertEqual(expected_object_name, str(product))

    # def test_get_absolute_url(self):
    #     author = Author.objects.get(id=1)
    #     # This will also fail if the urlconf is not defined.
    #     self.assertEqual(author.get_absolute_url(), '/catalog/author/1')


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='pate a tartiner')

    def test_object_name_is_category_name(self):
        category = Category.objects.get(name='pate a tartiner')
        expected_objet_name = category.name
        self.assertEqual(expected_objet_name, str(category))

    def test_name_max_length(self):
        product = Product.objects.get(name='nutella')
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_name_is_unique(self):
        product = Product.objects.get(name='nutella')
        unique = product._meta.get_field('name').unique
        self.assertTrue(unique)
