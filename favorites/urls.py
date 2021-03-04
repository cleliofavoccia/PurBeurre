"""URL of favorites app"""
from django.urls import path

from . import views

app_name = 'favorites'
urlpatterns = [
    path(
        'addfavorites/',
        views.FavoriteCreateView.as_view(),
        name='add_favorites'
    ),
    path('welldone/', views.WellDoneView.as_view(), name='well_done'),
    path('fail/', views.FailView.as_view(), name='fail'),
    path('myfavorites/', views.FavoriteListView.as_view(), name='my_favorites')
    ]
