"""Tests all the views of users app views that are implemented"""

from django.shortcuts import reverse
from django.test import TestCase

from users.models import User


class UserDetailViewTest(TestCase):
    """Test UserDetailView (view detailed user profile)"""

    def setUp(self):
        """Create User for test database to
        test all test methods"""
        self.test_user1 = User.objects.create_user(
            username="testuser", password="PdfjqX458s"
        )
        self.test_user1.save()

    def test_view_uses_correct_template_if_user_connected(self):
        """Test UserDetailView use users/user_account.html template
        if user is connected"""
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('users:user_account'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser')

        self.assertTemplateUsed(response, 'users/user_account.html')

    def test_view_uses_redirect_if_user_not_connected(self):
        """Test UserDetailView use login.html template
        if user is not connected"""
        response = self.client.get(reverse('users:user_account'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/users/my_account/')


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
