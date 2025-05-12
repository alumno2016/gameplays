from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('login/', views.login, name="login"),
    path('logout/', views.close, name="close"),
    path('menu/', views.menu, name='menu'),
    path('soup/', views.home, name="soup_api"),
]