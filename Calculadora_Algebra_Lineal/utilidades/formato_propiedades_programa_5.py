"""
Formatea los resultados del verificador de propiedades del Programa 5.
Muestra expresiones, ambos lados y la conclusión de cada igualdad.
Tema de clase: propiedades de matrices, inversas y determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_determinantes import formatear_matriz


def formatear_conclusion(cumple):
    """Devuelve la conclusión textual de una propiedad."""
    return "Se cumple" if cumple else "No se cumple"


def _agregar_matriz(lineas, titulo, matriz):
    """Agrega un título y una matriz formateada a una lista de líneas."""
    lineas.extend([
        titulo,
        "",
        formatear_matriz(matriz),
        "",
    ])


def formatear_propiedad_1(resultado):
    """Formatea (A⁻¹)⁻¹ = A."""
    lineas = [
        "PROPIEDAD 1",
        "(A⁻¹)⁻¹ = A",
        "=" * 60,
        "",
        "LADO IZQUIERDO",
        "",
    ]

    _agregar_matriz(
        lineas,
        "(A⁻¹)⁻¹ =",
        resultado["lado_izquierdo"],
    )

    lineas.extend([
        "LADO DERECHO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "A =",
        resultado["lado_derecho"],
    )

    lineas.append(
        formatear_conclusion(
            resultado["cumple"]
        )
    )

    return "\n".join(
        lineas
    )


def formatear_propiedad_2(resultado):
    """Formatea (AB)⁻¹ = B⁻¹A⁻¹."""
    lineas = [
        "PROPIEDAD 2",
        "(AB)⁻¹ = B⁻¹A⁻¹",
        "=" * 60,
        "",
    ]

    _agregar_matriz(
        lineas,
        "AB =",
        resultado["producto_ab"],
    )

    lineas.extend([
        "LADO IZQUIERDO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "(AB)⁻¹ =",
        resultado["lado_izquierdo"],
    )

    lineas.extend([
        "LADO DERECHO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "B⁻¹A⁻¹ =",
        resultado["lado_derecho"],
    )

    lineas.append(
        formatear_conclusion(
            resultado["cumple"]
        )
    )

    return "\n".join(
        lineas
    )


def formatear_propiedad_3(resultado):
    """Formatea (Aᵀ)⁻¹ = (A⁻¹)ᵀ."""
    lineas = [
        "PROPIEDAD 3",
        "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
        "=" * 60,
        "",
    ]

    _agregar_matriz(
        lineas,
        "Aᵀ =",
        resultado["transpuesta_a"],
    )

    lineas.extend([
        "LADO IZQUIERDO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "(Aᵀ)⁻¹ =",
        resultado["lado_izquierdo"],
    )

    lineas.extend([
        "LADO DERECHO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "(A⁻¹)ᵀ =",
        resultado["lado_derecho"],
    )

    lineas.append(
        formatear_conclusion(
            resultado["cumple"]
        )
    )

    return "\n".join(
        lineas
    )


def formatear_propiedad_4(resultado):
    """Formatea det(A⁻¹) = 1/det(A)."""
    lineas = [
        "PROPIEDAD 4",
        "det(A⁻¹) = 1/det(A)",
        "=" * 60,
        "",
    ]

    _agregar_matriz(
        lineas,
        "A⁻¹ =",
        resultado["inversa_a"],
    )

    lineas.extend([
        f"det(A) = {resultado['determinante_a']}",
        "",
        "LADO IZQUIERDO",
        f"det(A⁻¹) = {resultado['lado_izquierdo']}",
        "",
        "LADO DERECHO",
        f"1/det(A) = {resultado['lado_derecho']}",
        "",
        formatear_conclusion(
            resultado["cumple"]
        ),
    ])

    return "\n".join(
        lineas
    )


def _formatear_operacion_fila(
    titulo,
    bloque,
    det_original,
):
    """Formatea una verificación individual de la propiedad 5."""
    lineas = [
        titulo,
        "-" * 60,
        "",
        "Operación:",
        bloque["operacion"],
        "",
    ]

    _agregar_matriz(
        lineas,
        "Matriz resultante:",
        bloque["matriz"],
    )

    lineas.extend([
        f"det(A) original = {det_original}",
        (
            "Determinante obtenido = "
            f"{bloque['determinante_obtenido']}"
        ),
        (
            "Valor esperado = "
            f"{bloque['valor_esperado']}"
        ),
        "",
        formatear_conclusion(
            bloque["cumple"]
        ),
        "",
    ])

    return lineas


def formatear_propiedad_5(resultado):
    """Formatea las tres operaciones de fila de la propiedad 5."""
    lineas = [
        "PROPIEDAD 5",
        "DETERMINANTE Y OPERACIONES DE FILA",
        "=" * 60,
        "",
    ]

    det_original = resultado[
        "determinante_original"
    ]

    lineas += _formatear_operacion_fila(
        "A. Intercambio de dos filas",
        resultado["intercambio"],
        det_original,
    )

    lineas += _formatear_operacion_fila(
        "B. Reemplazo de una fila",
        resultado["reemplazo"],
        det_original,
    )

    lineas += _formatear_operacion_fila(
        "C. Multiplicación de una fila por k",
        resultado["escalamiento"],
        det_original,
    )

    lineas.extend([
        "=" * 60,
        (
            "Conclusión de la propiedad 5: "
            + formatear_conclusion(
                resultado["cumple"]
            )
        ),
    ])

    return "\n".join(
        lineas
    )


def formatear_propiedad_6(resultado):
    """Formatea la comparación del determinante triangular con cofactores."""
    lineas = [
        "PROPIEDAD 6",
        "DETERMINANTE DE UNA MATRIZ TRIANGULAR",
        "=" * 60,
        "",
    ]

    _agregar_matriz(
        lineas,
        "Matriz triangular obtenida:",
        resultado["matriz_triangular"],
    )

    lineas.extend([
        (
            "Producto de la diagonal = "
            f"{resultado['producto_diagonal']}"
        ),
        (
            "Intercambios de fila = "
            f"{resultado['intercambios']}"
        ),
        "",
        (
            "Determinante por cofactores = "
            f"{resultado['determinante_cofactores']}"
        ),
        (
            "Determinante triangular corregido = "
            f"{resultado['determinante_triangular']}"
        ),
        "",
        formatear_conclusion(
            resultado["cumple"]
        ),
    ])

    return "\n".join(
        lineas
    )


def formatear_propiedad_7(resultado):
    """Formatea A·A⁻¹ = I = A⁻¹·A."""
    lineas = [
        "PROPIEDAD 7",
        "IDENTIDAD DE LA MATRIZ INVERSA",
        "A·A⁻¹ = I = A⁻¹·A",
        "=" * 60,
        "",
    ]

    _agregar_matriz(
        lineas,
        "A⁻¹ =",
        resultado["inversa_a"],
    )

    lineas.extend([
        "PRIMER MIEMBRO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "A·A⁻¹ =",
        resultado[
            "producto_a_inversa"
        ],
    )

    lineas.extend([
        "MATRIZ IDENTIDAD",
        "",
    ])

    _agregar_matriz(
        lineas,
        "I =",
        resultado["identidad"],
    )

    lineas.extend([
        "TERCER MIEMBRO",
        "",
    ])

    _agregar_matriz(
        lineas,
        "A⁻¹·A =",
        resultado[
            "producto_inversa_a"
        ],
    )

    lineas.extend([
        (
            "A·A⁻¹ = I: "
            + formatear_conclusion(
                resultado[
                    "verifica_a_inversa"
                ]
            )
        ),
        (
            "A⁻¹·A = I: "
            + formatear_conclusion(
                resultado[
                    "verifica_inversa_a"
                ]
            )
        ),
        "",
        (
            "Conclusión de la propiedad 7: "
            + formatear_conclusion(
                resultado["cumple"]
            )
        ),
    ])

    return "\n".join(
        lineas
    )


def formatear_propiedad(
    numero,
    resultado,
):
    """Selecciona el formato correspondiente a la propiedad 1 a 7."""
    formateadores = {
        1: formatear_propiedad_1,
        2: formatear_propiedad_2,
        3: formatear_propiedad_3,
        4: formatear_propiedad_4,
        5: formatear_propiedad_5,
        6: formatear_propiedad_6,
        7: formatear_propiedad_7,
    }

    if numero not in formateadores:
        raise ValueError(
            "La propiedad seleccionada debe estar entre 1 y 7."
        )

    return formateadores[
        numero
    ](
        resultado
    )