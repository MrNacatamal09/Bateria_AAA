"""
Da formato al verificador consolidado y a sus resultados filtrados.
Conserva la numeración original y muestra ambos miembros de cada igualdad.
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
    """Da formato uniforme a matrices, vectores y escalares."""
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

    if isinstance(
        valor,
        list
    ):
        return "\n".join(
            f"[ {elemento} ]"
            for elemento in valor
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


def _formatear_propiedad(
    propiedad,
    numero_alternativo,
):
    """Construye la salida de una propiedad individual."""
    numero = propiedad.get(
        "numero",
        numero_alternativo,
    )

    categoria = propiedad.get(
        "categoria"
    )

    lineas = [
        f"{numero}. {propiedad['nombre']}",
    ]

    if categoria:
        lineas.append(
            f"Categoría: {categoria}"
        )

    lineas.extend(
        [
            propiedad[
                "formula"
            ],
            "-" * 60,
            "",
        ]
    )

    if not propiedad[
        "aplicable"
    ]:
        lineas.extend(
            [
                "No aplicable.",
                (
                    "Razón: "
                    + propiedad[
                        "razon"
                    ]
                ),
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


def _contar_resultados(propiedades):
    """Cuenta propiedades aplicables y cumplidas dentro de una selección."""
    aplicables = [
        propiedad
        for propiedad in propiedades
        if propiedad[
            "aplicable"
        ]
    ]

    cumplidas = [
        propiedad
        for propiedad in aplicables
        if propiedad[
            "cumple"
        ]
    ]

    return (
        len(aplicables),
        len(cumplidas),
    )


def _conclusion_propiedades(
    propiedades,
    aplicables,
    cumplidas,
):
    """Construye una conclusión para la selección mostrada."""
    if not propiedades:
        return (
            "No se encontraron propiedades que coincidan "
            "con los criterios de búsqueda."
        )

    if aplicables == 0:
        return (
            "CONCLUSIÓN: Ninguna de las propiedades mostradas "
            "es aplicable con los datos ingresados."
        )

    if aplicables == cumplidas:
        return (
            "CONCLUSIÓN: Todas las propiedades aplicables "
            "mostradas se cumplen."
        )

    return (
        "CONCLUSIÓN: Existe al menos una propiedad aplicable "
        "mostrada que no se cumple."
    )


def formatear_propiedades_consolidadas(
    resultado,
    propiedades=None,
    criterio="",
):
    """Muestra todas las propiedades o una selección ya filtrada."""
    if propiedades is None:
        propiedades = resultado[
            "propiedades"
        ]

    propiedades = list(
        propiedades
    )

    aplicables_mostradas, cumplidas_mostradas = (
        _contar_resultados(
            propiedades
        )
    )

    total_general = resultado[
        "total"
    ]

    lineas = [
        "PROPIEDADES CONSOLIDADAS",
        "Matrices, Transpuesta, Inversa y Determinantes",
        "=" * 60,
        "",
        f"Escalar r = {resultado['escalar']}",
        "",
        (
            "Propiedades calculadas: "
            f"{total_general}"
        ),
        (
            "Resultados mostrados: "
            f"{len(propiedades)} de {total_general}"
        ),
        (
            "Aplicables mostradas: "
            f"{aplicables_mostradas}"
        ),
        (
            "Cumplidas mostradas: "
            f"{cumplidas_mostradas}"
        ),
    ]

    if criterio:
        lineas.extend(
            [
                "",
                (
                    "Filtro activo: "
                    f"{criterio}"
                ),
            ]
        )

    lineas.extend(
        [
            "",
            "=" * 60,
            "",
        ]
    )

    if not propiedades:
        lineas.extend(
            [
                "No se encontraron propiedades.",
                "",
                (
                    "Puede buscar por número, nombre, "
                    "fórmula o categoría."
                ),
                "",
                "=" * 60,
                "",
                _conclusion_propiedades(
                    propiedades,
                    aplicables_mostradas,
                    cumplidas_mostradas,
                ),
            ]
        )

        return "\n".join(
            lineas
        )

    for indice, propiedad in enumerate(
        propiedades,
        start=1,
    ):
        lineas.append(
            _formatear_propiedad(
                propiedad,
                indice,
            )
        )

        lineas.extend(
            [
                "",
                "=" * 60,
                "",
            ]
        )

    lineas.append(
        _conclusion_propiedades(
            propiedades,
            aplicables_mostradas,
            cumplidas_mostradas,
        )
    )

    return "\n".join(
        lineas
    )