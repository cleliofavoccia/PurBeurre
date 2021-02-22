from django.test import TestCase

from favorites.models import Favorite
from favorites.forms import FavoriteForm

from products.models import Product, Category
from users.models import User


class FavoriteFormTest(TestCase):
    @classmethod
    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
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

        Favorite.objects.create(user=self.test_user1, product=nutella, substitute=muesli)

    def test_favorite_form_work_with_existant_products(self):
        login = self.client.force_login(self.test_user1)
        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')

        form = FavoriteForm(data={
            'csrfmiddlewaretoken':
                ['d25yDUumTlBlHNkj9sHM5IBS5pE9DfaoUbaZcxrsq4xeq2KTyCe4AnD1ucGXokIO'],
            'product': [product.id],
            'substitute': [substitute.id]
        })
        self.assertTrue(form.is_valid())

    def test_favorite_form_doesnt_work_with_unexistant_products(self):
        product = Product.objects.get(name='nutella')
        substitute = 'y'
        form = FavoriteForm(data={
            'csrfmiddlewaretoken':
                ['d25yDUumTlBlHNkj9sHM5IBS5pE9DfaoUbaZcxrsq4xeq2KTyCe4AnD1ucGXokIO'],
            'product': [product.id],
            'substitute': [substitute]
        })
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = 'y'
        form = FavoriteForm(data={
            'csrfmiddlewaretoken':
                ['d25yDUumTlBlHNkj9sHM5IBS5pE9DfaoUbaZcxrsq4xeq2KTyCe4AnD1ucGXokIO'],
            'product': [product],
            'substitute': [substitute]
        })
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        form = FavoriteForm(data={
            'csrfmiddlewaretoken':
                ['d25yDUumTlBlHNkj9sHM5IBS5pE9DfaoUbaZcxrsq4xeq2KTyCe4AnD1ucGXokIO'],
            'product': [product],
            'substitute': [substitute.id]
        })
        self.assertFalse(form.is_valid())

    def test_favorite_form_save_favorite_object(self):
        login = self.client.force_login(self.test_user1)

        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        favorite = Favorite.objects.get(id=1)
        data = {
            'csrfmiddlewaretoken':
                ['d25yDUumTlBlHNkj9sHM5IBS5pE9DfaoUbaZcxrsq4xeq2KTyCe4AnD1ucGXokIO'],
            'product': [product.id],
            'substitute': [substitute.id]
        }
        form = FavoriteForm(data=data)
        request = self.client.post('favorites:add_favorites', data=data)
        self.assertEqual(request, favorite.id)
