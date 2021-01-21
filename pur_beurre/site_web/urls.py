from django.urls import path
from . import views

app_name = 'site_web'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/categories', views.products_by_categories, name='products_by_categories'),
    path('products/<int:id>', views.ProductDetailView.as_view(), name='product'),
    path('my_account/<str:user>', views.user_account, name='user_account'),
    path('myfavorite/', views.FavoritebyUserListView.as_view(), name='favorite'),
    path('legal_mentions/', views.legal_mentions, name='legal_mentions'),
    path('login/', views.login, name='login'),
    path('logged_out/', views.logged_out, name='logged_out')
]



