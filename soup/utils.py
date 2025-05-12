import random

def generar_sopa_de_letras(palabras, filas=14, columnas=14):
    """Genera una sopa de letras con las palabras dadas."""
    grid = [['' for _ in range(columnas)] for _ in range(filas)]
    palabras_colocadas = []
    palabras_colocadas_info = []

    def colocar_palabra(palabra, fila_inicio, columna_inicio, direccion):
        coordenadas = []
        if direccion == "horizontal":
            for i in range(len(palabra)):
                grid[fila_inicio][columna_inicio + i] = palabra[i]
                coordenadas.append({'row': fila_inicio, 'col': columna_inicio + i})
        elif direccion == "vertical":
            for i in range(len(palabra)):
                grid[fila_inicio + i][columna_inicio] = palabra[i]
                coordenadas.append({'row': fila_inicio + i, 'col': columna_inicio})
        palabras_colocadas_info.append({'palabra': palabra, 'coordenadas': coordenadas})

    def puede_colocar(palabra, fila, columna, direccion):
        if direccion == "horizontal":
            if columna + len(palabra) > columnas:
                return False
            for i in range(len(palabra)):
                if grid[fila][columna + i] != '' and grid[fila][columna + i] != palabra[i]:
                    return False
        elif direccion == "vertical":
            if fila + len(palabra) > filas:
                return False
            for i in range(len(palabra)):
                if grid[fila + i][columna] != '' and grid[fila + i][columna] != palabra[i]:
                    return False
        return True

    def colocar_palabra(palabra, fila, columna, direccion):
        if direccion == "horizontal":
            for i in range(len(palabra)):
                grid[fila][columna + i] = palabra[i]
        elif direccion == "vertical":
            for i in range(len(palabra)):
                grid[fila + i][columna] = palabra[i]
        palabras_colocadas.append(palabra)

    # Intenta colocar cada palabra
    for palabra in palabras:
        intentos = 0
        max_intentos = 100  # Para evitar bucles infinitos
        while intentos < max_intentos:
            direccion = random.choice(["horizontal", "vertical"])
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            if puede_colocar(palabra, fila, columna, direccion):
                colocar_palabra(palabra, fila, columna, direccion)
                break
            intentos += 1

    # Rellena los espacios vacíos con letras aleatorias
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(filas):
        for j in range(columnas):
            if grid[i][j] == '':
                grid[i][j] = random.choice(letras)

    return grid, palabras_colocadas, palabras_colocadas_info