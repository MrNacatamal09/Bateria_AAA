"""
Da formato al verificador consolidado del módulo de Factorización LU.
Muestra ambos miembros de cada propiedad y una conclusión individual.
Tema de clase: propiedades de matrices, inversas y determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def _formatear_matriz(matriz):
    """Convierte una matriz en texto alineado por filas."""
    return "\n".join(
        "[ "
        + "   ".join(
            str(valor)
            for valor in fila
        )
        + " ]"
        for fila in matriz
    )


def _formatear_valor(valor):
    """Da formato uniforme a matrices y escalares."""
    if (
        isinstance(
            valor,
            list
        )
        and valor
        and isinstance(
            valor[0],
            list
        )
    ):
        return _formatear_matriz(
            valor
        )

    return str(
        valor
    )


def _estado(propiedad):
    """Devuelve la conclusión textual de una propiedad."""
    if not propiedad[
        "aplicable"
    ]:
        return "No aplicable"

    return (
        "Se cumple"
        if propiedad[
            "cumple"
        ]
        else "No se cumple"
    )


def _formatear_propiedad(numero, propiedad):
    """Construye la salida de una propiedad individual."""
    lineas = [
        f"{numero}. {propiedad['nombre']}",
        propiedad["formula"],
        "-" * 60,
        "",
    ]

    if not propiedad[
        "aplicable"
    ]:
        lineas.extend(
            [
                "No aplicable.",
                "Razón: "
                + propiedad[
                    "razon"
                ],
                "",
                _estado(
                    propiedad
                ),
            ]
        )

        return "\n".join(
            lineas
        )

    if propiedad[
        "tipo"
    ] == "triple":
        lineas.extend(
            [
                "MIEMBRO 1 =",
                "",
                _formatear_valor(
                    propiedad[
                        "miembro_1"
                    ]
                ),
                "",
                "MIEMBRO 2 =",
                "",
                _formatear_valor(
                    propiedad[
                        "miembro_2"
                    ]
                ),
                "",
                "MIEMBRO 3 =",
                "",
                _formatear_valor(
                    propiedad[
                        "miembro_3"
                    ]
                ),
                "",
            ]
        )

    else:
        lineas.extend(
            [
                "MIEMBRO IZQUIERDO =",
                "",
                _formatear_valor(
                    propiedad[
                        "lado_izquierdo"
                    ]
                ),
                "",
                "MIEMBRO DERECHO =",
                "",
                _formatear_valor(
                    propiedad[
                        "lado_derecho"
                    ]
                ),
                "",
            ]
        )

    lineas.append(
        _estado(
            propiedad
        )
    )

    return "\n".join(
        lineas
    )


def formatear_propiedades_consolidadas(resultado):
    """Muestra todas las propiedades y el resumen global."""
    lineas = [
        "PROPIEDADES CONSOLIDADAS",
        "Matrices, Transpuesta, Inversa y Determinantes",
        "=" * 60,
        "",
        f"Escalar r = {resultado['escalar']}",
        "",
        (
            "Propiedades evaluadas: "
            + str(
                resultado["total"]
            )
        ),
        (
            "Propiedades aplicables: "
            + str(
                resultado["aplicables"]
            )
        ),
        (
            "Propiedades cumplidas: "
            + str(
                resultado["cumplidas"]
            )
        ),
        "",
        "=" * 60,
        "",
    ]

    for numero, propiedad in enumerate(
        resultado[
            "propiedades"
        ],
        start=1
    ):
        lineas.append(
            _formatear_propiedad(
                numero,
                propiedad
            )
        )

        lineas.extend(
            [
                "",
                "=" * 60,
                "",
            ]
        )

    if resultado[
        "todas_cumplen"
    ]:
        lineas.append(
            "CONCLUSIÓN: Todas las propiedades aplicables se cumplen."
        )
    else:
        lineas.append(
            "CONCLUSIÓN: Existe al menos una propiedad aplicable que no se cumple."
        )

    return "\n".join(
        lineas
    )
