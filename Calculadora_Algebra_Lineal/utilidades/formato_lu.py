"""
Da formato al procedimiento de factorización LU y resolución de Ax = b.
Muestra L, U y las reducciones [L|b] e [U|y] usando Gauss-Jordan.
Tema de clase: factorización LU, reducción y encadenamiento de resultados.
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


def formatear_matriz_aumentada(
    matriz,
    columnas_coeficientes,
):
    """Muestra una matriz aumentada separando coeficientes y resultado."""
    lineas = []

    for fila in matriz:
        izquierda = "   ".join(
            str(valor)
            for valor in fila[
                :columnas_coeficientes
            ]
        )

        derecha = "   ".join(
            str(valor)
            for valor in fila[
                columnas_coeficientes:
            ]
        )

        lineas.append(
            f"[ {izquierda} | {derecha} ]"
        )

    return "\n".join(
        lineas
    )


def formatear_vector(vector):
    """Convierte un vector en formato columna."""
    return "\n".join(
        f"[ {valor} ]"
        for valor in vector
    )


def _nombre(letra, indice):
    """Construye nombres como y₁, y₂, x₁ y x₂."""
    return (
        letra
        + convertir_numero_subindice(
            indice + 1
        )
    )


def _formatear_componentes_vector(
    vector,
    letra,
):
    """Muestra cada componente del vector con subíndice."""
    return "\n".join(
        f"{_nombre(letra, indice)} = {valor}"
        for indice, valor in enumerate(
            vector
        )
    )


def _formatear_multiplicadores(resultado):
    """Muestra cómo se obtiene cada entrada inferior de L."""
    lineas = [
        "MULTIPLICADORES DURANTE LA ELIMINACIÓN",
        "=" * 60,
        "",
    ]

    if resultado.get("permutaciones"):
        lineas.extend([
            "Los índices corresponden al paso en que se calcularon. "
            "Un intercambio posterior mueve en L los multiplicadores "
            "de columnas anteriores; consulte la matriz L final.",
            "",
        ])

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

        sub_columna = convertir_numero_subindice(
            columna_l
        )

        lineas.extend(
            [
                (
                    f"l{sub_fila}{sub_columna} = "
                    "elemento a eliminar / pivote"
                ),
                (
                    f"l{sub_fila}{sub_columna} = "
                    f"{dato['elemento_eliminado']} / "
                    f"{dato['pivote']}"
                ),
                (
                    f"l{sub_fila}{sub_columna} = "
                    f"{dato['multiplicador']}"
                ),
                (
                    "Pivote usado: "
                    f"fila {fila_pivote}, "
                    f"columna {columna_pivote}"
                ),
                "",
            ]
        )

    return "\n".join(
        lineas
    )


def _formatear_pasos_reduccion(resultado):
    """Muestra intercambios y eliminaciones en su orden real."""
    operaciones = resultado.get("historial_operaciones", resultado["pasos"])
    lineas = [
        "PIVOTEO Y ELIMINACIÓN HASTA U",
        "=" * 60,
        "",
        "A inicial =",
        "",
        formatear_matriz(
            resultado["matriz_a"]
        ),
        "",
    ]

    if not operaciones:
        lineas.extend(
            [
                "No fueron necesarios intercambios ni reemplazos de filas.",
                "",
            ]
        )

    for numero, paso in enumerate(
        operaciones,
        start=1
    ):
        es_permutacion = paso.get("tipo") == "permutacion"
        lineas.extend(
            [
                f"Paso {numero}",
                paso["operacion"],
            ]
        )
        if es_permutacion:
            lineas.append("Se intercambian las mismas filas en U y P.")
            if paso.get("fila_pivote", 0) > 0:
                lineas.append(
                    "Se intercambian también los multiplicadores previos "
                    "de esas filas en L."
                )
        else:
            lineas.append(
                "Multiplicador registrado en L: "
                + str(paso["multiplicador"])
            )
        lineas.extend(
            [
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


def _formatear_historial_gauss_jordan(
    historial,
    columnas_coeficientes,
):
    """Convierte el historial de Gauss-Jordan en un procedimiento legible."""
    lineas = []

    for numero, paso in enumerate(
        historial,
        start=1
    ):
        lineas.extend(
            [
                f"Paso {numero}",
                paso["operacion"],
                "",
                formatear_matriz_aumentada(
                    paso["matriz"],
                    columnas_coeficientes,
                ),
            ]
        )

        verificada = paso.get(
            "verificada"
        )

        if verificada is not None:
            if verificada:
                estado = "correcta"
            else:
                estado = "incorrecta"

            lineas.extend(
                [
                    "",
                    (
                        "Verificación de la operación: "
                        + estado
                    ),
                ]
            )

        lineas.extend(
            [
                "",
                "-" * 60,
                "",
            ]
        )

    return "\n".join(
        lineas
    )


def formatear_factorizacion_lu(resultado):
    """Presenta A = LU o PA = LU según los intercambios realizados."""
    hubo_permutaciones = resultado.get("hubo_permutaciones", False)
    lineas = [
        "FACTORIZACIÓN LU",
        "P·A = L·U" if hubo_permutaciones else "A = L·U",
        "=" * 60,
        "",
        _formatear_pasos_reduccion(
            resultado
        ),
        "",
    ]

    if hubo_permutaciones:
        lineas.extend([
            "PERMUTACIONES REALIZADAS",
            "",
            *(
                f"F{fila_a + 1} ↔ F{fila_b + 1}"
                for fila_a, fila_b in resultado["permutaciones"]
            ),
            "",
            "MATRIZ P",
            "",
            formatear_matriz(resultado["matriz_p"]),
            "",
            "P·A =",
            "",
            formatear_matriz(resultado["producto_pa"]),
            "",
        ])
    else:
        lineas.extend([
            "No fue necesario realizar permutaciones.",
            "",
        ])

    lineas.extend([
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
    ])

    if resultado[
        "posiciones_pivote"
    ]:
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

    lineas.extend([
        "",
        "=" * 60,
        "",
        "VERIFICACIÓN DE LA FACTORIZACIÓN",
        "",
        "L·U =",
        "",
        formatear_matriz(resultado["producto_lu"]),
        "",
        "P·A =" if hubo_permutaciones else "A =",
        "",
        formatear_matriz(
            resultado["producto_pa"] if hubo_permutaciones
            else resultado["matriz_a"]
        ),
        "",
    ])

    if resultado[
        "cumple_lu"
    ]:
        lineas.append(
            "La factorización es correcta: P·A = L·U."
            if hubo_permutaciones else
            "La factorización es correcta: L·U = A."
        )

    else:
        lineas.append(
            "La factorización no es correcta: P·A ≠ L·U."
            if hubo_permutaciones else
            "La factorización no es correcta: L·U ≠ A."
        )

    return "\n".join(
        lineas
    )


def formatear_sustitucion_adelante(resultado):
    """Muestra la reducción de [L|Pb] utilizada para obtener y."""
    datos = resultado[
        "sustitucion_adelante"
    ]

    matriz_l = resultado[
        "factorizacion"
    ][
        "matriz_l"
    ]

    orden = len(
        matriz_l
    )

    hubo_permutaciones = resultado["factorizacion"].get(
        "hubo_permutaciones", False
    )
    vector_pb = resultado.get("vector_pb", resultado["vector_b"])

    lineas = [
        "SUSTITUCIÓN HACIA ADELANTE",
        (
            "Resolver Ly = Pb mediante reducción de [L|Pb]"
            if hubo_permutaciones else
            "Resolver Ly = b mediante reducción de [L|b]"
        ),
        "=" * 60,
        "",
        "L =",
        "",
        formatear_matriz(
            matriz_l
        ),
        "",
        "b =",
        "",
        formatear_vector(
            resultado[
                "vector_b"
            ]
        ),
        "",
    ]

    if hubo_permutaciones:
        lineas.extend([
            "P =",
            "",
            formatear_matriz(resultado["factorizacion"]["matriz_p"]),
            "",
            "Pb =",
            "",
            formatear_vector(vector_pb),
            "",
        ])

    lineas.extend([
        "Matriz aumentada inicial [L|Pb] =" if hubo_permutaciones
        else "Matriz aumentada inicial [L|b] =",
        "",
        formatear_matriz_aumentada(
            datos[
                "matriz_aumentada"
            ],
            orden,
        ),
        "",
        "=" * 60,
        "",
        "PROCEDIMIENTO DE GAUSS-JORDAN",
        "",
        _formatear_historial_gauss_jordan(
            datos[
                "historial"
            ],
            orden,
        ),
        "Matriz reducida [I|y] =",
        "",
        formatear_matriz_aumentada(
            datos[
                "matriz_reducida"
            ],
            orden,
        ),
        "",
        "VECTOR INTERMEDIO y",
        "",
        formatear_vector(
            resultado[
                "vector_y"
            ]
        ),
        "",
        _formatear_componentes_vector(
            resultado[
                "vector_y"
            ],
            "y",
        ),
    ])

    return "\n".join(
        lineas
    )


def formatear_sustitucion_atras(resultado):
    """Muestra la reducción de [U|y] utilizada para obtener x."""
    datos = resultado[
        "sustitucion_atras"
    ]

    matriz_u = resultado[
        "factorizacion"
    ][
        "matriz_u"
    ]

    orden = len(
        matriz_u
    )

    lineas = [
        "SUSTITUCIÓN HACIA ATRÁS",
        "Resolver Ux = y mediante reducción de [U|y]",
        "=" * 60,
        "",
        "U =",
        "",
        formatear_matriz(
            matriz_u
        ),
        "",
        "y =",
        "",
        formatear_vector(
            resultado[
                "vector_y"
            ]
        ),
        "",
        "Matriz aumentada inicial [U|y] =",
        "",
        formatear_matriz_aumentada(
            datos[
                "matriz_aumentada"
            ],
            orden,
        ),
        "",
        "=" * 60,
        "",
        "PROCEDIMIENTO DE GAUSS-JORDAN",
        "",
        _formatear_historial_gauss_jordan(
            datos[
                "historial"
            ],
            orden,
        ),
        "Matriz reducida [I|x] =",
        "",
        formatear_matriz_aumentada(
            datos[
                "matriz_reducida"
            ],
            orden,
        ),
        "",
        "VECTOR SOLUCIÓN x",
        "",
        formatear_vector(
            resultado[
                "vector_x"
            ]
        ),
        "",
        _formatear_componentes_vector(
            resultado[
                "vector_x"
            ],
            "x",
        ),
    ]

    return "\n".join(
        lineas
    )


def formatear_verificaciones_lu(resultado):
    """Muestra P·A=L·U o A=L·U y siempre A·x=b."""
    hubo_permutaciones = resultado["factorizacion"].get(
        "hubo_permutaciones", False
    )
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
        "P·A =" if hubo_permutaciones else "A =",
        "",
        formatear_matriz(
            resultado[
                "matriz_a"
            ] if not hubo_permutaciones else resultado[
                "factorizacion"
            ]["producto_pa"]
        ),
        "",
    ]

    if resultado[
        "cumple_lu"
    ]:
        lineas.append(
            "La factorización es correcta: P·A = L·U."
            if hubo_permutaciones else
            "La factorización es correcta: L·U = A."
        )

    else:
        lineas.append(
            "La factorización no es correcta: P·A ≠ L·U."
            if hubo_permutaciones else
            "La factorización no es correcta: L·U ≠ A."
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
            "2. COMPROBACIÓN DE LA SOLUCIÓN",
            "",
            "A·x =",
            "",
            formatear_vector(
                resultado[
                    "producto_ax"
                ]
            ),
            "",
            "b =",
            "",
            formatear_vector(
                resultado[
                    "vector_b"
                ]
            ),
            "",
        ]
    )

    if resultado[
        "cumple_ax_b"
    ]:
        lineas.append(
            "Comprobación exitosa: A · x == b."
        )

    else:
        lineas.append(
            "La comprobación no coincide: A · x != b."
        )

    return "\n".join(
        lineas
    )


def formatear_reconstruccion_lu(resultado):
    """Presenta la reconstrucción de A a partir de L, U y P opcional."""
    matriz_p = resultado["matriz_p"]
    lineas = [
        "RECONSTRUCCIÓN DE A",
        "A = Pᵀ·L·U" if matriz_p is not None else "A = L·U",
        "=" * 60,
        "",
    ]

    if matriz_p is not None:
        lineas.extend([
            "P =",
            "",
            formatear_matriz(matriz_p),
            "",
        ])

    lineas.extend([
        "L =",
        "",
        formatear_matriz(resultado["matriz_l"]),
        "",
        "U =",
        "",
        formatear_matriz(resultado["matriz_u"]),
        "",
    ])

    if matriz_p is not None:
        lineas.extend([
            "Pᵀ =",
            "",
            formatear_matriz(resultado["matriz_p_transpuesta"]),
            "",
        ])

    lineas.extend([
        "L·U =",
        "",
        formatear_matriz(resultado["producto_lu"]),
        "",
        "A reconstruida = Pᵀ·L·U =" if matriz_p is not None
        else "A reconstruida = L·U =",
        "",
        formatear_matriz(resultado["matriz_a"]),
    ])

    if matriz_p is not None:
        lineas.extend([
            "",
            "VERIFICACIÓN",
            "",
            "P·A =",
            "",
            formatear_matriz(resultado["producto_pa"]),
            "",
            "L·U =",
            "",
            formatear_matriz(resultado["producto_lu"]),
            "",
            "La reconstrucción es correcta: P·A = L·U."
            if resultado["cumple_lu"] else
            "La reconstrucción no cumple P·A = L·U.",
        ])

    return "\n".join(lineas)


def formatear_resolucion_lu(resultado):
    """Une factorización, reducciones y verificaciones en una sola salida."""
    return (
        formatear_factorizacion_lu(
            resultado[
                "factorizacion"
            ]
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
