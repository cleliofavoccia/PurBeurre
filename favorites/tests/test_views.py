from django.test import TestCase
from django.urls import reverse

from favorites.models import Favorite
from products.models import Product
from users.models import User


class FavoriteCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        for element in range(3):
            product = Product.objects.create(
                name='nutella' + str(element),
            )
            substitute = Product.objects.create(
                name='pâte de noisette bio' + str(element),
            )
            user = User.objects.create(
                username='jean' + str(element),
                password='hiuehfkdshk' + str(element)
            )
            Favorite.objects.create(
                product=product,
                substitute=substitute,
                user=user
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/favorites/myfavorites/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('my_favorites'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('my_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/favoritebyuser_list.html')

    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('authors')+'?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['author_list']) == 3)