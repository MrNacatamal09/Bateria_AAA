"""
Registra los procedimientos usados para calcular determinantes en el Programa 5.
Incluye expansión por cofactores, regla de Sarrus y reducción triangular.
Tema de clase: métodos para el cálculo de determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    obtener_menor,
    obtener_signo_cofactor,
    calcular_determinante,
    seleccionar_fila_o_columna,
    calcular_determinante_sarrus,
    triangularizar_para_determinante
)


def _resultado_orden_uno(matriz):
    """Construye el procedimiento directo para una matriz de orden 1."""
    return {
        "orden": 1,
        "matriz": matriz,
        "tipo_desarrollo": "directo",
        "determinante": matriz[0][0],
        "terminos": []
    }


def _resultado_orden_dos(matriz):
    """Construye el procedimiento ad - bc para una matriz de orden 2."""
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]

    producto_1 = a * d
    producto_2 = b * c

    return {
        "orden": 2,
        "matriz": matriz,
        "tipo_desarrollo": "2x2",
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "producto_1": producto_1,
        "producto_2": producto_2,
        "determinante": producto_1 - producto_2,
        "terminos": []
    }


def _crear_termino_cofactor(matriz, fila, columna):
    """Construye un término del desarrollo por cofactores y devuelve sus datos."""
    elemento = matriz[fila][columna]
    signo = obtener_signo_cofactor(
        fila,
        columna
    )

    # Un elemento cero no modifica el determinante y evita calcular un menor innecesario.
    if elemento == 0:
        return {
            "fila": fila,
            "columna": columna,
            "elemento": elemento,
            "signo": signo,
            "menor": None,
            "determinante_menor": Fraction(0),
            "cofactor": Fraction(0),
            "termino": Fraction(0),
            "omitido": True
        }

    menor = obtener_menor(
        matriz,
        fila,
        columna
    )

    determinante_menor = calcular_determinante(
        menor
    )

    cofactor = (
        signo
        * determinante_menor
    )

    return {
        "fila": fila,
        "columna": columna,
        "elemento": elemento,
        "signo": signo,
        "menor": menor,
        "determinante_menor": determinante_menor,
        "cofactor": cofactor,
        "termino": elemento * cofactor,
        "omitido": False
    }


def _desarrollar_por_fila(matriz, fila):
    """Genera los términos del desarrollo por una fila y devuelve su suma."""
    terminos = []

    for columna in range(
        len(matriz)
    ):
        terminos.append(
            _crear_termino_cofactor(
                matriz,
                fila,
                columna
            )
        )

    determinante = sum(
        (
            termino["termino"]
            for termino in terminos
        ),
        Fraction(0)
    )

    return terminos, determinante


def _desarrollar_por_columna(matriz, columna):
    """Genera los términos del desarrollo por una columna y devuelve su suma."""
    terminos = []

    for fila in range(
        len(matriz)
    ):
        terminos.append(
            _crear_termino_cofactor(
                matriz,
                fila,
                columna
            )
        )

    determinante = sum(
        (
            termino["termino"]
            for termino in terminos
        ),
        Fraction(0)
    )

    return terminos, determinante


def calcular_determinante_con_procedimiento(matriz):
    """Calcula el determinante por cofactores y conserva los datos del procedimiento."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(matriz)

    if orden == 1:
        return _resultado_orden_uno(
            matriz
        )

    if orden == 2:
        return _resultado_orden_dos(
            matriz
        )

    tipo, indice = seleccionar_fila_o_columna(
        matriz
    )

    if tipo == "fila":
        terminos, determinante = _desarrollar_por_fila(
            matriz,
            indice
        )
    else:
        terminos, determinante = _desarrollar_por_columna(
            matriz,
            indice
        )

    return {
        "orden": orden,
        "matriz": matriz,
        "tipo_desarrollo": tipo,
        "indice_desarrollo": indice,
        "terminos": terminos,
        "determinante": determinante
    }


def calcular_sarrus_con_procedimiento(matriz):
    """Calcula un determinante 3x3 por Sarrus y conserva sus seis productos."""
    validar_matriz_cuadrada(
        matriz
    )

    if len(matriz) != 3:
        raise ValueError(
            "La regla de Sarrus solamente se aplica "
            "a matrices de orden 3."
        )

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    productos_positivos = [
        a * e * i,
        b * f * g,
        c * d * h
    ]

    productos_negativos = [
        c * e * g,
        b * d * i,
        a * f * h
    ]

    suma_positiva = sum(
        productos_positivos,
        Fraction(0)
    )

    suma_negativa = sum(
        productos_negativos,
        Fraction(0)
    )

    return {
        "matriz": matriz,
        "productos_positivos": productos_positivos,
        "productos_negativos": productos_negativos,
        "suma_positiva": suma_positiva,
        "suma_negativa": suma_negativa,
        "determinante": calcular_determinante_sarrus(
            matriz
        )
    }


def calcular_triangular_con_procedimiento(matriz):
    """Reduce la matriz a triangular y conserva operaciones, pivotes y determinante."""
    validar_matriz_cuadrada(
        matriz
    )

    return triangularizar_para_determinante(
        matriz
    )


def comparar_procedimientos_determinante(matriz):
    """Compara cofactores, triangularización y Sarrus cuando la matriz es 3x3."""
    validar_matriz_cuadrada(
        matriz
    )

    cofactores = calcular_determinante_con_procedimiento(
        matriz
    )

    triangular = calcular_triangular_con_procedimiento(
        matriz
    )

    sarrus = None

    if len(matriz) == 3:
        sarrus = calcular_sarrus_con_procedimiento(
            matriz
        )

    coinciden = (
        cofactores["determinante"]
        == triangular["determinante"]
    )

    if sarrus is not None:
        coinciden = (
            coinciden
            and sarrus["determinante"]
            == cofactores["determinante"]
        )

    return {
        "cofactores": cofactores,
        "sarrus": sarrus,
        "triangular": triangular,
        "coinciden": coinciden
    }