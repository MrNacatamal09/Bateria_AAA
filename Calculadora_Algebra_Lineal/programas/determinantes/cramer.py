"""
Resuelve sistemas cuadrados mediante la regla de Cramer.
Calcula det(A), cada det(Aᵢ) y la solución exacta con Fraction.
Tema de clase: determinantes aplicados a sistemas de ecuaciones lineales.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.determinantes.determinante import (
    calcular_determinante,
    validar_matriz_cuadrada
)


def _validar_vector(vector_b, orden):
    """Valida que b contenga exactamente n términos independientes."""
    if len(vector_b) != orden:
        raise ValueError(
            "El vector b debe tener la misma cantidad de elementos que el orden de A."
        )


def reemplazar_columna(matriz_a, vector_b, columna):
    """Devuelve Aᵢ sustituyendo la columna indicada por el vector b."""
    matriz_reemplazada = []

    for fila in matriz_a:
        matriz_reemplazada.append(
            fila.copy()
        )

    for fila in range(len(matriz_reemplazada)):
        matriz_reemplazada[fila][columna] = vector_b[fila]

    return matriz_reemplazada


def verificar_solucion_cramer(matriz_a, vector_b, solucion):
    """Sustituye la solución en Ax=b y verifica cada ecuación."""
    ecuaciones = []
    correcta = True

    for i in range(len(matriz_a)):
        lado_izquierdo = Fraction(0)

        for j in range(len(solucion)):
            lado_izquierdo += matriz_a[i][j] * solucion[j]

        lado_derecho = vector_b[i]
        ecuacion_correcta = lado_izquierdo == lado_derecho

        ecuaciones.append(
            {
                "ecuacion": i + 1,
                "lado_izquierdo": lado_izquierdo,
                "lado_derecho": lado_derecho,
                "correcta": ecuacion_correcta
            }
        )

        if not ecuacion_correcta:
            correcta = False

    return {
        "correcta": correcta,
        "ecuaciones": ecuaciones
    }


def resolver_cramer(matriz_a, vector_b):
    """Resuelve Ax=b con Cramer cuando A es cuadrada y det(A) ≠ 0."""
    validar_matriz_cuadrada(
        matriz_a
    )

    orden = len(
        matriz_a
    )

    _validar_vector(
        vector_b,
        orden
    )

    determinante_a = calcular_determinante(
        matriz_a
    )

    if determinante_a == 0:
        raise ValueError(
            "El método de Cramer no se puede aplicar: det(A) = 0."
        )

    calculos = []
    solucion = []

    for columna in range(orden):
        matriz_ai = reemplazar_columna(
            matriz_a,
            vector_b,
            columna
        )

        determinante_ai = calcular_determinante(
            matriz_ai
        )

        valor = determinante_ai / determinante_a

        calculos.append(
            {
                "variable": columna,
                "matriz": matriz_ai,
                "determinante": determinante_ai,
                "valor": valor
            }
        )

        solucion.append(
            valor
        )

    verificacion = verificar_solucion_cramer(
        matriz_a,
        vector_b,
        solucion
    )

    return {
        "matriz_a": matriz_a,
        "vector_b": vector_b,
        "determinante_a": determinante_a,
        "calculos": calculos,
        "solucion": solucion,
        "verificacion": verificacion
    }
