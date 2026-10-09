"""
Da formato al procedimiento detallado de cada cofactor Cᵢⱼ.
Muestra el menor, su determinante, el signo y el resultado del cofactor.
Tema de clase: determinantes, cofactores y matriz adjunta.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_determinantes import formatear_matriz
from utilidades.formato_interfaz import convertir_numero_subindice


def _subindice(fila, columna):
    """Convierte una posición de Python al subíndice matemático i,j."""
    return (
        convertir_numero_subindice(fila + 1)
        + convertir_numero_subindice(columna + 1)
    )


def _formatear_menor(detalle):
    """Muestra el menor Mᵢⱼ y el cálculo de su determinante."""
    posicion = _subindice(
        detalle["fila"],
        detalle["columna"]
    )

    menor = detalle[
        "menor"
    ]

    lineas = [
        f"M{posicion} =",
        "",
    ]

    if menor:
        lineas.append(
            formatear_matriz(menor)
        )
    else:
        lineas.append(
            "[ menor vacío ]"
        )

    lineas.extend(
        [
            "",
            f"det(M{posicion}) =",
        ]
    )

    tipo = detalle[
        "detalle_determinante_menor"
    ]["tipo"]

    if tipo == "2x2":
        datos = detalle[
            "detalle_determinante_menor"
        ]

        lineas.extend(
            [
                (
                    f"({datos['a']})({datos['d']}) "
                    f"- ({datos['b']})({datos['c']})"
                ),
                (
                    f"{datos['producto_1']} "
                    f"- {datos['producto_2']}"
                ),
                str(
                    detalle["determinante_menor"]
                ),
            ]
        )

    elif tipo == "1x1":
        lineas.append(
            str(
                detalle["determinante_menor"]
            )
        )

    elif tipo == "vacio":
        lineas.append(
            "1"
        )

    else:
        lineas.extend(
            [
                "Se calcula con el método general de determinantes.",
                str(
                    detalle["determinante_menor"]
                ),
            ]
        )

    return lineas


def _formatear_un_cofactor(detalle):
    """Genera el desarrollo completo de un solo Cᵢⱼ."""
    fila = detalle[
        "fila"
    ]
    columna = detalle[
        "columna"
    ]

    posicion = _subindice(
        fila,
        columna
    )

    lineas = [
        f"COFACTOR C{posicion}",
        "-" * 60,
        "",
    ]

    lineas.extend(
        _formatear_menor(
            detalle
        )
    )

    lineas.extend(
        [
            "",
            "Signo del cofactor:",
            (
                f"(-1)^({fila + 1}+{columna + 1}) "
                f"= (-1)^{detalle['exponente']} "
                f"= {detalle['signo']}"
            ),
            "",
            (
                f"C{posicion} = "
                f"(-1)^({fila + 1}+{columna + 1}) "
                f"det(M{posicion})"
            ),
            (
                f"C{posicion} = "
                f"({detalle['signo']})"
                f"({detalle['determinante_menor']})"
            ),
            (
                f"C{posicion} = "
                f"{detalle['cofactor']}"
            ),
        ]
    )

    return "\n".join(
        lineas
    )


def formatear_cofactores_detallados(resultado):
    """Muestra todos los Cᵢⱼ y la matriz de cofactores resultante."""
    lineas = [
        "CÁLCULO DETALLADO DE LOS COFACTORES Cᵢⱼ",
        "=" * 60,
        "",
        "Para cada posición se usa:",
        "",
        "Cᵢⱼ = (-1)^(i+j) det(Mᵢⱼ)",
        "",
        "=" * 60,
        "",
    ]

    for detalle in resultado[
        "detalles"
    ]:
        lineas.append(
            _formatear_un_cofactor(
                detalle
            )
        )
        lineas.extend(
            [
                "",
                "=" * 60,
                "",
            ]
        )

    lineas.extend(
        [
            "MATRIZ DE COFACTORES C =",
            "",
            formatear_matriz(
                resultado[
                    "matriz_cofactores"
                ]
            ),
        ]
    )

    return "\n".join(
        lineas
    )
