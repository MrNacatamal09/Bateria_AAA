from copy import deepcopy

from .operaciones_fila import (
    intercambiar_filas,
    sumar_multiplo_fila
)
from .verificacion_proceso import (
    verificar_intercambio,
    verificar_reemplazo
)


# Buscamos una fila que pueda servir como pivote
def buscar_fila_pivote(matriz, i_inicio, j):

    for i in range(i_inicio, len(matriz)):

        if matriz[i][j] != 0:
            return i

    return None


# Guardamos la matriz después de cada operación
def guardar_paso(historial, operacion, matriz, verificada=None):

    historial.append({
        "operacion": operacion,
        "matriz": deepcopy(matriz),
        "verificada": verificada
    })


# Creamos el texto de una operación entre filas
def crear_texto_operacion(i, i_pivote, factor):

    if factor > 0:
        return (
            f"F{i + 1} -> "
            f"F{i + 1} - ({factor})F{i_pivote + 1}"
        )

    return (
        f"F{i + 1} -> "
        f"F{i + 1} + ({-factor})F{i_pivote + 1}"
    )


# Reducimos la matriz hasta forma escalonada
def gauss(matriz_original):

    # Trabajamos con una copia de la matriz original
    matriz = deepcopy(matriz_original)

    historial = []
    posiciones_pivote = []

    guardar_paso(
        historial,
        "Matriz inicial",
        matriz
    )

    if not matriz:
        return {
            "matriz_escalonada": matriz,
            "historial": historial,
            "posiciones_pivote": posiciones_pivote
        }

    filas = len(matriz)
    columnas = len(matriz[0])

    i_pivote = 0
    j_pivote = 0

    # Avanzamos por la matriz buscando pivotes
    while i_pivote < filas and j_pivote < columnas:

        i_encontrada = buscar_fila_pivote(
            matriz,
            i_pivote,
            j_pivote
        )

        # Si la columna no tiene pivote, avanzamos
        if i_encontrada is None:
            j_pivote += 1
            continue

        # Intercambiamos filas si es necesario
        if i_encontrada != i_pivote:

            matriz_antes = deepcopy(matriz)

            intercambiar_filas(
                matriz,
                i_pivote,
                i_encontrada
            )

            verificada = verificar_intercambio(
                matriz_antes,
                matriz,
                i_pivote,
                i_encontrada
            )

            guardar_paso(
                historial,
                f"F{i_pivote + 1} <-> F{i_encontrada + 1}",
                matriz,
                verificada
            )

        pivote = matriz[i_pivote][j_pivote]

        posiciones_pivote.append(
            (i_pivote, j_pivote)
        )

        # Hacemos cero los valores debajo del pivote
        for i in range(i_pivote + 1, filas):

            valor = matriz[i][j_pivote]

            if valor == 0:
                continue

            factor = valor / pivote
            matriz_antes = deepcopy(matriz)

            sumar_multiplo_fila(
                matriz,
                i,
                i_pivote,
                -factor
            )

            verificada = verificar_reemplazo(
                matriz_antes,
                matriz,
                i,
                i_pivote,
                -factor
            )

            guardar_paso(
                historial,
                crear_texto_operacion(
                    i,
                    i_pivote,
                    factor
                ),
                matriz,
                verificada
            )

        # Avanzamos a la siguiente posición
        i_pivote += 1
        j_pivote += 1

    return {
        "matriz_escalonada": matriz,
        "historial": historial,
        "posiciones_pivote": posiciones_pivote
    }