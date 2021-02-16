from django.urls import path

from . import views

app_name = 'favorites'
urlpatterns = [
    path('myfavorites/', views.FavoriteCreateView.as_view(), name='my_favorites')
    ]