"""Urls of user app, all urls that concern user
(authentification and others things)"""

from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('my_account/', views.UserDetailView.as_view(), name='user_account'),
    path('sign_in/', views.SignIn.as_view(), name='sign_in')
]
