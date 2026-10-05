"""
Da formato al procedimiento de inversa mediante matriz adjunta.
Muestra determinante, matriz de cofactores, adjunta e inversa obtenida.
Tema de clase: matriz adjunta e inversa de una matriz.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_determinantes import (
    formatear_matriz
)


def formatear_verificacion(verificacion):
    """Presenta la comprobación A·A^-1 = I y A^-1·A = I."""
    if verificacion is None:
        return "No existe verificación."

    texto = (
        "COMPROBACIÓN AUTOMÁTICA\n"
        + "=" * 60
        + "\n\n"
        + "A · A⁻¹ =\n\n"
        + formatear_matriz(
            verificacion["producto_a_inversa"]
        )
        + "\n\n"
        + "A⁻¹ · A =\n\n"
        + formatear_matriz(
            verificacion["producto_inversa_a"]
        )
        + "\n\n"
        + "Matriz identidad:\n\n"
        + formatear_matriz(
            verificacion["identidad"]
        )
        + "\n\n"
    )

    if verificacion["verificada"]:
        texto += (
            "La comprobación es correcta:\n"
            "A · A⁻¹ = I y A⁻¹ · A = I."
        )
    else:
        texto += (
            "La matriz obtenida no superó "
            "la comprobación de inversa."
        )

    return texto


def formatear_matriz_singular(resultado):
    """Presenta el diagnóstico cuando det(A) es cero y no existe inversa."""
    return (
        "INVERSA POR MATRIZ ADJUNTA\n"
        + "=" * 60
        + "\n\n"
        + "Matriz A:\n\n"
        + formatear_matriz(
            resultado["matriz_original"]
        )
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["determinante"]
        )
        + "\n\n"
        + "Como det(A) = 0, no se puede aplicar\n"
        + "A⁻¹ = (1/det(A)) · adj(A).\n\n"
        + resultado["mensaje"]
    )


def formatear_inversa_adjunta(resultado):
    """Presenta el procedimiento completo para obtener A^-1 mediante adj(A)."""
    if not resultado["es_invertible"]:
        return formatear_matriz_singular(
            resultado
        )

    texto = (
        "INVERSA POR MATRIZ ADJUNTA\n"
        + "=" * 60
        + "\n\n"
        + "Matriz A:\n\n"
        + formatear_matriz(
            resultado["matriz_original"]
        )
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["determinante"]
        )
        + "\n\n"
    )

    texto += (
        "Como det(A) ≠ 0, la matriz es invertible.\n\n"
        + "-" * 60
        + "\n\n"
        + "1. MATRIZ DE COFACTORES\n\n"
        + formatear_matriz(
            resultado["matriz_cofactores"]
        )
        + "\n\n"
    )

    texto += (
        "-" * 60
        + "\n\n"
        + "2. MATRIZ ADJUNTA\n\n"
        + "adj(A) es la transpuesta de la matriz "
        + "de cofactores:\n\n"
        + "adj(A) =\n\n"
        + formatear_matriz(
            resultado["adjunta"]
        )
        + "\n\n"
    )

    texto += (
        "-" * 60
        + "\n\n"
        + "3. CÁLCULO DE LA INVERSA\n\n"
        + "A⁻¹ = (1/det(A)) · adj(A)\n\n"
        + "A⁻¹ = ("
        + str(
            resultado["factor"]
        )
        + ") · adj(A)\n\n"
        + "A⁻¹ =\n\n"
        + formatear_matriz(
            resultado["inversa"]
        )
        + "\n\n"
    )

    texto += (
        "-" * 60
        + "\n\n"
        + formatear_verificacion(
            resultado["verificacion"]
        )
    )

    return texto


def formatear_comparacion_inversas(resultado):
    """Compara las inversas obtenidas por Gauss-Jordan y matriz adjunta."""
    gauss_jordan = resultado[
        "gauss_jordan"
    ]

    adjunta = resultado[
        "adjunta"
    ]

    texto = (
        "COMPARACIÓN DE MÉTODOS DE INVERSA\n"
        + "=" * 60
        + "\n\n"
    )

    if not gauss_jordan["es_invertible"]:
        texto += (
            "det(A) = 0\n\n"
            "La matriz es singular y ninguno de "
            "los métodos produce una inversa.\n\n"
        )

        if resultado["coinciden"]:
            texto += (
                "Ambos métodos coinciden en que "
                "la matriz no es invertible."
            )

        return texto

    texto += (
        "Inversa por Gauss-Jordan:\n\n"
        + formatear_matriz(
            gauss_jordan["inversa"]
        )
        + "\n\n"
        + "Inversa por matriz adjunta:\n\n"
        + formatear_matriz(
            adjunta["inversa"]
        )
        + "\n\n"
    )

    if resultado["coinciden"]:
        texto += (
            "Ambos métodos producen la misma matriz inversa."
        )
    else:
        texto += (
            "Los métodos produjeron resultados diferentes."
        )

    return texto