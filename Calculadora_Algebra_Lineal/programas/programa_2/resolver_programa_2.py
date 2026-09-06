from copy import deepcopy

from .gauss_jordan import gauss_jordan
from .solucion import obtener_solucion, formatear_solucion

from programas.programa_1.verificacion import (
    verificar_solucion
)


# Revisamos que la matriz tenga la estructura correcta
def validar_matriz(matriz, numero_variables):

    if not matriz:
        raise ValueError(
            "La matriz no puede estar vacía."
        )

    if numero_variables <= 0:
        raise ValueError(
            "Debe existir al menos una variable."
        )

    columnas_esperadas = numero_variables + 1

    for i in range(len(matriz)):

        if len(matriz[i]) != columnas_esperadas:

            raise ValueError(
                f"La fila {i + 1} debe contener "
                f"{columnas_esperadas} valores."
            )


# Resolvemos el Programa 2
def resolver_programa_2(
    matriz_original,
    numero_variables
):

    validar_matriz(
        matriz_original,
        numero_variables
    )

    # Conservamos la matriz original
    matriz_original = deepcopy(
        matriz_original
    )

    # Obtenemos la forma escalonada reducida
    resultado_metodo = gauss_jordan(
        matriz_original,
        numero_variables
    )

    matriz_reducida = resultado_metodo[
        "matriz_reducida"
    ]

    posiciones_pivote = resultado_metodo[
        "posiciones_pivote"
    ]

    # Obtenemos la solución y análisis de pivotes
    solucion = obtener_solucion(
        matriz_reducida,
        posiciones_pivote,
        numero_variables
    )

    analisis = solucion[
        "analisis"
    ]

    solucion_formateada = formatear_solucion(
        solucion,
        numero_variables
    )

    # Reutilizamos la verificación del Programa 1
    verificacion = verificar_solucion(
        matriz_original,
        solucion,
        numero_variables
    )

    return {
        "matriz_original":
            matriz_original,

        "matriz_reducida":
            matriz_reducida,

        "historial":
            resultado_metodo["historial"],

        "posiciones_pivote":
            posiciones_pivote,

        "columnas_pivote":
            analisis["columnas_pivote"],

        "columnas_pivote_matriz":
            analisis["columnas_pivote_matriz"],

        "pivote_columna_aumentada":
            analisis["pivote_columna_aumentada"],

        "variables_basicas":
            analisis["variables_basicas"],

        "variables_libres":
            analisis["variables_libres"],

        "tipo":
            solucion["tipo"],

        "solucion":
            solucion,

        "solucion_formateada":
            solucion_formateada,

        "verificacion":
            verificacion
    }