"""
Consolida propiedades de matrices, transpuesta, inversa y determinantes.
Recibe A, B, C y r una sola vez y permite filtrar resultados ya calculados.
Tema de clase: propiedades matriciales y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction
import unicodedata

from modulos.modulo_matrices import (
    sumar,
    multiplicar_por_escalar,
    producto_matricial,
    transponer,
    crear_identidad,
    matrices_son_iguales,
)

from modulos.modulo_determinantes import (
    determinante,
    inversa_gauss_jordan,
    verificar_propiedad_5,
    verificar_propiedad_6,
)


CATEGORIAS_PROPIEDADES = (
    "Todas",
    "Operaciones matriciales",
    "Transposición",
    "Matriz inversa",
    "Determinantes",
    "Operaciones de fila",
    "Matriz triangular",
)


CATEGORIA_POR_NOMBRE = {
    "Asociativa del producto": "Operaciones matriciales",
    "Distributiva izquierda": "Operaciones matriciales",
    "Distributiva derecha": "Operaciones matriciales",
    "Compatibilidad con escalar": "Operaciones matriciales",
    "Identidad multiplicativa": "Operaciones matriciales",

    "Transpuesta doble": "Transposición",
    "Transpuesta de una suma": "Transposición",
    "Transpuesta de un múltiplo": "Transposición",
    "Transpuesta de un producto": "Transposición",
    "Distributiva de escalar y transpuesta": "Transposición",

    "Inversa de la inversa": "Matriz inversa",
    "Inversa de la transpuesta": "Matriz inversa",
    "Identidad de la inversa": "Matriz inversa",
    "Inversa de un producto": "Matriz inversa",

    "Determinante de la transpuesta": "Determinantes",
    "Determinante de un producto": "Determinantes",
    "Determinante de la inversa": "Determinantes",
    "Determinante de un múltiplo": "Determinantes",

    "Intercambio de filas": "Operaciones de fila",
    "Reemplazo de fila": "Operaciones de fila",
    "Escalamiento de una fila": "Operaciones de fila",

    "Determinante de una matriz triangular": "Matriz triangular",
}


def _validar_matrices_cuadradas_mismo_orden(
    matriz_a,
    matriz_b,
    matriz_c,
):
    """Valida que A, B y C sean cuadradas y tengan el mismo orden."""
    matrices = {
        "A": matriz_a,
        "B": matriz_b,
        "C": matriz_c,
    }

    if not matriz_a or not matriz_a[0]:
        raise ValueError(
            "Las matrices no pueden estar vacías."
        )

    orden = len(
        matriz_a
    )

    for nombre, matriz in matrices.items():
        if not matriz or not matriz[0]:
            raise ValueError(
                f"La matriz {nombre} no puede estar vacía."
            )

        if len(matriz) != len(matriz[0]):
            raise ValueError(
                f"La matriz {nombre} debe ser cuadrada."
            )

        if len(matriz) != orden:
            raise ValueError(
                "A, B y C deben tener el mismo orden."
            )


def _resultado_doble(
    nombre,
    formula,
    lado_izquierdo,
    lado_derecho,
):
    """Construye el resultado de una igualdad con dos miembros."""
    if (
        isinstance(lado_izquierdo, list)
        and isinstance(lado_derecho, list)
    ):
        cumple = matrices_son_iguales(
            lado_izquierdo,
            lado_derecho,
        )

    else:
        cumple = (
            lado_izquierdo
            == lado_derecho
        )

    return {
        "nombre": nombre,
        "formula": formula,
        "tipo": "doble",
        "aplicable": True,
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "cumple": cumple,
    }


def _resultado_triple(
    nombre,
    formula,
    miembro_1,
    miembro_2,
    miembro_3,
):
    """Construye el resultado de una igualdad con tres miembros."""
    if all(
        isinstance(miembro, list)
        for miembro in (
            miembro_1,
            miembro_2,
            miembro_3,
        )
    ):
        cumple = (
            matrices_son_iguales(
                miembro_1,
                miembro_2,
            )
            and matrices_son_iguales(
                miembro_2,
                miembro_3,
            )
        )

    else:
        cumple = (
            miembro_1 == miembro_2
            and miembro_2 == miembro_3
        )

    return {
        "nombre": nombre,
        "formula": formula,
        "tipo": "triple",
        "aplicable": True,
        "miembro_1": miembro_1,
        "miembro_2": miembro_2,
        "miembro_3": miembro_3,
        "cumple": cumple,
    }


def _resultado_no_aplicable(
    nombre,
    formula,
    razon,
):
    """Representa una propiedad cuya hipótesis matemática no se cumple."""
    return {
        "nombre": nombre,
        "formula": formula,
        "tipo": "no_aplicable",
        "aplicable": False,
        "razon": razon,
        "cumple": None,
    }


def _obtener_inversa(matriz):
    """Devuelve la inversa de una matriz o None cuando es singular."""
    resultado = inversa_gauss_jordan(
        matriz
    )

    if not resultado[
        "es_invertible"
    ]:
        return None

    return resultado[
        "inversa"
    ]


def _agregar_propiedades_inversa(
    propiedades,
    matriz_a,
    matriz_b,
    producto_ab,
    transpuesta_a,
    identidad,
):
    """Agrega las propiedades obligatorias relacionadas con la inversa."""
    inversa_a = _obtener_inversa(
        matriz_a
    )

    inversa_b = _obtener_inversa(
        matriz_b
    )

    if inversa_a is None:
        propiedades.extend(
            [
                _resultado_no_aplicable(
                    "Inversa de la inversa",
                    "(A⁻¹)⁻¹ = A",
                    "A es singular.",
                ),
                _resultado_no_aplicable(
                    "Inversa de la transpuesta",
                    "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
                    "A es singular.",
                ),
                _resultado_no_aplicable(
                    "Identidad de la inversa",
                    "A·A⁻¹ = I = A⁻¹·A",
                    "A es singular.",
                ),
            ]
        )

    else:
        inversa_inversa = _obtener_inversa(
            inversa_a
        )

        inversa_transpuesta = _obtener_inversa(
            transpuesta_a
        )

        propiedades.append(
            _resultado_doble(
                "Inversa de la inversa",
                "(A⁻¹)⁻¹ = A",
                inversa_inversa,
                matriz_a,
            )
        )

        propiedades.append(
            _resultado_doble(
                "Inversa de la transpuesta",
                "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
                inversa_transpuesta,
                transponer(
                    inversa_a
                ),
            )
        )

        producto_a_inversa = producto_matricial(
            matriz_a,
            inversa_a,
        )

        producto_inversa_a = producto_matricial(
            inversa_a,
            matriz_a,
        )

        propiedades.append(
            _resultado_triple(
                "Identidad de la inversa",
                "A·A⁻¹ = I = A⁻¹·A",
                producto_a_inversa,
                identidad,
                producto_inversa_a,
            )
        )

    if inversa_a is None or inversa_b is None:
        propiedades.append(
            _resultado_no_aplicable(
                "Inversa de un producto",
                "(AB)⁻¹ = B⁻¹A⁻¹",
                "A y B deben ser invertibles.",
            )
        )

    else:
        propiedades.append(
            _resultado_doble(
                "Inversa de un producto",
                "(AB)⁻¹ = B⁻¹A⁻¹",
                _obtener_inversa(
                    producto_ab
                ),
                producto_matricial(
                    inversa_b,
                    inversa_a,
                ),
            )
        )

    return inversa_a


def _agregar_propiedades_filas(
    propiedades,
    matriz_a,
    escalar,
):
    """Reutiliza el verificador de operaciones de fila del Módulo IV."""
    orden = len(
        matriz_a
    )

    if orden < 2:
        razon = (
            "Se necesita una matriz de orden mínimo 2."
        )

        propiedades.extend(
            [
                _resultado_no_aplicable(
                    "Intercambio de filas",
                    "det(F₁ ↔ F₂) = -det(A)",
                    razon,
                ),
                _resultado_no_aplicable(
                    "Reemplazo de fila",
                    "det(F₂ → F₂ + rF₁) = det(A)",
                    razon,
                ),
                _resultado_no_aplicable(
                    "Escalamiento de una fila",
                    "det(F₁ → rF₁) = r·det(A)",
                    razon,
                ),
            ]
        )

        return

    if escalar == 0:
        escalar_fila = Fraction(1)

    else:
        escalar_fila = escalar

    resultado = verificar_propiedad_5(
        matriz_a,
        0,
        1,
        escalar,
        0,
        escalar_fila,
    )

    propiedades.append(
        _resultado_doble(
            "Intercambio de filas",
            "det(F₁ ↔ F₂) = -det(A)",
            resultado[
                "intercambio"
            ][
                "determinante_obtenido"
            ],
            resultado[
                "intercambio"
            ][
                "valor_esperado"
            ],
        )
    )

    propiedades.append(
        _resultado_doble(
            "Reemplazo de fila",
            "det(F₂ → F₂ + rF₁) = det(A)",
            resultado[
                "reemplazo"
            ][
                "determinante_obtenido"
            ],
            resultado[
                "reemplazo"
            ][
                "valor_esperado"
            ],
        )
    )

    formula_escalamiento = (
        "det(F₁ → rF₁) = r·det(A)"
        if escalar != 0
        else "det(F₁ → 1F₁) = 1·det(A)"
    )

    propiedades.append(
        _resultado_doble(
            "Escalamiento de una fila",
            formula_escalamiento,
            resultado[
                "escalamiento"
            ][
                "determinante_obtenido"
            ],
            resultado[
                "escalamiento"
            ][
                "valor_esperado"
            ],
        )
    )


def _asignar_metadatos(propiedades):
    """Añade número y categoría a cada propiedad ya calculada."""
    for numero, propiedad in enumerate(
        propiedades,
        start=1,
    ):
        propiedad[
            "numero"
        ] = numero

        propiedad[
            "categoria"
        ] = CATEGORIA_POR_NOMBRE.get(
            propiedad[
                "nombre"
            ],
            "Otras",
        )


def _normalizar_busqueda(texto):
    """Normaliza texto y notación para permitir búsquedas flexibles."""
    texto = str(
        texto
    ).strip().lower()

    texto = texto.replace(
        "⁻¹",
        "^-1",
    )

    texto = texto.replace(
        "ᵀ",
        "^t",
    )

    texto = texto.replace(
        "ⁿ",
        "^n",
    )

    texto = texto.replace(
        "·",
        "*",
    )

    texto = texto.replace(
        "×",
        "*",
    )

    texto = texto.replace(
        "−",
        "-",
    )

    texto = "".join(
        caracter
        for caracter in unicodedata.normalize(
            "NFD",
            texto,
        )
        if unicodedata.category(
            caracter
        ) != "Mn"
    )

    return " ".join(
        texto.split()
    )


def obtener_categorias_propiedades():
    """Devuelve las categorías disponibles para filtrar propiedades."""
    return list(
        CATEGORIAS_PROPIEDADES
    )


def filtrar_propiedades(
    resultado,
    texto_busqueda="",
    categoria="Todas",
):
    """Filtra resultados ya calculados por número, nombre, fórmula o categoría."""
    if categoria not in CATEGORIAS_PROPIEDADES:
        raise ValueError(
            "La categoría seleccionada no es válida."
        )

    texto_normalizado = _normalizar_busqueda(
        texto_busqueda
    )

    propiedades_filtradas = []

    for propiedad in resultado[
        "propiedades"
    ]:
        if (
            categoria != "Todas"
            and propiedad[
                "categoria"
            ] != categoria
        ):
            continue

        if not texto_normalizado:
            propiedades_filtradas.append(
                propiedad
            )
            continue

        campos = (
            str(
                propiedad[
                    "numero"
                ]
            ),
            propiedad[
                "nombre"
            ],
            propiedad[
                "formula"
            ],
            propiedad[
                "categoria"
            ],
        )

        coincide = any(
            texto_normalizado
            in _normalizar_busqueda(
                campo
            )
            for campo in campos
        )

        if coincide:
            propiedades_filtradas.append(
                propiedad
            )

    return propiedades_filtradas


def verificar_propiedades_consolidadas(
    matriz_a,
    matriz_b,
    matriz_c,
    escalar,
):
    """Evalúa las propiedades usando A, B, C y r sin reingresar resultados."""
    _validar_matrices_cuadradas_mismo_orden(
        matriz_a,
        matriz_b,
        matriz_c,
    )

    escalar = Fraction(
        escalar
    )

    orden = len(
        matriz_a
    )

    identidad = crear_identidad(
        orden
    )

    propiedades = []

    suma_ab = sumar(
        matriz_a,
        matriz_b,
    )

    suma_bc = sumar(
        matriz_b,
        matriz_c,
    )

    producto_ab = producto_matricial(
        matriz_a,
        matriz_b,
    )

    producto_bc = producto_matricial(
        matriz_b,
        matriz_c,
    )

    transpuesta_a = transponer(
        matriz_a
    )

    transpuesta_b = transponer(
        matriz_b
    )

    r_a = multiplicar_por_escalar(
        matriz_a,
        escalar,
    )

    r_b = multiplicar_por_escalar(
        matriz_b,
        escalar,
    )

    propiedades.append(
        _resultado_doble(
            "Asociativa del producto",
            "A(BC) = (AB)C",
            producto_matricial(
                matriz_a,
                producto_bc,
            ),
            producto_matricial(
                producto_ab,
                matriz_c,
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva izquierda",
            "A(B + C) = AB + AC",
            producto_matricial(
                matriz_a,
                suma_bc,
            ),
            sumar(
                producto_ab,
                producto_matricial(
                    matriz_a,
                    matriz_c,
                ),
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva derecha",
            "(B + C)A = BA + CA",
            producto_matricial(
                suma_bc,
                matriz_a,
            ),
            sumar(
                producto_matricial(
                    matriz_b,
                    matriz_a,
                ),
                producto_matricial(
                    matriz_c,
                    matriz_a,
                ),
            ),
        )
    )

    propiedades.append(
        _resultado_triple(
            "Compatibilidad con escalar",
            "r(AB) = (rA)B = A(rB)",
            multiplicar_por_escalar(
                producto_ab,
                escalar,
            ),
            producto_matricial(
                r_a,
                matriz_b,
            ),
            producto_matricial(
                matriz_a,
                r_b,
            ),
        )
    )

    propiedades.append(
        _resultado_triple(
            "Identidad multiplicativa",
            "IA = A = AI",
            producto_matricial(
                identidad,
                matriz_a,
            ),
            matriz_a,
            producto_matricial(
                matriz_a,
                identidad,
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta doble",
            "(Aᵀ)ᵀ = A",
            transponer(
                transpuesta_a
            ),
            matriz_a,
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de una suma",
            "(A + B)ᵀ = Aᵀ + Bᵀ",
            transponer(
                suma_ab
            ),
            sumar(
                transpuesta_a,
                transpuesta_b,
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de un múltiplo",
            "(rA)ᵀ = rAᵀ",
            transponer(
                r_a
            ),
            multiplicar_por_escalar(
                transpuesta_a,
                escalar,
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de un producto",
            "(AB)ᵀ = BᵀAᵀ",
            transponer(
                producto_ab
            ),
            producto_matricial(
                transpuesta_b,
                transpuesta_a,
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva de escalar y transpuesta",
            "(r(A + B))ᵀ = rAᵀ + rBᵀ",
            transponer(
                multiplicar_por_escalar(
                    suma_ab,
                    escalar,
                )
            ),
            sumar(
                multiplicar_por_escalar(
                    transpuesta_a,
                    escalar,
                ),
                multiplicar_por_escalar(
                    transpuesta_b,
                    escalar,
                ),
            ),
        )
    )

    inversa_a = _agregar_propiedades_inversa(
        propiedades,
        matriz_a,
        matriz_b,
        producto_ab,
        transpuesta_a,
        identidad,
    )

    determinante_a = determinante(
        matriz_a
    )

    determinante_b = determinante(
        matriz_b
    )

    propiedades.append(
        _resultado_doble(
            "Determinante de la transpuesta",
            "det(Aᵀ) = det(A)",
            determinante(
                transpuesta_a
            ),
            determinante_a,
        )
    )

    propiedades.append(
        _resultado_doble(
            "Determinante de un producto",
            "det(AB) = det(A)det(B)",
            determinante(
                producto_ab
            ),
            determinante_a
            * determinante_b,
        )
    )

    if inversa_a is None:
        propiedades.append(
            _resultado_no_aplicable(
                "Determinante de la inversa",
                "det(A⁻¹) = 1/det(A)",
                "A es singular.",
            )
        )

    else:
        propiedades.append(
            _resultado_doble(
                "Determinante de la inversa",
                "det(A⁻¹) = 1/det(A)",
                determinante(
                    inversa_a
                ),
                Fraction(1, 1)
                / determinante_a,
            )
        )

    propiedades.append(
        _resultado_doble(
            "Determinante de un múltiplo",
            "det(rA) = rⁿdet(A)",
            determinante(
                r_a
            ),
            (escalar ** orden)
            * determinante_a,
        )
    )

    _agregar_propiedades_filas(
        propiedades,
        matriz_a,
        escalar,
    )

    triangular = verificar_propiedad_6(
        matriz_a
    )

    propiedades.append(
        _resultado_doble(
            "Determinante de una matriz triangular",
            "det(A) = determinante obtenido desde su forma triangular",
            triangular[
                "determinante_cofactores"
            ],
            triangular[
                "determinante_triangular"
            ],
        )
    )

    _asignar_metadatos(
        propiedades
    )

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

    return {
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "matriz_c": matriz_c,
        "escalar": escalar,
        "propiedades": propiedades,
        "total": len(
            propiedades
        ),
        "aplicables": len(
            aplicables
        ),
        "cumplidas": len(
            cumplidas
        ),
        "todas_cumplen": (
            len(aplicables)
            == len(cumplidas)
        ),
    }