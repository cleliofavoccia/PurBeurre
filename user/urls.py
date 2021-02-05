from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('my_account/<str:user>/', views.user_account, name='user_account'),
    path('sign_in/', views.sign_in, name='sign_in')
]