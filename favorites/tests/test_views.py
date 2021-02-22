
from django.test import TestCase
from django.urls import reverse

from products.models import Product, Category
from favorites.models import Favorite
from users.models import User


class FavoriteListViewTest(TestCase):
    """Test Favorite view that print all the favorites of an user"""

    def setUp(self):
        # Create one user
        test_user1 = User.objects.create(username='testuser1', password='1X<ISRUkw+tuK')
        test_user1.save()

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

        biscotte = Product.objects.create(
            name='biscotte equilibrees',
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
        biscotte.categories.add(chocolat, noisette)

        Favorite.objects.create(
            user=User.objects.get(username='testuser1'),
            product=Product.objects.get(name='nutella'),
            substitute=Product.objects.get(name='muesli sans sucre ajouté* bio')
        )

        Favorite.objects.create(
            user=User.objects.get(username='testuser1'),
            product=Product.objects.get(name='nutella'),
            substitute=Product.objects.get(name='biscotte equilibrees')
        )

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

    def test_view_return_datas(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.post(
                             reverse('my_favorites'),
                             kwargs='testuser1'
        )
        favorite_by_user_list = response.context['results']

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')

        self.assertEqual(favorite_by_user_list, Favorite.objects.all())


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
            'product': ['1'],
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
