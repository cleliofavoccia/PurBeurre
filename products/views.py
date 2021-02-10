from django.views import generic
from django.db.models import Count
from django.shortcuts import get_object_or_404

from .models import Category, Product


class ProductListView(generic.ListView):
    """Generic class-based view listing all products"""
    model = Product


class ProductsByCategoryListView(generic.ListView):
    """Generic class-based view listing all products by Category"""
    model = Product


class ProductDetailView(generic.DetailView):
    """Generic class-based view detailed all products"""
    model = Product


class ResultsListView(generic.ListView):
    """Generic class-based view listing all products by nutriscore"""
    model = Product
    paginate_by = 6

    def get_queryset(self):
        self.request = get_object_or_404(Product, name=self.kwargs['product'])
        print(self.kwargs['product'])
        return Product.objects.filter(request=self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        product = Product.objects.filter(name__contains=self.request)[0]
        # product = self.request
        context['base_product'] = product

        # Take the categories of the researched product
        product_categories = product.categories.all()

        products = Product.objects.filter(nutriscore__lt=product.nutriscore)

        # Return all the objects of the categories of the researched product order by nutriscore
        context['results'] = (
            products.filter(categories__in=product_categories)
            .order_by('nutriscore')
            .annotate(num_product_same_category=Count('product'))
        )

        return context


