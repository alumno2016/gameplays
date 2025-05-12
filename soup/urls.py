from django.urls import path
from . import views

urlpatterns = [
    path('find', views.sopa_de_letras_view, name='soup_tailwind'),
]