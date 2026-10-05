"""
Verifica las seis propiedades matriciales requeridas en el Programa 5.
Reutiliza inversa, producto, transpuesta, determinante y operaciones de fila.
Tema de clase: propiedades de matrices invertibles y determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from copy import deepcopy
from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    calcular_determinante,
    triangularizar_para_determinante
)

from programas.matrices.inversa import (
    calcular_inversa
)

from programas.programa_3.matrices import (
    multiplicar_matrices,
    transponer_matriz
)

from programas.programa_3.propiedades_matrices_generales import (
    matrices_iguales
)

from programas.programa_1.operaciones_fila import (
    intercambiar_filas,
    multiplicar_fila,
    sumar_multiplo_fila
)


def validar_invertible(matriz):
    """Valida que una matriz sea cuadrada e invertible.
    Devuelve su matriz inversa."""
    validar_matriz_cuadrada(
        matriz
    )

    resultado = calcular_inversa(
        matriz
    )

    if not resultado["es_invertible"]:
        raise ValueError(
            "La matriz debe ser invertible "
            "para verificar esta propiedad."
        )

    return resultado[
        "inversa"
    ]


def validar_mismo_orden(matriz_a, matriz_b):
    """Valida que A y B sean matrices cuadradas del mismo orden."""
    validar_matriz_cuadrada(
        matriz_a
    )

    validar_matriz_cuadrada(
        matriz_b
    )

    if len(matriz_a) != len(matriz_b):
        raise ValueError(
            "Las matrices A y B deben tener "
            "el mismo orden."
        )


def verificar_inversa_de_inversa(matriz_a):
    """Comprueba la propiedad (A^-1)^-1 = A.
    Devuelve ambos miembros y el resultado de la comparación."""
    inversa_a = validar_invertible(
        matriz_a
    )

    inversa_de_inversa = validar_invertible(
        inversa_a
    )

    return {
        "propiedad":
            "(A⁻¹)⁻¹ = A",

        "inversa_a":
            inversa_a,

        "lado_izquierdo":
            inversa_de_inversa,

        "lado_derecho":
            matriz_a,

        "cumple":
            matrices_iguales(
                inversa_de_inversa,
                matriz_a
            )
    }


def verificar_inversa_producto(matriz_a, matriz_b):
    """Comprueba la propiedad (AB)^-1 = B^-1 A^-1.
    Devuelve ambos miembros y si son iguales."""
    validar_mismo_orden(
        matriz_a,
        matriz_b
    )

    inversa_a = validar_invertible(
        matriz_a
    )

    inversa_b = validar_invertible(
        matriz_b
    )

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    lado_izquierdo = validar_invertible(
        producto_ab
    )

    lado_derecho = multiplicar_matrices(
        inversa_b,
        inversa_a
    )

    return {
        "propiedad":
            "(AB)⁻¹ = B⁻¹A⁻¹",

        "producto_ab":
            producto_ab,

        "inversa_a":
            inversa_a,

        "inversa_b":
            inversa_b,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            matrices_iguales(
                lado_izquierdo,
                lado_derecho
            )
    }


def verificar_inversa_transpuesta(matriz_a):
    """Comprueba la propiedad (A^T)^-1 = (A^-1)^T.
    Devuelve ambos miembros y si son iguales."""
    inversa_a = validar_invertible(
        matriz_a
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    lado_izquierdo = validar_invertible(
        transpuesta_a
    )

    lado_derecho = transponer_matriz(
        inversa_a
    )

    return {
        "propiedad":
            "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",

        "transpuesta_a":
            transpuesta_a,

        "inversa_a":
            inversa_a,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            matrices_iguales(
                lado_izquierdo,
                lado_derecho
            )
    }


def verificar_determinante_inversa(matriz_a):
    """Comprueba la propiedad det(A^-1) = 1/det(A).
    Devuelve ambos valores y el resultado de la comparación."""
    inversa_a = validar_invertible(
        matriz_a
    )

    determinante_a = calcular_determinante(
        matriz_a
    )

    determinante_inversa = calcular_determinante(
        inversa_a
    )

    lado_derecho = (
        Fraction(1)
        / determinante_a
    )

    return {
        "propiedad":
            "det(A⁻¹) = 1/det(A)",

        "inversa_a":
            inversa_a,

        "determinante_a":
            determinante_a,

        "lado_izquierdo":
            determinante_inversa,

        "lado_derecho":
            lado_derecho,

        "cumple":
            (
                determinante_inversa
                == lado_derecho
            )
    }


def validar_indice_fila(matriz, fila):
    """Valida que un índice de fila pertenezca a la matriz."""
    if fila < 0 or fila >= len(matriz):
        raise ValueError(
            "La fila indicada no existe "
            "en la matriz."
        )


def crear_texto_reemplazo(
    fila_destino,
    fila_origen,
    escalar
):
    """Devuelve una operación de reemplazo con el signo escrito de forma natural."""
    if escalar < 0:
        return (
            f"F{fila_destino + 1} -> "
            f"F{fila_destino + 1} - "
            f"({-escalar})F{fila_origen + 1}"
        )

    return (
        f"F{fila_destino + 1} -> "
        f"F{fila_destino + 1} + "
        f"({escalar})F{fila_origen + 1}"
    )


def verificar_intercambio_filas(
    matriz_a,
    fila_1,
    fila_2
):
    """Comprueba que intercambiar dos filas cambia el signo del determinante."""
    validar_matriz_cuadrada(
        matriz_a
    )

    validar_indice_fila(
        matriz_a,
        fila_1
    )

    validar_indice_fila(
        matriz_a,
        fila_2
    )

    if fila_1 == fila_2:
        raise ValueError(
            "Para un intercambio deben seleccionarse "
            "dos filas diferentes."
        )

    matriz_transformada = deepcopy(
        matriz_a
    )

    intercambiar_filas(
        matriz_transformada,
        fila_1,
        fila_2
    )

    determinante_original = calcular_determinante(
        matriz_a
    )

    determinante_transformado = calcular_determinante(
        matriz_transformada
    )

    valor_esperado = (
        -determinante_original
    )

    return {
        "operacion":
            (
                f"F{fila_1 + 1} <-> "
                f"F{fila_2 + 1}"
            ),

        "matriz_transformada":
            matriz_transformada,

        "determinante_original":
            determinante_original,

        "determinante_transformado":
            determinante_transformado,

        "valor_esperado":
            valor_esperado,

        "cumple":
            (
                determinante_transformado
                == valor_esperado
            )
    }


def verificar_reemplazo_fila(
    matriz_a,
    fila_destino,
    fila_origen,
    escalar
):
    """Comprueba que Fi -> Fi + kFj conserva el determinante."""
    validar_matriz_cuadrada(
        matriz_a
    )

    validar_indice_fila(
        matriz_a,
        fila_destino
    )

    validar_indice_fila(
        matriz_a,
        fila_origen
    )

    if fila_destino == fila_origen:
        raise ValueError(
            "La fila destino y la fila origen "
            "deben ser diferentes."
        )

    escalar = Fraction(
        escalar
    )

    matriz_transformada = deepcopy(
        matriz_a
    )

    sumar_multiplo_fila(
        matriz_transformada,
        fila_destino,
        fila_origen,
        escalar
    )

    determinante_original = calcular_determinante(
        matriz_a
    )

    determinante_transformado = calcular_determinante(
        matriz_transformada
    )

    return {
        "operacion":
            crear_texto_reemplazo(
                fila_destino,
                fila_origen,
                escalar
            ),

        "matriz_transformada":
            matriz_transformada,

        "determinante_original":
            determinante_original,

        "determinante_transformado":
            determinante_transformado,

        "valor_esperado":
            determinante_original,

        "cumple":
            (
                determinante_transformado
                == determinante_original
            )
    }


def verificar_escalamiento_fila(
    matriz_a,
    fila,
    escalar
):
    """Comprueba que multiplicar una fila por k multiplica det(A) por k."""
    validar_matriz_cuadrada(
        matriz_a
    )

    validar_indice_fila(
        matriz_a,
        fila
    )

    escalar = Fraction(
        escalar
    )

    if escalar == 0:
        raise ValueError(
            "El escalar de una operación elemental "
            "no puede ser cero."
        )

    matriz_transformada = deepcopy(
        matriz_a
    )

    multiplicar_fila(
        matriz_transformada,
        fila,
        escalar
    )

    determinante_original = calcular_determinante(
        matriz_a
    )

    determinante_transformado = calcular_determinante(
        matriz_transformada
    )

    valor_esperado = (
        escalar
        * determinante_original
    )

    return {
        "operacion":
            (
                f"F{fila + 1} -> "
                f"({escalar})F{fila + 1}"
            ),

        "matriz_transformada":
            matriz_transformada,

        "determinante_original":
            determinante_original,

        "determinante_transformado":
            determinante_transformado,

        "valor_esperado":
            valor_esperado,

        "cumple":
            (
                determinante_transformado
                == valor_esperado
            )
    }


def verificar_propiedad_operaciones_fila(
    matriz_a,
    fila_1,
    fila_2,
    escalar_reemplazo,
    fila_escalar,
    escalar_fila
):
    """Comprueba las tres reglas del determinante ante operaciones elementales."""
    intercambio = verificar_intercambio_filas(
        matriz_a,
        fila_1,
        fila_2
    )

    reemplazo = verificar_reemplazo_fila(
        matriz_a,
        fila_2,
        fila_1,
        escalar_reemplazo
    )

    escalamiento = verificar_escalamiento_fila(
        matriz_a,
        fila_escalar,
        escalar_fila
    )

    return {
        "propiedad":
            (
                "Determinante y operaciones "
                "elementales de fila"
            ),

        "intercambio":
            intercambio,

        "reemplazo":
            reemplazo,

        "escalamiento":
            escalamiento,

        "cumple":
            (
                intercambio["cumple"]
                and reemplazo["cumple"]
                and escalamiento["cumple"]
            )
    }


def verificar_determinante_triangular(matriz_a):
    """Compara el determinante por cofactores con el obtenido al triangularizar A."""
    validar_matriz_cuadrada(
        matriz_a
    )

    determinante_cofactores = calcular_determinante(
        matriz_a
    )

    reduccion = triangularizar_para_determinante(
        matriz_a
    )

    determinante_triangular = reduccion[
        "determinante"
    ]

    return {
        "propiedad":
            (
                "El determinante de una matriz triangular "
                "es el producto corregido de su diagonal"
            ),

        "determinante_cofactores":
            determinante_cofactores,

        "matriz_triangular":
            reduccion[
                "matriz_triangular"
            ],

        "producto_diagonal":
            reduccion[
                "producto_diagonal"
            ],

        "intercambios":
            reduccion[
                "intercambios"
            ],

        "factores_eliminacion":
            reduccion[
                "factores_eliminacion"
            ],

        "num_pivotes":
            reduccion[
                "num_pivotes"
            ],

        "determinante_triangular":
            determinante_triangular,

        "historial":
            reduccion[
                "historial"
            ],

        "cumple":
            (
                determinante_cofactores
                == determinante_triangular
            )
    }