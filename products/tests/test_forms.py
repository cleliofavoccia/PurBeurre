"""Test forms from products app"""

from django.test import TestCase

from products.forms import SubstituteForm


class SubstituteFormTest(TestCase):
    """Test SubstituteForm (form that send a product
    to find his substitutes)"""

    def test_substitute_form_validity_with_different_datas(self):
        """Test form.is_valid() for different configurations
        of receive datas"""
        form = SubstituteForm(data={'research': 'nutella'})
        self.assertTrue(form.is_valid())

        form = SubstituteForm(data={'research': ''})
        self.assertFalse(form.is_valid())

        form = SubstituteForm(data={'request': 'nutella'})
        self.assertFalse(form.is_valid())
