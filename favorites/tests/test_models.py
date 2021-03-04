from django.test import TestCase

from favorites.models import Favorite
from products.models import Product, Category
from users.models import User


class FavoriteModelTest(TestCase):
    @classmethod
    def setUp(cls):
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        cls.nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        cls.muesli = Product.objects.create(
            name='muesli sans sucre ajouté* bio',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        cls.nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        cls.muesli.categories.add(chocolat, noisette)

        # Create one user
        cls.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        cls.test_user1.save()

        cls.favorite = Favorite.objects.create(
            user=cls.test_user1,
            product=cls.nutella,
            substitute=cls.muesli
        )

    def test_favorite_has_product(self):
        favorite_product = Favorite.objects.get(
            product=Product.objects.get(
                name='nutella'
            )
        )
        self.assertEqual(self.favorite, favorite_product)

    def test_favorite_has_substitute(self):
        favorite_substitute = Favorite.objects.get(substitute=self.muesli)
        self.assertEqual(self.favorite, favorite_substitute)

    def test_favorite_has_user(self):
        favorite_user = Favorite.objects.get(user=self.test_user1)
        self.assertEqual(self.favorite, favorite_user)

    def test_delete_favorite_not_delete_user_and_products(self):
        favorite = self.favorite
        favorite.delete()
        user = self.test_user1
        product = self.nutella
        substitute = self.muesli

        self.assertTrue(user)
        self.assertTrue(product)
        self.assertTrue(substitute)

    def test_object_name_is_user_plus_substitute(self):
        favorite = self.favorite
        user = self.test_user1
        substitute = self.muesli
        expected_objet_name = '%s, %s' % (user.username, substitute.name)
        self.assertEqual(expected_objet_name, str(favorite))
