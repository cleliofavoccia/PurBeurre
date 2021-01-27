from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('my_account/<str:user>/', views.user_account, name='user_account'),
    path('login/', views.login, name='login'),
    path('logged_out/', views.logged_out, name='logged_out')
]