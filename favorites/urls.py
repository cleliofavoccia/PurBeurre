from django.urls import path

from . import views

app_name = 'favorites'
urlpatterns = [
    path('myfavorites/', views.FavoritebyUserListView.as_view(), name='my_favorites')
    ]