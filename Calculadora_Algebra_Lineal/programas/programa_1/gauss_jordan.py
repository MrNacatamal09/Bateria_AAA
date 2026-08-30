from copy import deepcopy

from .gauss import gauss
from .operaciones_fila import (
    multiplicar_fila,
    sumar_multiplo_fila
)
from .verificacion_proceso import (
    verificar_escalamiento,
    verificar_reemplazo
)


# Guardamos la matriz después de cada operación
def guardar_paso(historial, operacion, matriz, verificada=None):
    historial.append({
        "operacion": operacion,
        "matriz": deepcopy(matriz),
        "verificada": verificada
    })


# Creamos el texto de una operación de escalamiento
def crear_texto_escalamiento(i, escalar):
    return f"F{i + 1} -> ({escalar})F{i + 1}"


# Creamos el texto de una operación de eliminación
def crear_texto_eliminacion(i, i_pivote, factor):
    i += 1
    i_pivote += 1

    if factor > 0:
        return f"F{i} -> F{i} - ({factor})F{i_pivote}"

    return f"F{i} -> F{i} + ({-factor})F{i_pivote}"


# Reducimos la matriz hasta forma escalonada reducida
def gauss_jordan(matriz_original):

    # Primero obtenemos la forma escalonada con Gauss
    resultado_gauss = gauss(matriz_original)

    matriz = deepcopy(
        resultado_gauss["matriz_escalonada"]
    )

    historial = deepcopy(
        resultado_gauss["historial"]
    )

    posiciones_pivote = resultado_gauss[
        "posiciones_pivote"
    ].copy()

    # Recorremos los pivotes desde abajo hacia arriba
    for i_pivote, j_pivote in reversed(posiciones_pivote):

        pivote = matriz[i_pivote][j_pivote]

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
                crear_texto_escalamiento(
                    i_pivote,
                    escalar
                ),
                matriz,
                verificada
            )

        # Hacemos cero los valores arriba del pivote
        for i in range(i_pivote):

            factor = matriz[i][j_pivote]

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
                crear_texto_eliminacion(
                    i,
                    i_pivote,
                    factor
                ),
                matriz,
                verificada
            )

    return {
        "matriz_reducida": matriz,
        "historial": historial,
        "posiciones_pivote": posiciones_pivote
    }