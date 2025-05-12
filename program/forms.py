from django import forms
from .models import SopaDeLetras
from django.forms import widgets
from django.core.validators import MinValueValidator

class SopaDeLetrasForm(forms.ModelForm):
    tamaño = forms.IntegerField(
        label='Tamaño',
        widget=widgets.NumberInput(attrs={'class': '', 'placeholder': 'Ej: 14', 'min': '14'}),
        validators=[MinValueValidator(14)]
    )
    palabras = forms.CharField(
        label='Palabras',
        widget=widgets.Textarea(attrs={'class': '', 'rows': 3, 'placeholder': 'Ingresa las palabras separadas por comas'})
    )
    class Meta:
        model = SopaDeLetras
        fields = ['tamaño', 'palabras']
