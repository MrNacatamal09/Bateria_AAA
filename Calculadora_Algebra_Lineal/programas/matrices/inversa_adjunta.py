"""
Implementa la inversa de una matriz mediante la matriz adjunta.
Construye la matriz de cofactores, obtiene adj(A) y calcula A^-1.
Tema de clase: determinantes, matriz adjunta e inversa.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    calcular_determinante,
    calcular_cofactor
)

from programas.programa_3.matrices import (
    transponer_matriz,
    multiplicar_matriz_escalar
)

from programas.matrices.inversa import (
    calcular_inversa,
    verificar_inversa
)


def construir_matriz_cofactores(matriz):
    """Construye y devuelve la matriz completa de cofactores de A."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(matriz)
    matriz_cofactores = []

    for fila in range(orden):
        nueva_fila = []

        for columna in range(orden):
            nueva_fila.append(
                calcular_cofactor(
                    matriz,
                    fila,
                    columna
                )
            )

        matriz_cofactores.append(
            nueva_fila
        )

    return matriz_cofactores


def calcular_adjunta(matriz):
    """Devuelve adj(A), obtenida al transponer la matriz de cofactores."""
    matriz_cofactores = construir_matriz_cofactores(
        matriz
    )

    return transponer_matriz(
        matriz_cofactores
    )


def calcular_inversa_adjunta(matriz):
    """Calcula A^-1 = (1/det(A)) adj(A) y devuelve el procedimiento."""
    validar_matriz_cuadrada(
        matriz
    )

    determinante = calcular_determinante(
        matriz
    )

    if determinante == 0:
        return {
            "matriz_original": matriz,
            "determinante": determinante,
            "es_invertible": False,
            "matriz_cofactores": None,
            "adjunta": None,
            "factor": None,
            "inversa": None,
            "verificacion": None,
            "mensaje": (
                "La matriz es singular porque det(A) = 0. "
                "No existe matriz inversa."
            )
        }

    matriz_cofactores = construir_matriz_cofactores(
        matriz
    )

    adjunta = transponer_matriz(
        matriz_cofactores
    )

    factor = (
        Fraction(1)
        / determinante
    )

    inversa = multiplicar_matriz_escalar(
        adjunta,
        factor
    )

    verificacion = verificar_inversa(
        matriz,
        inversa
    )

    return {
        "matriz_original": matriz,
        "determinante": determinante,
        "es_invertible": True,
        "matriz_cofactores": matriz_cofactores,
        "adjunta": adjunta,
        "factor": factor,
        "inversa": inversa,
        "verificacion": verificacion,
        "mensaje": (
            "La matriz inversa fue obtenida mediante "
            "la matriz adjunta."
        )
    }


def comparar_metodos_inversa(matriz):
    """Compara las inversas obtenidas por Gauss-Jordan y por matriz adjunta."""
    validar_matriz_cuadrada(
        matriz
    )

    gauss_jordan = calcular_inversa(
        matriz
    )

    adjunta = calcular_inversa_adjunta(
        matriz
    )

    if not gauss_jordan["es_invertible"]:
        return {
            "gauss_jordan": gauss_jordan,
            "adjunta": adjunta,
            "coinciden": (
                not adjunta["es_invertible"]
            )
        }

    return {
        "gauss_jordan": gauss_jordan,
        "adjunta": adjunta,
        "coinciden": (
            gauss_jordan["inversa"]
            == adjunta["inversa"]
        )
    }