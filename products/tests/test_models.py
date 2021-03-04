"""Test Products and Categories objects are conform"""
from django.test import TestCase

from products.models import Product, Category


class ProductModelTest(TestCase):
    """Class to test Products objects are conform"""
    @classmethod
    def setUpTestData(cls):
        """Create objects for database test of Django
        to test different things on Products objects"""
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        # Set up non-modified objects used by all test methods
        nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='e',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg')
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)

    def test_name_label(self):
        """Test name label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'product name')

    def test_description_label(self):
        """Test description label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'product description')

    def test_nutriscore_label(self):
        """Test nutriscore label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('nutriscore').verbose_name
        self.assertEqual(field_label, 'product nutriscore')

    def test_categories_label(self):
        """Test categories label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('categories').verbose_name
        self.assertEqual(field_label, 'categories')

    def test_url_label(self):
        """Test url label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('url').verbose_name
        self.assertEqual(field_label, 'product url')

    def test_image_url_label(self):
        """Test image label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = product._meta.get_field('image_url').verbose_name
        self.assertEqual(field_label, 'product image url')

    def test_nutrition_image_url_label(self):
        """Test nutrition label is what it expected"""
        product = Product.objects.get(name='nutella')
        field_label = (
            product._meta.get_field('nutrition_image_url')
            .verbose_name
        )
        self.assertEqual(field_label, 'product nutrition image url')

    def test_name_max_length(self):
        """Test name max length is what it expected"""
        product = Product.objects.get(name='nutella')
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_nutriscore_max_length(self):
        """Test nutriscore max length is what it expected"""
        product = Product.objects.get(name='nutella')
        max_length = product._meta.get_field('nutriscore').max_length
        self.assertEqual(max_length, 1)

    def test_object_name_is_name(self):
        """Test name is what it expected"""
        product = Product.objects.get(name='nutella')
        expected_object_name = product.name
        self.assertEqual(expected_object_name, str(product))


class CategoryModelTest(TestCase):
    """Class to test Category objects are conform"""
    @classmethod
    def setUpTestData(cls):
        """Create objects for database test of Django
        to test different things on Products objects"""
        Category.objects.create(name='pate a tartiner')

    def test_object_name_is_category_name(self):
        """Test name is what it expected"""
        category = Category.objects.get(name='pate a tartiner')
        expected_objet_name = category.name
        self.assertEqual(expected_objet_name, str(category))

    def test_name_max_length(self):
        """Test name max length is what it expected"""
        category = Category.objects.get(name='pate a tartiner')
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_name_is_unique(self):
        """Test name is unique, ie it's impossible
        to have two 'Sodas' categories"""
        category = Category.objects.get(name='pate a tartiner')
        unique = category._meta.get_field('name').unique
        self.assertTrue(unique)

    def test_categories_related_name(self):
        """Test related name is what it expected"""
        category = Category.objects.get(name='pate a tartiner')
        related_name = category._meta.get_field('products').related_name
        self.assertEqual(related_name, 'products')
