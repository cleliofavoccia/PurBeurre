"""Views of products app, all views that concern products"""

from django.views import generic
from django.db.models import Count

from .models import Product


class ResultsListView(generic.ListView):
    """Generic class-based view listing all products by nutriscore"""
    model = Product
    template_name = 'products/results.html'

    def get_context_data(self, **kwargs):
        """Methods that return an enriched context to use for the view"""
        search_product = self.request.GET.get('research')
        context = super().get_context_data(**kwargs)

        list_product = Product.objects.filter(name__icontains=search_product)

        if not list_product:
            context['base_product'] = (
                'Oups ! Pas de meilleur produit que celui-ci.'
            )
        else:
            product = list_product[0]
            context['base_product'] = product

            # Take the categories of the researched product
            product_categories = product.categories.all()

            products = Product.objects.filter(
                nutriscore__lt=product.nutriscore
            )

            # Return all the objects of the categories of
            # the researched product order by nutriscore
            context['results'] = (
                products.filter(
                    categories__in=product_categories
                )
                .annotate(
                    num_categories_share_with_product=Count('categories')
                )
                .order_by('num_categories_share_with_product')
                .order_by('nutriscore')
                [:6]
            )
            return context

        return context


class ProductDetailView(generic.DetailView):
    """Generic class-based view detailed all products"""
    model = Product
