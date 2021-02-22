
from django.shortcuts import reverse
from django.test import TestCase
from django.db.models import Count

from products.models import Product


class ResultsListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(
            name='nutella',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='d',
            categories='pate a tartiner, chocolat, noisette',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )
        Product.objects.create(
            name='pate aux noisettes lucien georgelin',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='a',
            categories='pate a tartiner, chocolat, noisette',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )
        Product.objects.create(
            name='nutella chocolat plus',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='e',
            categories='pate a tartiner, chocolat, noisette',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )
        Product.objects.create(
            name='nutella bio equitable',
            description='pate a tartiner au chocolat'
                        'et a la noisette',
            nutriscore='a',
            categories='pate a tartiner, chocolat, noisette',
            url='https://fr.openfoodfacts.org/produit/8000500217078/'
                'nutella-b-ready-biscuits-220g-paquet-de-10-pieces-ferrero',
            image_url='https://static.openfoodfacts.org/images/products/'
                      '800/050/021/7078/front_fr.63.400.jpg',
            nutrition_image_url='https://static.openfoodfacts.org/images/products'
                                '/800/050/021/7078/nutrition_fr.64.400.jpg'
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('results'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/results.html')

    def test_view_research_with_datas(self):
        request = {'research': ['nutella']}
        response = self.client.get(reverse('results'), kwargs=request)

        self.assertEqual(response, '/products/results/?research=nutella')

        request = {'research': ['']}
        response = self.client.get(reverse('results'), kwargs=request)

        self.assertEqual(response, '/products/results/?research=')

    def test_view_return_datas(self):
        request = {'research': ['nutella']}
        response = self.client.post(reverse('results'), kwargs=request)
        products_list = response.context['results']

        # Return all the objects of the categories of the researched product order by nutriscore
        products_list_test = Product.objects.filter(
            nutriscore__lt=Product.objects.get(name='nutella').nutriscore
        ).filter(
            categories__in=Product.objects.get(name='nutella').categories.all()
        ).annotate(
            num_categories_share_with_product=Count('categories')
        ).order_by('num_categories_share_with_product').order_by('nutriscore')

        self.assertEqual(products_list, products_list_test)

        request = {'research': ['']}
        response = self.client.post(reverse('results'), kwargs=request)
        error_response = response.context['base_product']

        self.assertEqual(error_response, 'Oups ! Pas de meilleur produit que celui-ci.')


