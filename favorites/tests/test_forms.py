from django.test import TestCase

from favorites.models import Favorite
from favorites.forms import FavoriteForm

from products.models import Product


class FavoriteFormTest(TestCase):

    def setUpTestData(cls):
        Product.objects.create(name='nutella')
        Product.objects.create(name='pâte de noisette bio')

    def test_favorite_form_work_with_existant_products(self):
        product = Product.objects.get(id=1)
        substitute = Product.objects.get(id=2)

        form = FavoriteForm(data={'product': product, 'substitute': substitute})
        self.assertTrue(form.is_valid())

    def test_favorite_form_doesnt_work_with_unexistant_products(self):
        product = Product.objects.get(id=1)
        substitute = 'y'
        form = FavoriteForm(data={'product': product, 'substitute': substitute})
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = 'y'
        form = FavoriteForm(data={'product': product, 'substitute': substitute})
        self.assertFalse(form.is_valid())

        product = 'x'
        substitute = Product.objects.get(id=2)
        form = FavoriteForm(data={'product': product, 'substitute': substitute})
        self.assertFalse(form.is_valid())

    def test_favorite_form_save_favorite_object(self):
        product = Product.objects.get(id=1)
        substitute = Product.objects.get(id=2)
        form = FavoriteForm(data={'product': product, 'substitute': substitute})
        self.assertTrue(Favorite.objects.get(id=1))
