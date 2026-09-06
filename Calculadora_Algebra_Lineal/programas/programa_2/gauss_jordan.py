from copy import deepcopy

from programas.programa_1.operaciones_fila import (
    intercambiar_filas,
    multiplicar_fila,
    sumar_multiplo_fila
)
from programas.programa_1.verificacion_proceso import (
    verificar_intercambio,
    verificar_escalamiento,
    verificar_reemplazo
)


# Buscamos una fila que pueda servir como pivote
def buscar_fila_pivote(matriz, i_inicio, j):

    for i in range(i_inicio, len(matriz)):

        if matriz[i][j] != 0:
            return i

    return None


# Guardamos cada operación realizada
def guardar_paso(historial, operacion, matriz, verificada=None):

    historial.append({
        "operacion": operacion,
        "matriz": deepcopy(matriz),
        "verificada": verificada
    })


# Creamos el texto de una operación de reemplazo
def crear_texto_reemplazo(i, i_pivote, factor):

    if factor > 0:
        return (
            f"F{i + 1} -> "
            f"F{i + 1} - ({factor})F{i_pivote + 1}"
        )

    return (
        f"F{i + 1} -> "
        f"F{i + 1} + ({-factor})F{i_pivote + 1}"
    )


# Reducimos la matriz aumentada hasta RREF
def gauss_jordan(matriz_original, numero_variables):

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
            "matriz_reducida": matriz,
            "historial": historial,
            "posiciones_pivote": posiciones_pivote
        }

    filas = len(matriz)
    columnas = numero_variables + 1

    i_pivote = 0

    # Recorremos toda la matriz aumentada
    for j in range(columnas):

        if i_pivote >= filas:
            break

        i_encontrada = buscar_fila_pivote(
            matriz,
            i_pivote,
            j
        )

        if i_encontrada is None:
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

        pivote = matriz[i_pivote][j]

        # Convertimos el pivote en 1
        if pivote != 1:

            escalar = 1 / pivote
            matriz_antes = deepcopy(matriz)

            multiplicar_fila(
                matriz,
                i_pivote,
                escalar
            )

            verificada = verificar_escalamiento(
                matriz_antes,
                matriz,
                i_pivote,
                escalar
            )

            guardar_paso(
                historial,
                f"F{i_pivote + 1} -> "
                f"({escalar})F{i_pivote + 1}",
                matriz,
                verificada
            )

        # Hacemos ceros arriba y debajo del pivote
        for i in range(filas):

            if i == i_pivote:
                continue

            factor = matriz[i][j]

            if factor == 0:
                continue

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
                crear_texto_reemplazo(
                    i,
                    i_pivote,
                    factor
                ),
                matriz,
                verificada
            )

        posiciones_pivote.append(
            (i_pivote, j)
        )

        i_pivote += 1

    return {
        "matriz_reducida": matriz,
        "historial": historial,
        "posiciones_pivote": posiciones_pivote
    }