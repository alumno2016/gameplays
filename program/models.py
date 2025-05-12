from django.db import models

# Create your models here.
class SopaDeLetras(models.Model):
    tamaño = models.PositiveIntegerField()
    palabras = models.TextField(help_text="Lista de palabras separadas por comas")

