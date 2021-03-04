"""Test forms of users app"""

from django.test import TestCase

from users.forms import CreateUserForm


class CreateUserFormTest(TestCase):
    """Test CreateUserForm
    (sign in forms to permit the users to register him)"""

    def test_substitute_form_validity_with_different_datas(self):
        """Test form.is_valid() for different configurations
        of receive datas"""
        request = {'username': 'testuser1', 'email': 'testuser1@test.fr',
                   'password1': 'sdfuhosd', 'password2': 'sdfuhosd'}

        form = CreateUserForm(data=request)
        self.assertTrue(form.is_valid())

        form = CreateUserForm(data={'username': 'testuser1',
                                    'password1': 'sdfuhosd',
                                    'password2': 'sdfuhosd'})
        self.assertTrue(form.is_valid())

        form = CreateUserForm(data={'username': 'testuser1',
                                    'password1': 'sdfuhosd'})
        self.assertFalse(form.is_valid())

        form = CreateUserForm(data={'username': 'testuser1',
                                    'email': 'testuser1@test.fr'})
        self.assertFalse(form.is_valid())

        form = CreateUserForm(data={'email': 'testuser1@test.fr',
                                    'password1': 'sdfuhosd',
                                    'password2': 'sdfuhosd'})
        self.assertFalse(form.is_valid())
