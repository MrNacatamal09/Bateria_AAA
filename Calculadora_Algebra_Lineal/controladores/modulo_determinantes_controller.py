from utilidades.estructuras_entrada import (
    convertir_matriz
)

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    obtener_menor,
    calcular_cofactor,
    calcular_determinante,
    es_matriz_invertible
)

from programas.determinantes.procedimiento_determinante import (
    calcular_determinante_con_procedimiento
)


# ==========================================================
# MÓDULO 4
# CONTROLADOR DE DETERMINANTES
# ==========================================================


# ==========================================================
# CALCULAR DETERMINANTE
# ==========================================================

def procesar_determinante(
    matriz
):

    matriz = convertir_matriz(
        matriz
    )

    validar_matriz_cuadrada(
        matriz
    )

    determinante = calcular_determinante(
        matriz
    )

    return {
        "operacion":
            "determinante",

        "matriz":
            matriz,

        "orden":
            len(matriz),

        "determinante":
            determinante
    }


# ==========================================================
# MENOR Y COFACTOR
#
# La interfaz trabajará con filas y columnas
# comenzando desde 1.
#
# Internamente Python trabaja desde 0.
# ==========================================================

def procesar_menor_cofactor(
    matriz,
    fila,
    columna
):

    matriz = convertir_matriz(
        matriz
    )

    validar_matriz_cuadrada(
        matriz
    )

    try:

        fila = int(
            fila
        )

        columna = int(
            columna
        )

    except ValueError:

        raise ValueError(
            "La fila y la columna deben ser "
            "números enteros."
        )

    orden = len(
        matriz
    )

    if (
        fila < 1
        or fila > orden
    ):

        raise ValueError(
            "La fila indicada no existe "
            "en la matriz."
        )

    if (
        columna < 1
        or columna > orden
    ):

        raise ValueError(
            "La columna indicada no existe "
            "en la matriz."
        )

    # Convertimos de posición matemática
    # a índice de Python.
    fila_indice = (
        fila - 1
    )

    columna_indice = (
        columna - 1
    )

    menor = obtener_menor(
        matriz,
        fila_indice,
        columna_indice
    )

    determinante_menor = None

    # Para una matriz 1 x 1 el menor queda vacío.
    if orden > 1:

        determinante_menor = (
            calcular_determinante(
                menor
            )
        )

    cofactor = calcular_cofactor(
        matriz,
        fila_indice,
        columna_indice
    )

    return {
        "operacion":
            "menor_cofactor",

        "matriz":
            matriz,

        "orden":
            orden,

        "fila":
            fila,

        "columna":
            columna,

        "fila_indice":
            fila_indice,

        "columna_indice":
            columna_indice,

        "menor":
            menor,

        "determinante_menor":
            determinante_menor,

        "cofactor":
            cofactor
    }


# ==========================================================
# DESARROLLO POR COFACTORES
# ==========================================================

def procesar_desarrollo_cofactores(
    matriz
):

    matriz = convertir_matriz(
        matriz
    )

    validar_matriz_cuadrada(
        matriz
    )

    resultado = (
        calcular_determinante_con_procedimiento(
            matriz
        )
    )

    return {
        "operacion":
            "desarrollo_cofactores",

        "resultado":
            resultado
    }


# ==========================================================
# ANALIZAR INVERTIBILIDAD
# ==========================================================

def procesar_invertibilidad(
    matriz
):

    matriz = convertir_matriz(
        matriz
    )

    validar_matriz_cuadrada(
        matriz
    )

    determinante = calcular_determinante(
        matriz
    )

    invertible = es_matriz_invertible(
        matriz
    )

    if invertible:

        mensaje = (
            "La matriz es invertible porque "
            "su determinante es diferente de cero."
        )

    else:

        mensaje = (
            "La matriz no es invertible porque "
            "su determinante es igual a cero."
        )

    return {
        "operacion":
            "invertibilidad",

        "matriz":
            matriz,

        "orden":
            len(matriz),

        "determinante":
            determinante,

        "es_invertible":
            invertible,

        "mensaje":
            mensaje
    }