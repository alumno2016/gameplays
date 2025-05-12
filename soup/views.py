from django.shortcuts import render
from .utils import generar_sopa_de_letras
from django.contrib.auth.decorators import login_required

@login_required
def sopa_de_letras_view(request):
    palabras_para_sopa = [
        "MANATI", 
        "PERRO", 
        "GATO", 
        "CONEJO", 
        "TIBURON",
        "ELEFANTE",
        "ALCON",
        "SERPIENTE",
        "JAGUAR",
        "CANGURO",
        "LOBO",
        "MONO",
        "NUTRIA",
        "LEON",
        "LORO",
        "TORO",
        "ORUGA"
        ]
    sopa, palabras_colocadas, palabras_colocadas_info = generar_sopa_de_letras(palabras_para_sopa)
    context = {
        'sopa': sopa,
        'palabras': palabras_colocadas,
        'palabras_info': palabras_colocadas_info,
    }
    return render(request, 'index.html', context)