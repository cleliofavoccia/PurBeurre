"""Tests all the views of users app views that are implemented"""

from django.shortcuts import reverse
from django.test import TestCase


class UserDetailViewTest(TestCase):
    """Test UserDetailView (view detailed user profile)"""

    def test_view_uses_correct_template(self):
        """Test UserDetailView use users/user_account.html template"""
        response = self.client.get(reverse('users:user_account'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_account.html')


class SignInTest(TestCase):
    """Test SignIn (view to sign in an user with CreateUserForm)"""

    def test_view_uses_correct_template(self):
        """Test SignIn use users/sign_in.html template"""
        response = self.client.get(reverse('users:sign_in'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/sign_in.html')

    def test_view_return_datas(self):
        """Test SignIn save datas or not from the CreateUserForm"""
        request = {'username': 'testuser1', 'email': 'testuser1@test.fr',
                   'password1': 'sdfuhosd', 'password2': 'sdfuhosd'}
        response = self.client.post(reverse('users:sign_in'), data=request)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('website:index'))

        request = {'username': 'testuser1', 'email': 'testuser1@test.fr'}
        response = self.client.post(reverse('users:sign_in'), data=request)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
