from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('my_account/<str:users>/', views.user_account, name='user_account'),
    path('sign_in/', views.SignIn.as_view(), name='sign_in')
]