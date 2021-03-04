"""Tests all the views of products app views that are implemented"""

from django.shortcuts import reverse
from django.test import TestCase
from django.db.models import Count

from products.models import Product, Category


class ResultsListViewTest(TestCase):
    """Test ResultsListView that print all substitutes
    for a requested product by user"""
    @classmethod
    def setUpTestData(cls):
        """Create objects for test database to
        all test methods"""
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        # Set up non-modified objects used by all test methods
        nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url=(
                'https://static.openfoodfacts.org/images/products/'
                '800/050/021/7078/front_fr.63.400.jpg'
            ),
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )
        lucien_georgelin = Product.objects.create(
            name='pate aux noisettes lucien georgelin',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='a',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url=(
                'https://static.openfoodfacts.org/images/products/'
                '800/050/021/7078/front_fr.63.400.jpg'
            ),
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )
        muesli = Product.objects.create(
            name='muesli',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='e',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url=(
                'https://static.openfoodfacts.org/images/products/'
                '800/050/021/7078/front_fr.63.400.jpg'
            ),
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )
        nutella_bio = Product.objects.create(
            name='nutella bio equitable',
            description='pate a tartiner a la noisette',
            nutriscore='a',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url=(
                'https://static.openfoodfacts.org/images/products/'
                '800/050/021/7078/front_fr.63.400.jpg'
            ),
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )

        nutella.categories.add(pate_a_tartiner, chocolat, noisette)
        lucien_georgelin.categories.add(pate_a_tartiner, chocolat, noisette)
        muesli.categories.add(chocolat, noisette)
        nutella_bio.categories.add(pate_a_tartiner, noisette)

    def test_view_uses_correct_template(self):
        """Test ResultsListView use the correct template"""
        request = {'research': ['nutella']}
        response = self.client.get(reverse('products:results'), data=request)
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/results.html')

    def test_view_return_datas(self):
        """Test ResultsListView return the products list
        that represents substitutes ; products in the same categories
        with a better nutriscore than requested product
        by user"""
        request = {'research': 'nutella'}
        response = self.client.get(reverse('products:results'), data=request)
        products_list = response.context['results']

        # Return all the objects of the categories of
        # the researched product order by nutriscore
        products_list_test = Product.objects.filter(
            nutriscore__lt=Product.objects.get(name='nutella').nutriscore
        ).filter(
            categories__in=Product.objects.get(name='nutella').categories.all()
        ).annotate(
            num_categories_share_with_product=Count('categories')
        ).order_by('num_categories_share_with_product').order_by('nutriscore')

        for products in zip(products_list, products_list_test):
            self.assertEqual(products[0], products[1])

        request2 = {'research': 'qsd'}
        response2 = self.client.get(reverse('products:results'), data=request2)
        error_response = response2.context['base_product']

        self.assertEqual(
            error_response,
            'Oups ! Pas de meilleur produit que celui-ci.'
        )

        # que faire pour champs vide ?


class ProductDetailView(TestCase):
    """Test of ProductDetailView that print all informations about
    one product. It is a product page."""
    @classmethod
    def setUpTestData(cls):
        """Create objects for test database to
        all test methods"""
        pate_a_tartiner = Category.objects.create(name='pate a tartiner')
        chocolat = Category.objects.create(name='chocolat')
        noisette = Category.objects.create(name='noisette')

        # Set up non-modified objects used by all test methods
        nutella = Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            url=(
                'https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero'
            ),
            image_url=(
                'https://static.openfoodfacts.org/images/products/'
                '800/050/021/7078/front_fr.63.400.jpg'
            ),
            nutrition_image_url=(
                'https://static.openfoodfacts.org/images/products'
                '/800/050/021/7078/nutrition_fr.64.400.jpg'
            )
        )
        nutella.categories.add(pate_a_tartiner, chocolat, noisette)

    def test_view_uses_correct_template(self):
        """Test ProductDetailView use the correct template"""
        product = Product.objects.get(name='nutella')
        response = self.client.get(
            reverse(
                'products:product', args=[product.pk]
            )
        )
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
