from django.test import TestCase
from django.urls import reverse


class FavoriteCreateViewTest(TestCase):

    def test_view_url_redirect_at_desired_location_in_valide_case(self):
        response = self.client.get('/favorites/welldone/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_redirect_at_desired_location_in_invalide_case(self):
        response = self.client.get('/favorites/fail/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('add_favorites'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_favorites'))
        self.assertRedirects(response, 'users/login/?next=/favorites/addfavorites/')

