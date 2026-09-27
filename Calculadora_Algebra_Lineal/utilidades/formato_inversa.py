# ==========================================================
# FORMATO DEL PROCEDIMIENTO DE LA MATRIZ INVERSA
# ==========================================================


# ==========================================================
# FORMATEAR MATRIZ NORMAL
# ==========================================================

def formatear_matriz(
    matriz
):

    if matriz is None:

        return "No existe."

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
# FORMATEAR MATRIZ AUMENTADA [A | I]
#
# La separación se coloca después de las
# primeras n columnas.
# ==========================================================

def formatear_matriz_aumentada(
    matriz,
    orden
):

    if matriz is None:

        return "No existe."

    lineas = []

    for fila in matriz:

        izquierda = []

        derecha = []

        # Parte izquierda.
        for j in range(
            orden
        ):

            izquierda.append(
                str(
                    fila[j]
                )
            )

        # Parte derecha.
        for j in range(
            orden,
            len(fila)
        ):

            derecha.append(
                str(
                    fila[j]
                )
            )

        linea = (
            "[ "
            + "   ".join(
                izquierda
            )
            + "   |   "
            + "   ".join(
                derecha
            )
            + " ]"
        )

        lineas.append(
            linea
        )

    return "\n".join(
        lineas
    )


# ==========================================================
# FORMATEAR HISTORIAL DE GAUSS-JORDAN
# ==========================================================

def formatear_historial_inversa(
    historial,
    orden
):

    if not historial:

        return (
            "No se realizaron operaciones "
            "de Gauss-Jordan."
        )

    texto = ""

    for numero, paso in enumerate(
        historial
    ):

        texto += (
            "Paso "
            + str(numero)
            + "\n"
        )

        texto += (
            "Operación: "
            + str(
                paso.get(
                    "operacion",
                    "Operación no especificada"
                )
            )
            + "\n\n"
        )

        matriz = paso.get(
            "matriz"
        )

        if matriz is not None:

            texto += formatear_matriz_aumentada(
                matriz,
                orden
            )

            texto += "\n"

        verificada = paso.get(
            "verificada"
        )

        if verificada is True:

            texto += (
                "\nVerificación de la operación: "
                "Correcta\n"
            )

        elif verificada is False:

            texto += (
                "\nVerificación de la operación: "
                "Incorrecta\n"
            )

        texto += (
            "\n"
            + "-" * 60
            + "\n\n"
        )

    return texto


# ==========================================================
# FORMATEAR VERIFICACIÓN
# ==========================================================

def formatear_verificacion_inversa(
    verificacion
):

    if verificacion is None:

        return (
            "No existe verificación porque "
            "la matriz no posee inversa."
        )

    texto = (
        "Primera comprobación:\n\n"
        "A · A⁻¹ =\n\n"
    )

    texto += formatear_matriz(
        verificacion[
            "producto_a_inversa"
        ]
    )

    texto += (
        "\n\n"
        "Matriz identidad esperada:\n\n"
    )

    texto += formatear_matriz(
        verificacion[
            "identidad"
        ]
    )

    texto += "\n\n"

    if verificacion[
        "verifica_a_inversa"
    ]:

        texto += (
            "A · A⁻¹ = I   ✓\n"
        )

    else:

        texto += (
            "A · A⁻¹ ≠ I\n"
        )

    texto += (
        "\n"
        + "-" * 60
        + "\n\n"
    )

    texto += (
        "Segunda comprobación:\n\n"
        "A⁻¹ · A =\n\n"
    )

    texto += formatear_matriz(
        verificacion[
            "producto_inversa_a"
        ]
    )

    texto += (
        "\n\n"
        "Matriz identidad esperada:\n\n"
    )

    texto += formatear_matriz(
        verificacion[
            "identidad"
        ]
    )

    texto += "\n\n"

    if verificacion[
        "verifica_inversa_a"
    ]:

        texto += (
            "A⁻¹ · A = I   ✓\n"
        )

    else:

        texto += (
            "A⁻¹ · A ≠ I\n"
        )

    texto += (
        "\n"
        + "=" * 60
        + "\n"
    )

    if verificacion[
        "verificada"
    ]:

        texto += (
            "\nVerificación final correcta.\n"
            "La matriz obtenida sí es A⁻¹."
        )

    else:

        texto += (
            "\nLa verificación final "
            "no fue satisfactoria."
        )

    return texto


# ==========================================================
# FORMATEAR RESULTADO DE MATRIZ NO INVERTIBLE
# ==========================================================

def formatear_no_invertible(
    resultado
):

    texto = (
        "MATRIZ ORIGINAL\n"
        + "=" * 60
        + "\n\n"
    )

    texto += formatear_matriz(
        resultado[
            "matriz_original"
        ]
    )

    texto += (
        "\n\n"
        "Determinante:\n\n"
        "det(A) = "
        + str(
            resultado[
                "determinante"
            ]
        )
        + "\n\n"
    )

    texto += (
        "Como det(A) = 0, la matriz "
        "no es invertible.\n\n"
    )

    texto += (
        resultado[
            "mensaje"
        ]
    )

    return texto


# ==========================================================
# FORMATEAR RESULTADO DE MATRIZ INVERTIBLE
# ==========================================================

def formatear_resultado_inversa(
    resultado
):

    if not resultado[
        "es_invertible"
    ]:

        return formatear_no_invertible(
            resultado
        )

    orden = resultado[
        "orden"
    ]

    texto = (
        "CÁLCULO DE LA MATRIZ INVERSA\n"
        + "=" * 60
        + "\n\n"
    )

    # ======================================================
    # MATRIZ ORIGINAL
    # ======================================================

    texto += (
        "Matriz original A:\n\n"
    )

    texto += formatear_matriz(
        resultado[
            "matriz_original"
        ]
    )

    # ======================================================
    # DETERMINANTE
    # ======================================================

    texto += (
        "\n\n"
        + "-" * 60
        + "\n"
    )

    texto += (
        "Comprobación de invertibilidad:\n\n"
    )

    texto += (
        "det(A) = "
        + str(
            resultado[
                "determinante"
            ]
        )
        + "\n"
    )

    texto += (
        "\nComo det(A) ≠ 0, "
        "la matriz es invertible.\n"
    )

    # ======================================================
    # CONSTRUCCIÓN [A | I]
    # ======================================================

    texto += (
        "\n"
        + "-" * 60
        + "\n"
    )

    texto += (
        "Construimos la matriz aumentada "
        "[A | I]:\n\n"
    )

    texto += formatear_matriz_aumentada(
        resultado[
            "matriz_aumentada"
        ],
        orden
    )

    # ======================================================
    # EXPLICACIÓN DEL MÉTODO
    # ======================================================

    texto += (
        "\n\n"
        "Aplicamos operaciones elementales "
        "por filas mediante Gauss-Jordan.\n\n"
        "El objetivo es transformar:\n\n"
        "[A | I]\n\n"
        "en:\n\n"
        "[I | A⁻¹]\n"
    )

    # ======================================================
    # PROCEDIMIENTO
    # ======================================================

    texto += (
        "\n"
        + "=" * 60
        + "\n"
        "PROCEDIMIENTO GAUSS-JORDAN\n"
        + "=" * 60
        + "\n\n"
    )

    texto += formatear_historial_inversa(
        resultado[
            "historial"
        ],
        orden
    )

    # ======================================================
    # MATRIZ FINAL
    # ======================================================

    texto += (
        "\n"
        + "=" * 60
        + "\n"
        "MATRIZ AUMENTADA FINAL\n"
        + "=" * 60
        + "\n\n"
    )

    texto += formatear_matriz_aumentada(
        resultado[
            "matriz_reducida"
        ],
        orden
    )

    # ======================================================
    # INVERSA
    # ======================================================

    texto += (
        "\n\n"
        "La parte izquierda se convirtió "
        "en la matriz identidad.\n"
        "Por tanto, la parte derecha "
        "corresponde a A⁻¹.\n\n"
    )

    texto += (
        "A⁻¹ =\n\n"
    )

    texto += formatear_matriz(
        resultado[
            "inversa"
        ]
    )

    return texto


# ==========================================================
# FUNCIÓN PRINCIPAL
# ==========================================================

def formatear_procedimiento_inversa(
    resultado
):

    texto = formatear_resultado_inversa(
        resultado
    )

    # Si no existe inversa,
    # no hay nada que verificar.
    if not resultado[
        "es_invertible"
    ]:

        return texto

    texto += (
        "\n\n"
        + "=" * 60
        + "\n"
        "VERIFICACIÓN DE LA INVERSA\n"
        + "=" * 60
        + "\n\n"
    )

    texto += formatear_verificacion_inversa(
        resultado[
            "verificacion"
        ]
    )

    return texto