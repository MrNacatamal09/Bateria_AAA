"""
Da formato al Análisis Matricial Integrado del Módulo IV.
Organiza determinante, Cᵢⱼ, adjunta, inversa, verificación y propiedades.
Tema de clase: determinantes, matriz adjunta e invertibilidad.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_determinantes import (
    formatear_matriz,
    formatear_procedimiento_determinante,
    formatear_sarrus,
)

from utilidades.formato_cofactores import (
    formatear_cofactores_detallados,
)

from utilidades.formato_inversa import (
    formatear_procedimiento_inversa,
)


def _estado(cumple):
    """Devuelve el texto de conclusión para una igualdad."""
    return (
        "Se cumple"
        if cumple
        else "No se cumple"
    )


def formatear_determinante_integrado(resultado):
    """Muestra det(A), el desarrollo y todos los Cᵢⱼ."""
    metodos = resultado[
        "metodos_determinante"
    ]

    lineas = [
        "ANÁLISIS MATRICIAL INTEGRADO",
        "DETERMINANTE, MENORES Y COFACTORES",
        "=" * 60,
        "",
        "MATRIZ A =",
        "",
        formatear_matriz(
            resultado["matriz_a"]
        ),
        "",
        "DESARROLLO POR COFACTORES",
        "=" * 60,
        "",
        formatear_procedimiento_determinante(
            metodos["cofactores"]
        ),
    ]

    if metodos["sarrus"] is not None:
        lineas.extend(
            [
                "",
                "=" * 60,
                "",
                "COMPROBACIÓN POR SARRUS",
                "",
                formatear_sarrus(
                    metodos["sarrus"]
                ),
            ]
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
            formatear_cofactores_detallados(
                resultado["cofactores"]
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_adjunta_inversa_integrada(resultado):
    """Muestra el encadenamiento C -> adj(A) -> A⁻¹."""
    lineas = [
        "ANÁLISIS MATRICIAL INTEGRADO",
        "MATRIZ ADJUNTA E INVERSA",
        "=" * 60,
        "",
        "Se reutiliza la matriz de cofactores obtenida anteriormente.",
        "",
        "MATRIZ DE COFACTORES C =",
        "",
        formatear_matriz(
            resultado["matriz_cofactores"]
        ),
        "",
        "adj(A) = Cᵀ",
        "",
        "adj(A) =",
        "",
        formatear_matriz(
            resultado["adjunta"]
        ),
        "",
        f"det(A) = {resultado['determinante_a']}",
        "",
    ]

    if resultado["inversa_adjunta"] is None:
        lineas.extend(
            [
                "A⁻¹ no existe porque det(A) = 0.",
                "",
                "La matriz es singular.",
            ]
        )

        return "\n".join(
            lineas
        )

    lineas.extend(
        [
            "A⁻¹ = (1/det(A)) adj(A)",
            "",
            (
                "A⁻¹ = ("
                + str(
                    resultado["factor_inversa"]
                )
                + ") adj(A)"
            ),
            "",
            "A⁻¹ =",
            "",
            formatear_matriz(
                resultado["inversa_adjunta"]
            ),
            "",
            "=" * 60,
            "",
            "VERIFICACIÓN DE LA INVERSA",
            "",
            "A · A⁻¹ =",
            "",
            formatear_matriz(
                resultado["verificacion_inversa"][
                    "producto_a_inversa"
                ]
            ),
            "",
            "A⁻¹ · A =",
            "",
            formatear_matriz(
                resultado["verificacion_inversa"][
                    "producto_inversa_a"
                ]
            ),
            "",
            "I =",
            "",
            formatear_matriz(
                resultado["verificacion_inversa"][
                    "identidad"
                ]
            ),
            "",
            _estado(
                resultado["verificacion_inversa"][
                    "cumple"
                ]
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_gauss_jordan_integrado(resultado):
    """Muestra Gauss-Jordan y contrasta su inversa con la adjunta."""
    lineas = [
        "ANÁLISIS MATRICIAL INTEGRADO",
        "CONTRASTE CON GAUSS-JORDAN",
        "=" * 60,
        "",
        formatear_procedimiento_inversa(
            resultado["gauss_jordan"]
        ),
        "",
        "=" * 60,
        "",
    ]

    if resultado["inversa_adjunta"] is None:
        lineas.extend(
            [
                "No hay inversa por adjunta para comparar.",
                "La matriz es singular.",
            ]
        )

        return "\n".join(
            lineas
        )

    lineas.extend(
        [
            "INVERSA POR MATRIZ ADJUNTA =",
            "",
            formatear_matriz(
                resultado["inversa_adjunta"]
            ),
            "",
            "INVERSA POR GAUSS-JORDAN =",
            "",
            formatear_matriz(
                resultado["gauss_jordan"]["inversa"]
            ),
            "",
            (
                "Ambos métodos producen la misma inversa: "
                + _estado(
                    resultado["comparacion_inversas"]
                )
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_propiedades_integradas(resultado):
    """Muestra las tres propiedades requeridas para determinantes e inversa."""
    transpuesta = resultado[
        "propiedad_transpuesta"
    ]

    producto = resultado[
        "propiedad_producto"
    ]

    lineas = [
        "ANÁLISIS MATRICIAL INTEGRADO",
        "COMPROBACIÓN DE PROPIEDADES",
        "=" * 60,
        "",
        "1. DETERMINANTE DE LA TRANSPUESTA",
        "det(Aᵀ) = det(A)",
        "",
        "Aᵀ =",
        "",
        formatear_matriz(
            transpuesta["transpuesta_a"]
        ),
        "",
        (
            "det(Aᵀ) = "
            + str(
                transpuesta[
                    "determinante_transpuesta"
                ]
            )
        ),
        (
            "det(A)  = "
            + str(
                transpuesta[
                    "determinante_a"
                ]
            )
        ),
        "",
        _estado(
            transpuesta["cumple"]
        ),
        "",
        "=" * 60,
        "",
        "2. DETERMINANTE DE UN PRODUCTO",
        "det(AB) = det(A) · det(B)",
        "",
        "B =",
        "",
        formatear_matriz(
            resultado["matriz_b"]
        ),
        "",
        "AB =",
        "",
        formatear_matriz(
            producto["producto_ab"]
        ),
        "",
        f"det(AB) = {producto['determinante_ab']}",
        f"det(A) = {producto['determinante_a']}",
        f"det(B) = {producto['determinante_b']}",
        (
            "det(A) · det(B) = "
            + str(
                producto[
                    "producto_determinantes"
                ]
            )
        ),
        "",
        _estado(
            producto["cumple"]
        ),
        "",
        "=" * 60,
        "",
        "3. DETERMINANTE DE LA INVERSA",
        "det(A⁻¹) = 1/det(A)",
        "",
    ]

    propiedad_inversa = resultado[
        "propiedad_inversa"
    ]

    if propiedad_inversa is None:
        lineas.extend(
            [
                "No se puede verificar porque A no tiene inversa.",
                "",
                "No se cumple la condición det(A) ≠ 0.",
            ]
        )
    else:
        lineas.extend(
            [
                (
                    "det(A⁻¹) = "
                    + str(
                        propiedad_inversa[
                            "determinante_inversa"
                        ]
                    )
                ),
                (
                    "1/det(A) = "
                    + str(
                        propiedad_inversa[
                            "reciproco_determinante"
                        ]
                    )
                ),
                "",
                _estado(
                    propiedad_inversa["cumple"]
                ),
            ]
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
            "JUSTIFICACIÓN DE INVERTIBILIDAD",
            "",
            resultado["diagnostico"]["texto"],
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_resumen_integrado(resultado):
    """Muestra un resumen compacto de todo el análisis."""
    lineas = [
        "ANÁLISIS MATRICIAL INTEGRADO",
        "RESUMEN GENERAL",
        "=" * 60,
        "",
        f"det(A) = {resultado['determinante_a']}",
        "",
        "Matriz de cofactores =",
        "",
        formatear_matriz(
            resultado["matriz_cofactores"]
        ),
        "",
        "adj(A) =",
        "",
        formatear_matriz(
            resultado["adjunta"]
        ),
        "",
    ]

    if resultado["inversa_adjunta"] is None:
        lineas.extend(
            [
                "A⁻¹ = No existe.",
                "",
                "A es singular.",
            ]
        )
    else:
        lineas.extend(
            [
                "A⁻¹ =",
                "",
                formatear_matriz(
                    resultado["inversa_adjunta"]
                ),
                "",
                (
                    "A · A⁻¹ = I: "
                    + _estado(
                        resultado[
                            "verificacion_inversa"
                        ]["cumple"]
                    )
                ),
                (
                    "Adjunta = Gauss-Jordan: "
                    + _estado(
                        resultado[
                            "comparacion_inversas"
                        ]
                    )
                ),
            ]
        )

    lineas.extend(
        [
            "",
            (
                "det(Aᵀ) = det(A): "
                + _estado(
                    resultado[
                        "propiedad_transpuesta"
                    ]["cumple"]
                )
            ),
            (
                "det(AB) = det(A)det(B): "
                + _estado(
                    resultado[
                        "propiedad_producto"
                    ]["cumple"]
                )
            ),
        ]
    )

    if resultado["propiedad_inversa"] is not None:
        lineas.append(
            "det(A⁻¹) = 1/det(A): "
            + _estado(
                resultado[
                    "propiedad_inversa"
                ]["cumple"]
            )
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
            "CONCLUSIÓN",
            "",
            resultado["diagnostico"]["texto"],
        ]
    )

    return "\n".join(
        lineas
    )
