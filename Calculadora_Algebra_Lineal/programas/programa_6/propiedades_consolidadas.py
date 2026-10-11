"""
Consolida propiedades de matrices, transpuesta, inversa y determinantes.
Recibe A, B, C y r una sola vez y reutiliza resultados intermedios.
Tema de clase: propiedades matriciales y encadenamiento de funciones.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.programa_3.matrices import (
    sumar_matrices,
    multiplicar_matriz_escalar,
    multiplicar_matrices,
    transponer_matriz,
)

from programas.determinantes.determinante import (
    calcular_determinante,
)

from programas.matrices.inversa import (
    calcular_inversa,
)

from programas.programa_6.factorizacion_lu import (
    factorizar_lu,
)


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

    orden = len(
        matriz_a
    )

    if orden == 0:
        raise ValueError(
            "Las matrices no pueden estar vacías."
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


def _identidad(orden):
    """Construye la identidad de orden n."""
    matriz = []

    for i in range(orden):
        fila = []

        for j in range(orden):
            fila.append(
                Fraction(1)
                if i == j
                else Fraction(0)
            )

        matriz.append(
            fila
        )

    return matriz


def _resultado_doble(
    nombre,
    formula,
    lado_izquierdo,
    lado_derecho,
):
    """Construye el resultado de una igualdad con dos miembros."""
    return {
        "nombre": nombre,
        "formula": formula,
        "tipo": "doble",
        "aplicable": True,
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "cumple": lado_izquierdo == lado_derecho,
    }


def _resultado_triple(
    nombre,
    formula,
    miembro_1,
    miembro_2,
    miembro_3,
):
    """Construye el resultado de una igualdad con tres miembros."""
    return {
        "nombre": nombre,
        "formula": formula,
        "tipo": "triple",
        "aplicable": True,
        "miembro_1": miembro_1,
        "miembro_2": miembro_2,
        "miembro_3": miembro_3,
        "cumple": (
            miembro_1 == miembro_2
            and miembro_2 == miembro_3
        ),
    }


def _resultado_no_aplicable(nombre, formula, razon):
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
    """Devuelve A⁻¹ o None cuando la matriz es singular."""
    resultado = calcular_inversa(
        matriz
    )

    if not resultado[
        "es_invertible"
    ]:
        return None

    return resultado[
        "inversa"
    ]


def _intercambiar_dos_filas(matriz):
    """Devuelve una copia de A con F₁ y F₂ intercambiadas."""
    resultado = [
        fila.copy()
        for fila in matriz
    ]

    resultado[0], resultado[1] = (
        resultado[1],
        resultado[0],
    )

    return resultado


def _reemplazar_fila(matriz, escalar):
    """Devuelve A después de F₂ -> F₂ + rF₁."""
    resultado = [
        fila.copy()
        for fila in matriz
    ]

    for j in range(
        len(resultado[0])
    ):
        resultado[1][j] += (
            escalar
            * resultado[0][j]
        )

    return resultado


def _escalar_primera_fila(matriz, escalar):
    """Devuelve A después de F₁ -> rF₁."""
    resultado = [
        fila.copy()
        for fila in matriz
    ]

    for j in range(
        len(resultado[0])
    ):
        resultado[0][j] *= escalar

    return resultado


def _producto_diagonal(matriz):
    """Calcula el producto de la diagonal principal."""
    producto = Fraction(1)

    limite = min(
        len(matriz),
        len(matriz[0]),
    )

    for i in range(limite):
        producto *= matriz[i][i]

    return producto


def verificar_propiedades_consolidadas(
    matriz_a,
    matriz_b,
    matriz_c,
    escalar,
):
    """Evalúa el conjunto consolidado usando A, B, C y r una sola vez."""
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

    identidad = _identidad(
        orden
    )

    propiedades = []

    suma_ab = sumar_matrices(
        matriz_a,
        matriz_b
    )

    suma_bc = sumar_matrices(
        matriz_b,
        matriz_c
    )

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    producto_bc = multiplicar_matrices(
        matriz_b,
        matriz_c
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    transpuesta_b = transponer_matriz(
        matriz_b
    )

    r_a = multiplicar_matriz_escalar(
        matriz_a,
        escalar
    )

    r_b = multiplicar_matriz_escalar(
        matriz_b,
        escalar
    )

    propiedades.append(
        _resultado_doble(
            "Asociativa del producto",
            "A(BC) = (AB)C",
            multiplicar_matrices(
                matriz_a,
                producto_bc
            ),
            multiplicar_matrices(
                producto_ab,
                matriz_c
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva izquierda",
            "A(B + C) = AB + AC",
            multiplicar_matrices(
                matriz_a,
                suma_bc
            ),
            sumar_matrices(
                producto_ab,
                multiplicar_matrices(
                    matriz_a,
                    matriz_c
                ),
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva derecha",
            "(B + C)A = BA + CA",
            multiplicar_matrices(
                suma_bc,
                matriz_a
            ),
            sumar_matrices(
                multiplicar_matrices(
                    matriz_b,
                    matriz_a
                ),
                multiplicar_matrices(
                    matriz_c,
                    matriz_a
                ),
            ),
        )
    )

    propiedades.append(
        _resultado_triple(
            "Compatibilidad con escalar",
            "r(AB) = (rA)B = A(rB)",
            multiplicar_matriz_escalar(
                producto_ab,
                escalar
            ),
            multiplicar_matrices(
                r_a,
                matriz_b
            ),
            multiplicar_matrices(
                matriz_a,
                r_b
            ),
        )
    )

    propiedades.append(
        _resultado_triple(
            "Identidad multiplicativa",
            "IA = A = AI",
            multiplicar_matrices(
                identidad,
                matriz_a
            ),
            matriz_a,
            multiplicar_matrices(
                matriz_a,
                identidad
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta doble",
            "(Aᵀ)ᵀ = A",
            transponer_matriz(
                transpuesta_a
            ),
            matriz_a,
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de una suma",
            "(A + B)ᵀ = Aᵀ + Bᵀ",
            transponer_matriz(
                suma_ab
            ),
            sumar_matrices(
                transpuesta_a,
                transpuesta_b
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de un múltiplo",
            "(rA)ᵀ = rAᵀ",
            transponer_matriz(
                r_a
            ),
            multiplicar_matriz_escalar(
                transpuesta_a,
                escalar
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Transpuesta de un producto",
            "(AB)ᵀ = BᵀAᵀ",
            transponer_matriz(
                producto_ab
            ),
            multiplicar_matrices(
                transpuesta_b,
                transpuesta_a
            ),
        )
    )

    propiedades.append(
        _resultado_doble(
            "Distributiva de escalar y transpuesta",
            "(r(A + B))ᵀ = rAᵀ + rBᵀ",
            transponer_matriz(
                multiplicar_matriz_escalar(
                    suma_ab,
                    escalar
                )
            ),
            sumar_matrices(
                multiplicar_matriz_escalar(
                    transpuesta_a,
                    escalar
                ),
                multiplicar_matriz_escalar(
                    transpuesta_b,
                    escalar
                ),
            ),
        )
    )

    inversa_a = _obtener_inversa(
        matriz_a
    )

    inversa_b = _obtener_inversa(
        matriz_b
    )

    if inversa_a is None:
        propiedades.append(
            _resultado_no_aplicable(
                "Inversa de la inversa",
                "(A⁻¹)⁻¹ = A",
                "A es singular."
            )
        )

        propiedades.append(
            _resultado_no_aplicable(
                "Inversa de la transpuesta",
                "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
                "A es singular."
            )
        )

    else:
        propiedades.append(
            _resultado_doble(
                "Inversa de la inversa",
                "(A⁻¹)⁻¹ = A",
                _obtener_inversa(
                    inversa_a
                ),
                matriz_a,
            )
        )

        propiedades.append(
            _resultado_doble(
                "Inversa de la transpuesta",
                "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
                _obtener_inversa(
                    transpuesta_a
                ),
                transponer_matriz(
                    inversa_a
                ),
            )
        )

    if inversa_a is None or inversa_b is None:
        propiedades.append(
            _resultado_no_aplicable(
                "Inversa de un producto",
                "(AB)⁻¹ = B⁻¹A⁻¹",
                "A y B deben ser invertibles."
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
                multiplicar_matrices(
                    inversa_b,
                    inversa_a
                ),
            )
        )

    determinante_a = calcular_determinante(
        matriz_a
    )

    determinante_b = calcular_determinante(
        matriz_b
    )

    determinante_ab = calcular_determinante(
        producto_ab
    )

    propiedades.append(
        _resultado_doble(
            "Determinante de la transpuesta",
            "det(Aᵀ) = det(A)",
            calcular_determinante(
                transpuesta_a
            ),
            determinante_a,
        )
    )

    propiedades.append(
        _resultado_doble(
            "Determinante de un producto",
            "det(AB) = det(A)det(B)",
            determinante_ab,
            determinante_a * determinante_b,
        )
    )

    if inversa_a is None:
        propiedades.append(
            _resultado_no_aplicable(
                "Determinante de la inversa",
                "det(A⁻¹) = 1/det(A)",
                "A es singular."
            )
        )
    else:
        propiedades.append(
            _resultado_doble(
                "Determinante de la inversa",
                "det(A⁻¹) = 1/det(A)",
                calcular_determinante(
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
            calcular_determinante(
                r_a
            ),
            (escalar ** orden)
            * determinante_a,
        )
    )

    if orden >= 2:
        matriz_intercambio = _intercambiar_dos_filas(
            matriz_a
        )

        propiedades.append(
            _resultado_doble(
                "Intercambio de filas",
                "det(F₁ ↔ F₂) = -det(A)",
                calcular_determinante(
                    matriz_intercambio
                ),
                -determinante_a,
            )
        )

        matriz_reemplazo = _reemplazar_fila(
            matriz_a,
            escalar
        )

        propiedades.append(
            _resultado_doble(
                "Reemplazo de fila",
                "det(F₂ → F₂ + rF₁) = det(A)",
                calcular_determinante(
                    matriz_reemplazo
                ),
                determinante_a,
            )
        )
    else:
        propiedades.append(
            _resultado_no_aplicable(
                "Intercambio de filas",
                "det(F₁ ↔ F₂) = -det(A)",
                "Se necesita una matriz de orden mínimo 2."
            )
        )

        propiedades.append(
            _resultado_no_aplicable(
                "Reemplazo de fila",
                "det(F₂ → F₂ + rF₁) = det(A)",
                "Se necesita una matriz de orden mínimo 2."
            )
        )

    matriz_escalada = _escalar_primera_fila(
        matriz_a,
        escalar
    )

    propiedades.append(
        _resultado_doble(
            "Escalamiento de una fila",
            "det(F₁ → rF₁) = r·det(A)",
            calcular_determinante(
                matriz_escalada
            ),
            escalar * determinante_a,
        )
    )

    try:
        factorizacion = factorizar_lu(
            matriz_a
        )

        producto_diagonal = _producto_diagonal(
            factorizacion[
                "matriz_u"
            ]
        )

        propiedades.append(
            _resultado_doble(
                "Determinante triangular mediante LU",
                "det(A) = producto de la diagonal de U",
                determinante_a,
                producto_diagonal,
            )
        )

    except ValueError as error:
        propiedades.append(
            _resultado_no_aplicable(
                "Determinante triangular mediante LU",
                "det(A) = producto de la diagonal de U",
                str(error)
            )
        )

    aplicables = [
        propiedad
        for propiedad in propiedades
        if propiedad["aplicable"]
    ]

    cumplidas = [
        propiedad
        for propiedad in aplicables
        if propiedad["cumple"]
    ]

    return {
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "matriz_c": matriz_c,
        "escalar": escalar,
        "propiedades": propiedades,
        "total": len(propiedades),
        "aplicables": len(aplicables),
        "cumplidas": len(cumplidas),
        "todas_cumplen": (
            len(aplicables)
            == len(cumplidas)
        ),
    }
