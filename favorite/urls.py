from django.urls import path

from . import views

app_name = 'favorite'
urlpatterns = [
    path('myfavorites/', views.FavoritebyUserListView.as_view(), name='favorite')
    ]