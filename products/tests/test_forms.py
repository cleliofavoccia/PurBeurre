from django.test import TestCase
from django.shortcuts import reverse

from products.forms import SubstituteForm

from products.models import Product, Category


class FavoriteFormTest(TestCase):

    def test_substitute_form_is_valid_with_different_datas(self):
        form = SubstituteForm(data={'research': 'nutella'})
        self.assertTrue(form.is_valid())
