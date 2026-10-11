"""
Encadena determinantes, cofactores, adjunta, inversa y propiedades.
Reutiliza resultados intermedios para evitar reingresar matrices.
Tema de clase: determinantes, matriz adjunta e invertibilidad.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    calcular_determinante,
)

from programas.determinantes.procedimiento_determinante import (
    comparar_procedimientos_determinante,
)

from programas.determinantes.cofactores_detallados import (
    calcular_cofactores_detallados,
)

from programas.matrices.inversa import (
    calcular_inversa,
)

from programas.programa_3.matrices import (
    multiplicar_matrices,
    multiplicar_matriz_escalar,
    transponer_matriz,
)

from programas.programa_3.propiedades_matrices_generales import (
    crear_matriz_identidad,
    matrices_iguales,
)


def _validar_matrices(matriz_a, matriz_b):
    """Valida que A y B sean cuadradas y del mismo orden."""
    validar_matriz_cuadrada(
        matriz_a
    )

    validar_matriz_cuadrada(
        matriz_b
    )

    if len(matriz_a) != len(matriz_b):
        raise ValueError(
            "Las matrices A y B deben tener el mismo orden."
        )


def _construir_adjunta(matriz_cofactores):
    """Obtiene adj(A) transponiendo la matriz de cofactores."""
    return transponer_matriz(
        matriz_cofactores
    )


def _construir_inversa_adjunta(adjunta, determinante_a):
    """Calcula A⁻¹ = (1/det(A)) adj(A) usando la adjunta ya obtenida."""
    factor = Fraction(
        1,
        1
    ) / determinante_a

    inversa = multiplicar_matriz_escalar(
        adjunta,
        factor
    )

    return factor, inversa


def _verificar_inversa(matriz_a, inversa):
    """Verifica A·A⁻¹ = I y A⁻¹·A = I."""
    orden = len(
        matriz_a
    )

    identidad = crear_matriz_identidad(
        orden
    )

    producto_a_inversa = multiplicar_matrices(
        matriz_a,
        inversa
    )

    producto_inversa_a = multiplicar_matrices(
        inversa,
        matriz_a
    )

    cumple_izquierda = matrices_iguales(
        producto_a_inversa,
        identidad
    )

    cumple_derecha = matrices_iguales(
        producto_inversa_a,
        identidad
    )

    return {
        "identidad": identidad,
        "producto_a_inversa": producto_a_inversa,
        "producto_inversa_a": producto_inversa_a,
        "cumple_izquierda": cumple_izquierda,
        "cumple_derecha": cumple_derecha,
        "cumple": cumple_izquierda and cumple_derecha,
    }


def _propiedad_transpuesta(matriz_a, determinante_a):
    """Verifica det(Aᵀ) = det(A)."""
    transpuesta_a = transponer_matriz(
        matriz_a
    )

    determinante_transpuesta = calcular_determinante(
        transpuesta_a
    )

    return {
        "transpuesta_a": transpuesta_a,
        "determinante_transpuesta": determinante_transpuesta,
        "determinante_a": determinante_a,
        "cumple": determinante_transpuesta == determinante_a,
    }


def _propiedad_producto(matriz_a, matriz_b, determinante_a):
    """Verifica det(AB) = det(A)det(B)."""
    determinante_b = calcular_determinante(
        matriz_b
    )

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    determinante_ab = calcular_determinante(
        producto_ab
    )

    producto_determinantes = (
        determinante_a
        * determinante_b
    )

    return {
        "matriz_b": matriz_b,
        "producto_ab": producto_ab,
        "determinante_a": determinante_a,
        "determinante_b": determinante_b,
        "determinante_ab": determinante_ab,
        "producto_determinantes": producto_determinantes,
        "cumple": determinante_ab == producto_determinantes,
    }


def _propiedad_inversa(inversa, determinante_a):
    """Verifica det(A⁻¹) = 1/det(A)."""
    determinante_inversa = calcular_determinante(
        inversa
    )

    reciproco = Fraction(
        1,
        1
    ) / determinante_a

    return {
        "determinante_inversa": determinante_inversa,
        "reciproco_determinante": reciproco,
        "cumple": determinante_inversa == reciproco,
    }


def _diagnostico_invertibilidad(determinante_a, orden, gauss_jordan):
    """Construye la justificación de invertibilidad utilizada en la salida."""
    posiciones_pivote = gauss_jordan.get(
        "posiciones_pivote",
        []
    )

    num_pivotes = len(
        posiciones_pivote
    )

    es_invertible = (
        determinante_a != 0
        and gauss_jordan.get(
            "es_invertible",
            False
        )
        and num_pivotes == orden
    )

    if es_invertible:
        texto = (
            "A es invertible porque det(A) ≠ 0. "
            "Además tiene n posiciones pivote, sus columnas son L.I. "
            "y generan ℝⁿ."
        )
    else:
        texto = (
            "A es singular porque det(A) = 0; no posee inversa."
        )

    return {
        "es_invertible": es_invertible,
        "num_pivotes": num_pivotes,
        "texto": texto,
    }


def resolver_analisis_matricial_integrado(matriz_a, matriz_b):
    """Ejecuta el flujo completo reutilizando A, B y resultados intermedios."""
    _validar_matrices(
        matriz_a,
        matriz_b
    )

    orden = len(
        matriz_a
    )

    metodos_determinante = comparar_procedimientos_determinante(
        matriz_a
    )

    determinante_a = calcular_determinante(
        matriz_a
    )

    cofactores = calcular_cofactores_detallados(
        matriz_a
    )

    matriz_cofactores = cofactores[
        "matriz_cofactores"
    ]

    adjunta = _construir_adjunta(
        matriz_cofactores
    )

    gauss_jordan = calcular_inversa(
        matriz_a
    )

    propiedad_transpuesta = _propiedad_transpuesta(
        matriz_a,
        determinante_a
    )

    propiedad_producto = _propiedad_producto(
        matriz_a,
        matriz_b,
        determinante_a
    )

    resultado = {
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "orden": orden,
        "determinante_a": determinante_a,
        "metodos_determinante": metodos_determinante,
        "cofactores": cofactores,
        "matriz_cofactores": matriz_cofactores,
        "adjunta": adjunta,
        "gauss_jordan": gauss_jordan,
        "propiedad_transpuesta": propiedad_transpuesta,
        "propiedad_producto": propiedad_producto,
    }

    if determinante_a == 0:
        resultado.update(
            {
                "factor_inversa": None,
                "inversa_adjunta": None,
                "verificacion_inversa": None,
                "comparacion_inversas": None,
                "propiedad_inversa": None,
                "diagnostico": {
                    "es_invertible": False,
                    "num_pivotes": len(
                        gauss_jordan.get(
                            "posiciones_pivote",
                            []
                        )
                    ),
                    "texto": (
                        "A es singular porque det(A) = 0; "
                        "no posee inversa."
                    ),
                },
            }
        )

        return resultado

    factor_inversa, inversa_adjunta = _construir_inversa_adjunta(
        adjunta,
        determinante_a
    )

    verificacion_inversa = _verificar_inversa(
        matriz_a,
        inversa_adjunta
    )

    inversa_gauss = gauss_jordan[
        "inversa"
    ]

    comparacion_inversas = matrices_iguales(
        inversa_adjunta,
        inversa_gauss
    )

    propiedad_inversa = _propiedad_inversa(
        inversa_adjunta,
        determinante_a
    )

    diagnostico = _diagnostico_invertibilidad(
        determinante_a,
        orden,
        gauss_jordan
    )

    resultado.update(
        {
            "factor_inversa": factor_inversa,
            "inversa_adjunta": inversa_adjunta,
            "verificacion_inversa": verificacion_inversa,
            "comparacion_inversas": comparacion_inversas,
            "propiedad_inversa": propiedad_inversa,
            "diagnostico": diagnostico,
        }
    )

    return resultado
