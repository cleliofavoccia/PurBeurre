from django.test import TestCase

from favorites.models import Favorite
from products.models import Product, Category
from users.models import User


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )

        muesli = Product.objects.create(
            name='muesli sans sucre ajouté* bio',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        muesli.categories.add(chocolat, noisette)

        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

        favorite = Favorite.objects.create(user=test_user1, product=nutella, substitute=muesli)

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
