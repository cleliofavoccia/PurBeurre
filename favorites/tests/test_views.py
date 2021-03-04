
from django.test import TestCase
from django.urls import reverse

from products.models import Product, Category
from favorites.models import Favorite
from users.models import User


class FavoriteListViewTest(TestCase):
    """Test Favorite view that print all the favorites of an user"""

    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.test_user1.save()

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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        muesli.categories.add(chocolat, noisette)
        biscotte.categories.add(chocolat, noisette)

        Favorite.objects.create(
            user=User.objects.get(username='testuser1'),
            product=Product.objects.get(name='nutella'),
            substitute=Product.objects.get(
                name='muesli sans sucre ajouté* bio'
            )
        )

        Favorite.objects.create(
            user=User.objects.get(username='testuser1'),
            product=Product.objects.get(name='nutella'),
            substitute=Product.objects.get(name='biscotte equilibrees')
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favorites:my_favorites'))
        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("favorites:my_favorites")}'
        )

    def test_view_url_redirect_at_desired_location(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:my_favorites'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser1')

    def test_view_url_accessible_by_name(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:my_favorites'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser1')

    def test_view_uses_correct_template(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:my_favorites'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser1')

        self.assertTemplateUsed(response, 'favorites/favoritebyuser_list.html')

    def test_view_return_datas(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(
                             reverse('favorites:my_favorites'),
        )
        favorite_by_user_list = response.context['list_favorites']
        for favorites in zip(
                favorite_by_user_list,
                Favorite.objects.filter(user=self.test_user1)
        ):
            self.assertEqual(favorites[0], favorites[1])


class FavoriteCreateViewTest(TestCase):

    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.test_user1.save()

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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
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
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        muesli.categories.add(chocolat, noisette)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favorites:add_favorites'))
        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("favorites:add_favorites")}'
        )

    def test_view_url_accessible_by_name(self):
        self.client.force_login(self.test_user1)
        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')

        response = self.client.post(
            reverse('favorites:add_favorites'),
            data={'product': product.id, 'substitute': substitute.id}
        )

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 302)

    def test_view_verify_datas_with_form(self):
        self.client.force_login(self.test_user1)
        product = Product.objects.get(name='nutella')
        substitute = Product.objects.get(name='muesli sans sucre ajouté* bio')
        true_request = {
            'product': product.id,
            'substitute': substitute.id
                        }
        true_response = self.client.post(
            reverse('favorites:add_favorites'),
            data=true_request
        )

        self.assertRedirects(
            true_response,
            reverse('favorites:well_done')
        )

        false_request = {
            'product': ['1'],
            'substitute': ['Y']
                        }
        false_response = self.client.post(
            reverse('favorites:add_favorites'),
            data=false_request
        )

        self.assertRedirects(
            false_response,
            reverse('favorites:fail')
        )


class WellDoneViewTest(TestCase):

    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favorites:well_done'))
        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("favorites:well_done")}'
        )

    def test_view_url_redirect_at_desired_location(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:well_done'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(
            response.context['msg_welldone'],
            'Produit ajouté à vos favoris !'
        )

    def test_view_url_accessible_by_name(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('favorites:well_done'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 302)


class FailViewTest(TestCase):

    def setUp(self):
        # Create one user
        self.test_user1 = User.objects.create(
            username='testuser1',
            password='1X<ISRUkw+tuK'
        )
        self.test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('favorites:fail'))
        self.assertRedirects(
            response,
            f'{reverse("login")}?next={reverse("favorites:fail")}'
        )

    def test_view_url_redirect_at_desired_location(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:fail'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser1')

    def test_view_url_accessible_by_name(self):
        self.client.force_login(self.test_user1)
        response = self.client.get(reverse('favorites:fail'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check our user is logged in
        self.assertEqual(response.context['user'].username, 'testuser1')
