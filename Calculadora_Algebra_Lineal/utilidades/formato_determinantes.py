from utilidades.formato_interfaz import (
    convertir_numero_subindice
)


# ==========================================================
# FORMATO DE DETERMINANTES
# ==========================================================


# ==========================================================
# FORMATEAR MATRIZ
# ==========================================================

def formatear_matriz(
    matriz
):

    lineas = []

    for fila in matriz:

        contenido = "   ".join(
            str(valor)
            for valor in fila
        )

        lineas.append(
            "[ "
            + contenido
            + " ]"
        )

    return "\n".join(
        lineas
    )


# ==========================================================
# NOMBRE DE UNA POSICIÓN
#
# Ejemplo:
# (0, 0) -> ₁₁
# ==========================================================

def nombre_posicion(
    fila,
    columna
):

    fila_texto = convertir_numero_subindice(
        fila + 1
    )

    columna_texto = convertir_numero_subindice(
        columna + 1
    )

    return (
        fila_texto
        + columna_texto
    )


# ==========================================================
# FORMATEAR DETERMINANTE 1 x 1
# ==========================================================

def formatear_determinante_1x1(
    resultado
):

    valor = resultado[
        "determinante"
    ]

    texto = (
        "Matriz de orden 1:\n\n"
    )

    texto += formatear_matriz(
        resultado["matriz"]
    )

    texto += (
        "\n\n"
        "El determinante de una matriz 1 × 1 "
        "es su único elemento.\n\n"
        "det(A) = "
        + str(valor)
    )

    return texto


# ==========================================================
# FORMATEAR DETERMINANTE 2 x 2
# ==========================================================

def formatear_determinante_2x2(
    resultado
):

    a = resultado["a"]
    b = resultado["b"]
    c = resultado["c"]
    d = resultado["d"]

    producto_1 = resultado[
        "producto_1"
    ]

    producto_2 = resultado[
        "producto_2"
    ]

    determinante = resultado[
        "determinante"
    ]

    texto = (
        "Matriz de orden 2:\n\n"
    )

    texto += formatear_matriz(
        resultado["matriz"]
    )

    texto += (
        "\n\n"
        "Para una matriz 2 × 2:\n\n"
        "det(A) = ad - bc\n\n"
    )

    texto += (
        "det(A) = "
        + "("
        + str(a)
        + ")("
        + str(d)
        + ")"
        + " - "
        + "("
        + str(b)
        + ")("
        + str(c)
        + ")"
        + "\n"
    )

    texto += (
        "det(A) = "
        + str(producto_1)
        + " - "
        + str(producto_2)
        + "\n"
    )

    texto += (
        "det(A) = "
        + str(determinante)
    )

    return texto


# ==========================================================
# FORMATEAR UN TÉRMINO DEL DESARROLLO
# ==========================================================

def formatear_termino(
    termino,
    numero_termino
):

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

    signo = termino[
        "signo"
    ]

    texto = (
        "Término "
        + str(numero_termino)
        + "\n"
    )

    texto += (
        "Posición: a"
        + posicion
        + "\n"
    )

    texto += (
        "Elemento: "
        + str(elemento)
        + "\n"
    )

    # ======================================================
    # ELEMENTO CERO
    # ======================================================

    if termino[
        "omitido"
    ]:

        texto += (
            "\nEl elemento es 0, por lo tanto "
            "este término no aporta al determinante.\n"
        )

        texto += (
            "Término = 0"
        )

        return texto

    # ======================================================
    # MENOR
    # ======================================================

    menor = termino[
        "menor"
    ]

    determinante_menor = termino[
        "determinante_menor"
    ]

    cofactor = termino[
        "cofactor"
    ]

    valor_termino = termino[
        "termino"
    ]

    texto += (
        "\nMenor M"
        + posicion
        + ":\n\n"
    )

    texto += formatear_matriz(
        menor
    )

    texto += (
        "\n\n"
        "det(M"
        + posicion
        + ") = "
        + str(determinante_menor)
        + "\n"
    )

    # ======================================================
    # SIGNO DEL COFACTOR
    # ======================================================

    texto += (
        "\nSigno del cofactor:\n"
    )

    texto += (
        "(-1)^("
        + str(fila + 1)
        + "+"
        + str(columna + 1)
        + ") = "
        + str(signo)
        + "\n"
    )

    # ======================================================
    # COFACTOR
    # ======================================================

    texto += (
        "\nC"
        + posicion
        + " = "
        + "("
        + str(signo)
        + ")("
        + str(determinante_menor)
        + ")"
        + "\n"
    )

    texto += (
        "C"
        + posicion
        + " = "
        + str(cofactor)
        + "\n"
    )

    # ======================================================
    # TÉRMINO FINAL
    # ======================================================

    texto += (
        "\nTérmino = "
        + str(elemento)
        + "("
        + str(cofactor)
        + ")"
        + "\n"
    )

    texto += (
        "Término = "
        + str(valor_termino)
    )

    return texto


# ==========================================================
# FORMATEAR DESARROLLO POR COFACTORES
# ==========================================================

def formatear_desarrollo_cofactores(
    resultado
):

    tipo = resultado[
        "tipo_desarrollo"
    ]

    indice = resultado[
        "indice_desarrollo"
    ]

    determinante = resultado[
        "determinante"
    ]

    terminos = resultado[
        "terminos"
    ]

    texto = (
        "Matriz original:\n\n"
    )

    texto += formatear_matriz(
        resultado["matriz"]
    )

    texto += (
        "\n\n"
        "Se utilizará desarrollo por cofactores.\n"
    )

    # ======================================================
    # FILA O COLUMNA SELECCIONADA
    # ======================================================

    if tipo == "fila":

        texto += (
            "Se seleccionó automáticamente la fila "
            + str(indice + 1)
            + " porque facilita el desarrollo.\n"
        )

    else:

        texto += (
            "Se seleccionó automáticamente la columna "
            + str(indice + 1)
            + " porque facilita el desarrollo.\n"
        )

    texto += (
        "\n"
        + "=" * 55
        + "\n\n"
    )

    # ======================================================
    # CADA TÉRMINO
    # ======================================================

    for numero, termino in enumerate(
        terminos,
        start=1
    ):

        texto += formatear_termino(
            termino,
            numero
        )

        texto += (
            "\n\n"
            + "-" * 55
            + "\n\n"
        )

    # ======================================================
    # SUMA DE LOS TÉRMINOS
    # ======================================================

    valores = []

    for termino in terminos:

        valores.append(
            str(
                termino["termino"]
            )
        )

    texto += (
        "Suma de los términos:\n\n"
    )

    texto += (
        "det(A) = "
        + " + ".join(
            valores
        )
        + "\n"
    )

    texto += (
        "\ndet(A) = "
        + str(determinante)
    )

    return texto


# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def formatear_procedimiento_determinante(
    resultado
):

    tipo = resultado[
        "tipo_desarrollo"
    ]

    if tipo == "directo":

        return formatear_determinante_1x1(
            resultado
        )

    if tipo == "2x2":

        return formatear_determinante_2x2(
            resultado
        )

    return formatear_desarrollo_cofactores(
        resultado
    )