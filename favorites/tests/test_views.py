from django.test import TestCase
from django.urls import reverse

from users.models import User


class FavoriteListViewTest(TestCase):
    """Test Favorite view that print all the favorites of an user"""

    def setUp(self):
        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('my_favorites'))
        self.assertRedirects(response, 'users/login/?next=/favorites/myfavorites/')

    def test_view_url_redirect_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/favorites/myfavorites/')

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my_favorites'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('my_favorites'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'favorites/favoritebyuser_list.html')

    #Tester que si la liste est vide, cela renvoi "vous n'avez pas de substituts"
    # ce qui est fait actuellement dans le html?


class FavoriteCreateViewTest(TestCase):

    def setUp(self):
        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_favorites'))
        self.assertRedirects(response, 'users/login/?next=/favorites/addfavorites/')

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('add_favorites'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_verify_datas_with_form(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')

        true_request = {
            'csrfmiddlewaretoken':
            ['ZP1J9xryqNyYWMUCKigTsb2g8PeLxZgjuS0y0NYUquChRUx6OhtWgDycSdv1XTwe'],
            'product': ['1'],
            'substitute': ['2']
                        }
        true_response = self.client.post(reverse('add_favorites'), kwargs=true_request)

        # Check our user is logged in
        self.assertEqual(str(true_response.context['user']), 'testuser1')

        self.assertRedirects(true_response, '/favorites/welldone/')

        false_request = {
            'csrfmiddlewaretoken':
            ['ZP1J9xryqNyYWMUCKigTsb2g8PeLxZgjuS0y0NYUquChRUx6OhtWgDycSdv1XTwe'],
            'product': ['X'],
            'substitute': ['Y']
                        }
        false_response = self.client.post(reverse('add_favorites'), kwargs=false_request)

        # Check our user is logged in
        self.assertEqual(str(false_response.context['user']), 'testuser1')

        self.assertRedirects(false_response, '/favorites/fail/')


class WellDoneViewTest(TestCase):

    def setUp(self):
        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('well_done'))
        self.assertRedirects(response, 'users/login/?next=/favorites/welldone/')

    def test_view_url_redirect_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/favorites/welldone/')

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('well_done'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)


class FailViewTest(TestCase):

    def setUp(self):
        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('fail'))
        self.assertRedirects(response, 'users/login/?next=/favorites/fail/')

    def test_view_url_redirect_at_desired_location(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/favorites/fail/')

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('fail'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
