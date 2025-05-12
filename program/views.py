import random
import string
from django.shortcuts import render
from .forms import SopaDeLetrasForm
from django.contrib.auth.decorators import login_required

import json

@login_required
def generar_sopa(tamaño, palabras):
    # Inicializar la matriz con espacios vacíos
    matriz = [[' ' for _ in range(tamaño)] for _ in range(tamaño)]
    palabras_lista = [p.strip().upper() for p in palabras.split(",")]
    palabras_colocadas = [] # Lista para almacenar las palabras que se lograron colocar

    direcciones = [
        (0, 1),   # Derecha
        (0, -1),  # Izquierda
        (1, 0),   # Abajo
        (-1, 0),  # Arriba
        (1, 1),   # Diagonal abajo-derecha
        (-1, -1), # Diagonal arriba-izquierda
        (1, -1),  # Diagonal abajo-izquierda
        (-1, 1)   # Diagonal arriba-derecha
    ]

    def puede_colocar(palabra, fila, col, df, dc):
        """ Verifica si la palabra cabe sin sobrescribir otras letras. """
        for i in range(len(palabra)):
            nueva_fila = fila + i * df
            nueva_col = col + i * dc
            if not (0 <= nueva_fila < tamaño and 0 <= nueva_col < tamaño and
                    matriz[nueva_fila][nueva_col] in (' ', palabra[i])):
                return False
        return True

    def colocar_palabra(palabra):
        """ Intenta colocar la palabra en la matriz """
        intentos = 0
        while intentos < 100:
            fila = random.randint(0, tamaño - 1)
            col = random.randint(0, tamaño - 1)
            direccion = random.choice(direcciones)
            df, dc = direccion

            if (0 <= fila + df * (len(palabra) - 1) < tamaño and
                    0 <= col + dc * (len(palabra) - 1) < tamaño and
                    puede_colocar(palabra, fila, col, df, dc)):

                # Insertar la palabra en la matriz
                for i in range(len(palabra)):
                    matriz[fila + i * df][col + i * dc] = palabra[i]
                palabras_colocadas.append(palabra)
                return True
            intentos += 1
        return False  # Si después de muchos intentos no se pudo colocar

    # Colocar todas las palabras
    for palabra in palabras_lista:
        if len(palabra) <= tamaño:
            colocado = colocar_palabra(palabra)
            if not colocado:
                print(f"No se pudo colocar la palabra: {palabra}")

    # Rellenar espacios vacíos con letras aleatorias
    for i in range(tamaño):
        for j in range(tamaño):
            if matriz[i][j] == ' ':
                matriz[i][j] = random.choice(string.ascii_uppercase)

    return matriz, palabras_colocadas

@login_required
def sopa_de_letras(request):
    sopa = None
    palabras_encontrables = []
    if request.method == "POST":
        form = SopaDeLetrasForm(request.POST)
        if form.is_valid():
            tamaño = form.cleaned_data['tamaño']
            palabras = form.cleaned_data['palabras']
            sopa, palabras_encontrables = generar_sopa(tamaño, palabras)
            palabras_encontrables = json.dumps(palabras_encontrables)
    else:
        form = SopaDeLetrasForm()

    return render(request, "landing.html", {"form": form, "sopa": sopa, "palabras_encontrables": palabras_encontrables})