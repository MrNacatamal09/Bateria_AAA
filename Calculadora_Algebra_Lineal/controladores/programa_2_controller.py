from utilidades.matriz_entrada import construir_matriz_aumentada

from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)


# Preparamos los datos y ejecutamos el Programa 2
def procesar_programa_2(
    datos,
    numero_ecuaciones,
    numero_variables
):

    # Convertimos los datos en una matriz aumentada
    matriz = construir_matriz_aumentada(
        datos,
        numero_ecuaciones,
        numero_variables
    )

    # Aplicamos Gauss-Jordan y analizamos los pivotes
    resultado = resolver_programa_2(
        matriz,
        numero_variables
    )

    return resultado