from django.test import TestCase

from favorites.models import Favorite
from products.models import Product, Category
from users.models import User


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(name='nutella')
        substitute = Product.objects.create(name='pâte de noisette bio')
        user = User.objects.create(username='jean', password='hiuehfkdshk')
        favorite = Favorite.objects.create(user=user, product=product, substitute=substitute)

    def test_object_name_is_product_name(self):
        product = Product.objects.get(id=1)
        expected_objet_name = product.name
        self.assertEqual(expected_objet_name, str(product))


class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='pate a tartiner')
        product = Product.objects.create(name='nutella')
        substitute = Product.objects.create(name='pâte de noisette bio')
        user = User.objects.create(username='jean', password='hiuehfkdshk')
        favorite = Favorite.objects.create(user=user, product=product, substitute=substitute)

    def test_object_name_is_product_name(self):
        category = Category.objects.get(id=1)
        expected_objet_name = category.name
        self.assertEqual(expected_objet_name, str(category))
