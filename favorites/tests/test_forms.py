from django.test import TestCase

from favorites.models import Favorite
from favorites.forms import FavoriteForm

from products.models import Product, Category
from users.models import User


class FavoriteFormTest(TestCase):
    @classmethod
    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.test_user1.save()

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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        muesli.categories.add(chocolat, noisette)

        Favorite.objects.create(
            user=self.test_user1,
            product=nutella,
            substitute=muesli)

        self.cleaned_data = {
            'product': None,
            'substitute': None
        }

    def test_favorite_form_work_with_existant_products(self):
        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')

        form = FavoriteForm(data={
            'product': product.id,
            'substitute': substitute.id
        })
        self.assertTrue(form.is_valid())

    def test_favorite_form_doesnt_work_with_unexistant_products(self):
        product = Product.objects.get(name='nutella')
        substitute = 'y'
        form = FavoriteForm(data={
            'product': product.id,
            'substitute': substitute
        })
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = 'y'
        form = FavoriteForm(data={
            'product': product,
            'substitute': substitute
        })
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        form = FavoriteForm(data={
            'product': product,
            'substitute': substitute.id
        })
        self.assertFalse(form.is_valid())

    def test_favorite_form_save_favorite_object(self):
        self.client.force_login(self.test_user1)

        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        data = {
            'product': product.id,
            'substitute': substitute.id
        }
        form = FavoriteForm(data=data)
        form.is_valid()
        favorite = form.save(self.test_user1)
        self.assertEqual(favorite, Favorite.objects.get(id=favorite.id))

    def test_clean_product(self):
        product = Product.objects.get(name='nutella')
        self.cleaned_data['product'] = product.id
        self.assertEqual(product, FavoriteForm.clean_product(self))

    def test_clean_substitute(self):
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        self.cleaned_data['substitute'] = substitute.id
        self.assertEqual(substitute, FavoriteForm.clean_substitute(self))
