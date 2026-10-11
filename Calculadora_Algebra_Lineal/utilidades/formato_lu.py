"""
Da formato al procedimiento de factorización LU y resolución de Ax = b.
Muestra multiplicadores, operaciones, L, U, y, x y las verificaciones.
Tema de clase: factorización LU y sustituciones triangulares.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_interfaz import (
    convertir_numero_subindice,
)


def formatear_matriz(matriz):
    """Convierte una matriz en filas de texto."""
    return "\n".join(
        "[ "
        + "   ".join(
            str(valor)
            for valor in fila
        )
        + " ]"
        for fila in matriz
    )


def formatear_vector(vector):
    """Convierte un vector en formato columna."""
    return "\n".join(
        f"[ {valor} ]"
        for valor in vector
    )


def _nombre(letra, indice):
    """Construye y₁, y₂, x₁, x₂ y nombres equivalentes."""
    return (
        letra
        + convertir_numero_subindice(
            indice + 1
        )
    )


def _estado(cumple):
    """Devuelve la conclusión textual de una verificación."""
    return (
        "Se cumple"
        if cumple
        else "No se cumple"
    )


def _formatear_multiplicadores(resultado):
    """Muestra cómo se obtiene cada entrada inferior de L."""
    lineas = [
        "MULTIPLICADORES REGISTRADOS EN L",
        "=" * 60,
        "",
    ]

    if not resultado["multiplicadores"]:
        lineas.append(
            "No fue necesario eliminar entradas debajo de los pivotes."
        )

        return "\n".join(
            lineas
        )

    for dato in resultado[
        "multiplicadores"
    ]:
        fila = dato[
            "fila"
        ] + 1

        columna_l = dato[
            "fila_pivote"
        ] + 1

        fila_pivote = dato[
            "fila_pivote"
        ] + 1

        columna_pivote = dato[
            "columna_pivote"
        ] + 1

        sub_fila = convertir_numero_subindice(
            fila
        )

        sub_columna_l = convertir_numero_subindice(
            columna_l
        )

        lineas.extend(
            [
                (
                    f"l{sub_fila}{sub_columna_l} = "
                    f"entrada a eliminar / pivote"
                ),
                (
                    f"l{sub_fila}{sub_columna_l} = "
                    f"{dato['elemento_eliminado']} / "
                    f"{dato['pivote']}"
                ),
                (
                    f"l{sub_fila}{sub_columna_l} = "
                    f"{dato['multiplicador']}"
                ),
                (
                    "Pivote usado: "
                    f"fila {fila_pivote}, columna {columna_pivote}"
                ),
                "",
            ]
        )

    return "\n".join(
        lineas
    )


def _formatear_pasos_reduccion(resultado):
    """Muestra cada reemplazo de fila utilizado para construir U."""
    lineas = [
        "REDUCCIÓN DE A HASTA U",
        "=" * 60,
        "",
        "A inicial =",
        "",
        formatear_matriz(
            resultado["matriz_a"]
        ),
        "",
    ]

    for numero, paso in enumerate(
        resultado["pasos"],
        start=1
    ):
        lineas.extend(
            [
                f"Paso {numero}",
                paso["operacion"],
                (
                    "Multiplicador guardado en L: "
                    + str(
                        paso["multiplicador"]
                    )
                ),
                "",
                "Matriz resultante =",
                "",
                formatear_matriz(
                    paso["matriz_despues"]
                ),
                "",
            ]
        )

    return "\n".join(
        lineas
    )


def formatear_factorizacion_lu(resultado):
    """Presenta el procedimiento completo de A = LU."""
    lineas = [
        "FACTORIZACIÓN LU",
        "A = L·U",
        "=" * 60,
        "",
        _formatear_pasos_reduccion(
            resultado
        ),
        "",
        _formatear_multiplicadores(
            resultado
        ),
        "",
        "=" * 60,
        "",
        "MATRIZ L",
        "",
        formatear_matriz(
            resultado["matriz_l"]
        ),
        "",
        "MATRIZ U",
        "",
        formatear_matriz(
            resultado["matriz_u"]
        ),
        "",
        "POSICIONES PIVOTE",
        "",
    ]

    if resultado["posiciones_pivote"]:
        for fila, columna in resultado[
            "posiciones_pivote"
        ]:
            lineas.append(
                f"({fila + 1}, {columna + 1})"
            )
    else:
        lineas.append(
            "No se encontraron posiciones pivote."
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
            "VERIFICACIÓN",
            "",
            "L·U =",
            "",
            formatear_matriz(
                resultado["producto_lu"]
            ),
            "",
            "A =",
            "",
            formatear_matriz(
                resultado["matriz_a"]
            ),
            "",
            (
                "L·U = A: "
                + _estado(
                    resultado["cumple_lu"]
                )
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def _formatear_terminos(terminos, letra):
    """Convierte una suma de productos triangulares en una expresión."""
    if not terminos:
        return "0"

    partes = []

    for termino in terminos:
        variable = _nombre(
            letra,
            termino["indice"]
        )

        partes.append(
            f"({termino['coeficiente']})({variable})"
        )

    return " + ".join(
        partes
    )


def formatear_sustitucion_adelante(resultado):
    """Presenta el procedimiento para resolver Ly = b."""
    pasos = resultado[
        "sustitucion_adelante"
    ][
        "pasos"
    ]

    lineas = [
        "SUSTITUCIÓN HACIA ADELANTE",
        "Ly = b",
        "=" * 60,
        "",
        "L =",
        "",
        formatear_matriz(
            resultado[
                "factorizacion"
            ][
                "matriz_l"
            ]
        ),
        "",
        "b =",
        "",
        formatear_vector(
            resultado["vector_b"]
        ),
        "",
    ]

    for paso in pasos:
        indice = paso[
            "indice"
        ]

        nombre_y = _nombre(
            "y",
            indice
        )

        expresion = _formatear_terminos(
            paso["terminos"],
            "y"
        )

        lineas.extend(
            [
                f"{nombre_y}:",
                (
                    f"{paso['diagonal']}({nombre_y}) + "
                    f"{expresion} = {paso['b']}"
                ),
                (
                    f"{nombre_y} = "
                    f"({paso['b']} - {paso['suma']}) "
                    f"/ {paso['diagonal']}"
                ),
                (
                    f"{nombre_y} = "
                    f"{paso['resultado']}"
                ),
                "",
            ]
        )

    lineas.extend(
        [
            "y =",
            "",
            formatear_vector(
                resultado["vector_y"]
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_sustitucion_atras(resultado):
    """Presenta el procedimiento para resolver Ux = y."""
    pasos = resultado[
        "sustitucion_atras"
    ][
        "pasos"
    ]

    lineas = [
        "SUSTITUCIÓN HACIA ATRÁS",
        "Ux = y",
        "=" * 60,
        "",
        "U =",
        "",
        formatear_matriz(
            resultado[
                "factorizacion"
            ][
                "matriz_u"
            ]
        ),
        "",
        "y =",
        "",
        formatear_vector(
            resultado["vector_y"]
        ),
        "",
    ]

    for paso in pasos:
        indice = paso[
            "indice"
        ]

        nombre_x = _nombre(
            "x",
            indice
        )

        expresion = _formatear_terminos(
            paso["terminos"],
            "x"
        )

        lineas.extend(
            [
                f"{nombre_x}:",
                (
                    f"{paso['diagonal']}({nombre_x}) + "
                    f"{expresion} = {paso['y']}"
                ),
                (
                    f"{nombre_x} = "
                    f"({paso['y']} - {paso['suma']}) "
                    f"/ {paso['diagonal']}"
                ),
                (
                    f"{nombre_x} = "
                    f"{paso['resultado']}"
                ),
                "",
            ]
        )

    lineas.extend(
        [
            "x =",
            "",
            formatear_vector(
                resultado["vector_x"]
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_verificaciones_lu(resultado):
    """Muestra L·U=A y A·x=b utilizando los resultados ya obtenidos."""
    lineas = [
        "VERIFICACIÓN DE RESULTADOS",
        "=" * 60,
        "",
        "1. COMPROBACIÓN DE LA FACTORIZACIÓN",
        "",
        "L·U =",
        "",
        formatear_matriz(
            resultado[
                "factorizacion"
            ][
                "producto_lu"
            ]
        ),
        "",
        "A =",
        "",
        formatear_matriz(
            resultado["matriz_a"]
        ),
        "",
        (
            "L·U = A: "
            + _estado(
                resultado["cumple_lu"]
            )
        ),
        "",
        "=" * 60,
        "",
        "2. COMPROBACIÓN DE LA SOLUCIÓN",
        "",
        "A·x =",
        "",
        formatear_vector(
            resultado["producto_ax"]
        ),
        "",
        "b =",
        "",
        formatear_vector(
            resultado["vector_b"]
        ),
        "",
        (
            "A·x = b: "
            + _estado(
                resultado["cumple_ax_b"]
            )
        ),
    ]

    return "\n".join(
        lineas
    )


def formatear_resolucion_lu(resultado):
    """Une factorización, ambas sustituciones y verificaciones."""
    return (
        formatear_factorizacion_lu(
            resultado["factorizacion"]
        )
        + "\n\n"
        + "=" * 60
        + "\n\n"
        + formatear_sustitucion_adelante(
            resultado
        )
        + "\n\n"
        + "=" * 60
        + "\n\n"
        + formatear_sustitucion_atras(
            resultado
        )
        + "\n\n"
        + "=" * 60
        + "\n\n"
        + formatear_verificaciones_lu(
            resultado
        )
    )
