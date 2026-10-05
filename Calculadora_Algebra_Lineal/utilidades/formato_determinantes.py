"""
Da formato legible a los procedimientos de determinantes del Programa 5.
Presenta cofactores, regla de Sarrus y reducción triangular paso a paso.
Tema de clase: cálculo y comparación de determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_interfaz import (
    convertir_numero_subindice
)


def formatear_matriz(matriz):
    """Convierte una matriz en un texto organizado por filas."""
    if matriz is None:
        return "No existe."

    if not matriz:
        return "[]"

    lineas = []

    for fila in matriz:
        contenido = "   ".join(
            str(valor)
            for valor in fila
        )

        lineas.append(
            "[ " + contenido + " ]"
        )

    return "\n".join(
        lineas
    )


def nombre_posicion(fila, columna):
    """Devuelve una posición matricial usando subíndices matemáticos."""
    return (
        convertir_numero_subindice(
            fila + 1
        )
        + convertir_numero_subindice(
            columna + 1
        )
    )


def formatear_determinante_1x1(resultado):
    """Presenta el cálculo directo del determinante de una matriz 1x1."""
    valor = resultado[
        "matriz"
    ][0][0]

    return (
        "DETERMINANTE DE ORDEN 1\n"
        + "=" * 60
        + "\n\n"
        + formatear_matriz(
            resultado["matriz"]
        )
        + "\n\n"
        + "det(A) = "
        + str(valor)
    )


def formatear_determinante_2x2(resultado):
    """Presenta el cálculo ad - bc para una matriz de orden 2."""
    a = resultado["a"]
    b = resultado["b"]
    c = resultado["c"]
    d = resultado["d"]

    texto = (
        "DETERMINANTE DE ORDEN 2\n"
        + "=" * 60
        + "\n\n"
        + formatear_matriz(
            resultado["matriz"]
        )
        + "\n\n"
    )

    texto += (
        "det(A) = ad - bc\n\n"
        + "det(A) = "
        + f"({a})({d}) - ({b})({c})"
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["producto_1"]
        )
        + " - "
        + str(
            resultado["producto_2"]
        )
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["determinante"]
        )
    )

    return texto


def formatear_termino_cofactor(termino):
    """Presenta un término del desarrollo por cofactores."""
    fila = termino[
        "fila"
    ]

    columna = termino[
        "columna"
    ]

    posicion = nombre_posicion(
        fila,
        columna
    )

    elemento = termino[
        "elemento"
    ]

    if termino[
        "omitido"
    ]:
        return (
            "a"
            + posicion
            + " = 0\n"
            + "El término se omite porque no aporta "
            + "al determinante."
        )

    texto = (
        "a"
        + posicion
        + " = "
        + str(elemento)
        + "\n\n"
    )

    texto += (
        "M"
        + posicion
        + " =\n\n"
        + formatear_matriz(
            termino["menor"]
        )
        + "\n\n"
    )

    texto += (
        "det(M"
        + posicion
        + ") = "
        + str(
            termino[
                "determinante_menor"
            ]
        )
        + "\n\n"
    )

    texto += (
        "C"
        + posicion
        + " = (-1)^("
        + str(fila + 1)
        + "+"
        + str(columna + 1)
        + ") · det(M"
        + posicion
        + ")\n\n"
    )

    texto += (
        "C"
        + posicion
        + " = "
        + str(
            termino["cofactor"]
        )
        + "\n\n"
    )

    texto += (
        "a"
        + posicion
        + "C"
        + posicion
        + " = "
        + str(elemento)
        + "("
        + str(
            termino["cofactor"]
        )
        + ")"
        + " = "
        + str(
            termino["termino"]
        )
    )

    return texto


def formatear_desarrollo_cofactores(resultado):
    """Presenta el desarrollo completo por la fila o columna seleccionada."""
    tipo = resultado[
        "tipo_desarrollo"
    ]

    indice = resultado[
        "indice_desarrollo"
    ]

    texto = (
        "EXPANSIÓN POR COFACTORES\n"
        + "=" * 60
        + "\n\n"
        + "Matriz A:\n\n"
        + formatear_matriz(
            resultado["matriz"]
        )
        + "\n\n"
    )

    texto += (
        "Se seleccionó automáticamente la "
        + tipo
        + " "
        + str(indice + 1)
        + " porque permite reducir el trabajo "
        + "del desarrollo.\n\n"
    )

    texto += (
        "-" * 60
        + "\n\n"
    )

    for numero, termino in enumerate(
        resultado["terminos"],
        start=1
    ):
        texto += (
            "Término "
            + str(numero)
            + "\n\n"
        )

        texto += formatear_termino_cofactor(
            termino
        )

        texto += (
            "\n\n"
            + "-" * 60
            + "\n\n"
        )

    valores = [
        str(
            termino["termino"]
        )
        for termino in resultado[
            "terminos"
        ]
    ]

    texto += (
        "Suma de términos:\n\n"
        + "det(A) = "
        + " + ".join(
            valores
        )
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["determinante"]
        )
    )

    return texto


def formatear_procedimiento_determinante(resultado):
    """Presenta el procedimiento por cofactores según el orden de la matriz."""
    orden = resultado[
        "orden"
    ]

    if orden == 1:
        return formatear_determinante_1x1(
            resultado
        )

    if orden == 2:
        return formatear_determinante_2x2(
            resultado
        )

    return formatear_desarrollo_cofactores(
        resultado
    )


def formatear_sarrus(resultado):
    """Presenta los seis productos usados en la regla de Sarrus para una matriz 3x3."""
    positivos = resultado[
        "productos_positivos"
    ]

    negativos = resultado[
        "productos_negativos"
    ]

    matriz = resultado[
        "matriz"
    ]

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    texto = (
        "REGLA DE SARRUS\n"
        + "=" * 60
        + "\n\n"
        + "Matriz A:\n\n"
        + formatear_matriz(
            matriz
        )
        + "\n\n"
    )

    texto += (
        "Diagonales positivas:\n\n"
        + f"({a})({e})({i}) = {positivos[0]}\n"
        + f"({b})({f})({g}) = {positivos[1]}\n"
        + f"({c})({d})({h}) = {positivos[2]}\n\n"
    )

    texto += (
        "Suma positiva = "
        + str(
            resultado["suma_positiva"]
        )
        + "\n\n"
    )

    texto += (
        "Diagonales negativas:\n\n"
        + f"({c})({e})({g}) = {negativos[0]}\n"
        + f"({b})({d})({i}) = {negativos[1]}\n"
        + f"({a})({f})({h}) = {negativos[2]}\n\n"
    )

    texto += (
        "Suma negativa = "
        + str(
            resultado["suma_negativa"]
        )
        + "\n\n"
    )

    texto += (
        "det(A) = "
        + str(
            resultado["suma_positiva"]
        )
        + " - "
        + str(
            resultado["suma_negativa"]
        )
        + "\n\n"
    )

    texto += (
        "det(A) = "
        + str(
            resultado["determinante"]
        )
    )

    return texto


def formatear_historial_triangular(historial):
    """Presenta las operaciones de fila realizadas durante la triangularización."""
    lineas = []

    for numero, paso in enumerate(
        historial
    ):
        lineas.append(
            "Paso "
            + str(numero)
        )

        lineas.append(
            str(
                paso["operacion"]
            )
        )

        lineas.append("")

        lineas.append(
            formatear_matriz(
                paso["matriz"]
            )
        )

        lineas.append("")
        lineas.append(
            "-" * 60
        )
        lineas.append("")

    return "\n".join(
        lineas
    )


def formatear_triangular(resultado):
    """Presenta la reducción triangular y el cálculo del producto de la diagonal."""
    texto = (
        "REDUCCIÓN A FORMA TRIANGULAR\n"
        + "=" * 60
        + "\n\n"
        + "Matriz original:\n\n"
        + formatear_matriz(
            resultado[
                "matriz_original"
            ]
        )
        + "\n\n"
    )

    texto += (
        "Procedimiento:\n\n"
        + formatear_historial_triangular(
            resultado[
                "historial"
            ]
        )
    )

    texto += (
        "\nMatriz triangular final:\n\n"
        + formatear_matriz(
            resultado[
                "matriz_triangular"
            ]
        )
        + "\n\n"
    )

    diagonal = []

    for indice in range(
        len(
            resultado[
                "matriz_triangular"
            ]
        )
    ):
        diagonal.append(
            resultado[
                "matriz_triangular"
            ][indice][indice]
        )

    texto += (
        "Producto de la diagonal:\n\n"
        + " · ".join(
            str(valor)
            for valor in diagonal
        )
        + " = "
        + str(
            resultado[
                "producto_diagonal"
            ]
        )
        + "\n\n"
    )

    texto += (
        "Intercambios de fila: "
        + str(
            resultado[
                "intercambios"
            ]
        )
        + "\n"
    )

    if resultado[
        "intercambios"
    ] % 2 == 0:
        texto += (
            "El número de intercambios es par, "
            "por lo que el signo no cambia.\n\n"
        )
    else:
        texto += (
            "El número de intercambios es impar, "
            "por lo que el signo del determinante cambia.\n\n"
        )

    texto += (
        "Número de pivotes: "
        + str(
            resultado[
                "num_pivotes"
            ]
        )
        + "\n\n"
    )

    texto += (
        "det(A) = "
        + str(
            resultado[
                "determinante"
            ]
        )
    )

    return texto


def formatear_comparacion_determinantes(resultado):
    """Presenta y compara los resultados obtenidos por todos los métodos disponibles."""
    cofactores = resultado[
        "cofactores"
    ]

    sarrus = resultado[
        "sarrus"
    ]

    triangular = resultado[
        "triangular"
    ]

    texto = (
        "COMPARACIÓN DE MÉTODOS\n"
        + "=" * 60
        + "\n\n"
        + "Cofactores: det(A) = "
        + str(
            cofactores[
                "determinante"
            ]
        )
        + "\n"
    )

    if sarrus is not None:
        texto += (
            "Sarrus: det(A) = "
            + str(
                sarrus[
                    "determinante"
                ]
            )
            + "\n"
        )

    texto += (
        "Reducción triangular: det(A) = "
        + str(
            triangular[
                "determinante"
            ]
        )
        + "\n\n"
    )

    if resultado[
        "coinciden"
    ]:
        texto += (
            "Los métodos coinciden."
        )
    else:
        texto += (
            "Los métodos no coinciden."
        )

    return texto