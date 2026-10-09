"""
Calcula paso a paso cada cofactor Cᵢⱼ de una matriz cuadrada.
Construye el menor Mᵢⱼ, su determinante, el signo y el valor de Cᵢⱼ.
Tema de clase: determinantes, cofactores y matriz adjunta.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    obtener_menor,
    obtener_signo_cofactor,
    calcular_determinante,
)


def _detalle_determinante_menor(menor):
    """Describe el cálculo directo de det(Mᵢⱼ) cuando el menor es 1×1 o 2×2."""
    orden = len(menor)

    if orden == 0:
        return {
            "tipo": "vacio",
            "texto": "det(M) = 1 por convenio para una matriz 1 × 1.",
        }

    if orden == 1:
        valor = menor[0][0]

        return {
            "tipo": "1x1",
            "valor": valor,
            "texto": f"det(M) = {valor}",
        }

    if orden == 2:
        a = menor[0][0]
        b = menor[0][1]
        c = menor[1][0]
        d = menor[1][1]

        producto_1 = a * d
        producto_2 = b * c
        determinante = producto_1 - producto_2

        return {
            "tipo": "2x2",
            "a": a,
            "b": b,
            "c": c,
            "d": d,
            "producto_1": producto_1,
            "producto_2": producto_2,
            "determinante": determinante,
            "texto": (
                f"det(M) = ({a})({d}) - ({b})({c})\n"
                f"det(M) = {producto_1} - {producto_2}\n"
                f"det(M) = {determinante}"
            ),
        }

    determinante = calcular_determinante(
        menor
    )

    return {
        "tipo": "general",
        "determinante": determinante,
        "texto": (
            "det(M) se obtiene con el método general de determinantes.\n"
            f"det(M) = {determinante}"
        ),
    }


def calcular_cofactor_detallado(matriz, fila, columna):
    """Calcula Mᵢⱼ, det(Mᵢⱼ), (-1)^(i+j) y Cᵢⱼ."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    if fila < 0 or fila >= orden:
        raise ValueError(
            "La fila indicada para el cofactor no es válida."
        )

    if columna < 0 or columna >= orden:
        raise ValueError(
            "La columna indicada para el cofactor no es válida."
        )

    signo = obtener_signo_cofactor(
        fila,
        columna
    )

    if orden == 1:
        menor = []
        determinante_menor = Fraction(1)
        detalle_menor = _detalle_determinante_menor(
            menor
        )
    else:
        menor = obtener_menor(
            matriz,
            fila,
            columna
        )

        determinante_menor = calcular_determinante(
            menor
        )

        detalle_menor = _detalle_determinante_menor(
            menor
        )

    cofactor = signo * determinante_menor

    return {
        "fila": fila,
        "columna": columna,
        "menor": menor,
        "determinante_menor": determinante_menor,
        "detalle_determinante_menor": detalle_menor,
        "signo": signo,
        "exponente": (fila + 1) + (columna + 1),
        "cofactor": cofactor,
    }


def calcular_cofactores_detallados(matriz):
    """Calcula todos los Cᵢⱼ y devuelve también la matriz de cofactores."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    detalles = []
    matriz_cofactores = []

    for fila in range(orden):
        fila_cofactores = []

        for columna in range(orden):
            detalle = calcular_cofactor_detallado(
                matriz,
                fila,
                columna
            )

            detalles.append(
                detalle
            )

            fila_cofactores.append(
                detalle["cofactor"]
            )

        matriz_cofactores.append(
            fila_cofactores
        )

    return {
        "matriz": matriz,
        "orden": orden,
        "detalles": detalles,
        "matriz_cofactores": matriz_cofactores,
    }
