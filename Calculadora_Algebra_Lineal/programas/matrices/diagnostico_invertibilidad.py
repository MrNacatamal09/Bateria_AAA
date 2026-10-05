"""
Analiza las condiciones equivalentes de invertibilidad de una matriz cuadrada.
Relaciona determinante, pivotes, independencia lineal y generación de R^n.
Tema de clase: Teorema de la Matriz Invertible.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    calcular_determinante,
    triangularizar_para_determinante
)


def analizar_invertibilidad(matriz):
    """Analiza una matriz cuadrada y devuelve sus condiciones de invertibilidad."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(matriz)

    determinante = calcular_determinante(
        matriz
    )

    reduccion = triangularizar_para_determinante(
        matriz
    )

    num_pivotes = reduccion[
        "num_pivotes"
    ]

    tiene_n_pivotes = (
        num_pivotes == orden
    )

    determinante_no_cero = (
        determinante != 0
    )

    # Para una matriz cuadrada, tener n pivotes equivale a que sus columnas sean L.I.
    columnas_linealmente_independientes = (
        tiene_n_pivotes
    )

    # n columnas L.I. en R^n forman una base y, por tanto, generan R^n.
    columnas_generan_rn = (
        tiene_n_pivotes
    )

    es_invertible = (
        determinante_no_cero
        and tiene_n_pivotes
    )

    return {
        "matriz": matriz,
        "orden": orden,
        "determinante": determinante,
        "num_pivotes": num_pivotes,
        "determinante_no_cero": determinante_no_cero,
        "tiene_n_pivotes": tiene_n_pivotes,
        "columnas_linealmente_independientes":
            columnas_linealmente_independientes,
        "columnas_generan_rn":
            columnas_generan_rn,
        "es_invertible": es_invertible,
        "matriz_triangular":
            reduccion["matriz_triangular"],
        "historial":
            reduccion["historial"]
    }


def construir_diagnostico(resultado):
    """Devuelve el diagnóstico textual según las condiciones obtenidas."""
    if resultado["es_invertible"]:
        return (
            "La matriz es invertible: det(A) ≠ 0, "
            "tiene n posiciones pivote, sus columnas "
            "son L.I. y generan ℝⁿ."
        )

    return (
        "La matriz es singular (no tiene inversa): "
        "det(A) = 0."
    )