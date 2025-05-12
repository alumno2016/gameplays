from django.urls import path
from . import views

urlpatterns = [
    path('list', views.sopa_de_letras, name="soup_bootstrap"),
]
