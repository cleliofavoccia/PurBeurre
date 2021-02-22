from django.test import TestCase

from favorites.models import Favorite
from products.models import Product
from users.models import User


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        product = Product.objects.create(name='nutella')
        substitute = Product.objects.create(name='pâte de noisette bio')
        user = User.objects.create(username='jean', password='hiuehfkdshk')
        favorite = Favorite.objects.create(user=user, product=product, substitute=substitute)

    def test_favorite_has_product(self):
        favorite = Favorite.objects.get(id=1)
        product = Product.objects.get(id=1)
        favorite_product = Favorite.objects.get(product=product)
        self.assertEqual(favorite, favorite_product)

    def test_favorite_has_substitute(self):
        favorite = Favorite.objects.get(id=1)
        substitute = Product.objects.get(id=2)
        favorite_substitute = Favorite.objects.get(substitute=substitute)
        self.assertEqual(favorite, favorite_substitute)

    def test_favorite_has_user(self):
        favorite = Favorite.objects.get(id=1)
        user = User.objects.get(id=1)
        favorite_user = Favorite.objects.get(user=user)
        self.assertEqual(favorite, favorite_user)

    def test_delete_favorite_not_delete_user_and_products(self):
        favorite = Favorite.objects.get(id=1)
        favorite.delete()
        user = User.objects.get(id=1)
        product = Product.objects.get(id=1)
        substitute = Product.objects.get(id=2)

        self.assertTrue(user)
        self.assertTrue(product)
        self.assertTrue(substitute)

    def test_object_name_is_user_plus_substitute(self):
        favorite = Favorite.objects.get(id=1)
        user = User.objects.get(id=1)
        substitute = Product.objects.get(id=2)
        expected_objet_name = '%s, %s' % (user.username, substitute.name)
        self.assertEqual(expected_objet_name, str(favorite))
