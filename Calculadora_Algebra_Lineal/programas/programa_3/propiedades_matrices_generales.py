"""
Verifica propiedades generales de las operaciones con matrices.
Incluye suma, producto, escalares y propiedades de la transpuesta.
Tema de clase: Módulo III de Álgebra de Matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.programa_3.matrices import (
    validar_matriz,
    validar_mismas_dimensiones,
    sumar_matrices,
    multiplicar_matriz_escalar,
    multiplicar_matrices,
    transponer_matriz
)


# ==========================================================
# PROPIEDADES GENERALES DE MATRICES
# ==========================================================


# ==========================================================
# COMPARAR MATRICES
# ==========================================================

def matrices_iguales(
    matriz_1,
    matriz_2
):

    validar_matriz(
        matriz_1
    )

    validar_matriz(
        matriz_2
    )

    if (
        len(matriz_1)
        != len(matriz_2)
    ):

        return False

    if (
        len(matriz_1[0])
        != len(matriz_2[0])
    ):

        return False

    for i in range(
        len(matriz_1)
    ):

        for j in range(
            len(matriz_1[i])
        ):

            if (
                matriz_1[i][j]
                != matriz_2[i][j]
            ):

                return False

    return True


# ==========================================================
# MATRIZ IDENTIDAD
# ==========================================================

def crear_matriz_identidad(
    orden
):

    if orden <= 0:

        raise ValueError(
            "El orden de la matriz identidad "
            "debe ser mayor que cero."
        )

    identidad = []

    for i in range(
        orden
    ):

        fila = []

        for j in range(
            orden
        ):

            if i == j:

                fila.append(
                    Fraction(1)
                )

            else:

                fila.append(
                    Fraction(0)
                )

        identidad.append(
            fila
        )

    return identidad


# ==========================================================
# PROPIEDAD ASOCIATIVA
#
# A(BC) = (AB)C
# ==========================================================

def verificar_asociativa_multiplicacion(
    matriz_a,
    matriz_b,
    matriz_c
):

    validar_matriz(
        matriz_a
    )

    validar_matriz(
        matriz_b
    )

    validar_matriz(
        matriz_c
    )

    # Calculamos BC.
    producto_bc = multiplicar_matrices(
        matriz_b,
        matriz_c
    )

    # Calculamos A(BC).
    lado_izquierdo = multiplicar_matrices(
        matriz_a,
        producto_bc
    )

    # Calculamos AB.
    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    # Calculamos (AB)C.
    lado_derecho = multiplicar_matrices(
        producto_ab,
        matriz_c
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "A(BC) = (AB)C",

        "producto_bc":
            producto_bc,

        "producto_ab":
            producto_ab,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# PROPIEDAD DISTRIBUTIVA IZQUIERDA
#
# A(B + C) = AB + AC
# ==========================================================

def verificar_distributiva_izquierda(
    matriz_a,
    matriz_b,
    matriz_c
):

    validar_mismas_dimensiones(
        matriz_b,
        matriz_c
    )

    suma_bc = sumar_matrices(
        matriz_b,
        matriz_c
    )

    lado_izquierdo = multiplicar_matrices(
        matriz_a,
        suma_bc
    )

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    producto_ac = multiplicar_matrices(
        matriz_a,
        matriz_c
    )

    lado_derecho = sumar_matrices(
        producto_ab,
        producto_ac
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "A(B + C) = AB + AC",

        "suma_bc":
            suma_bc,

        "producto_ab":
            producto_ab,

        "producto_ac":
            producto_ac,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# PROPIEDAD DISTRIBUTIVA DERECHA
#
# (B + C)A = BA + CA
# ==========================================================

def verificar_distributiva_derecha(
    matriz_a,
    matriz_b,
    matriz_c
):

    validar_mismas_dimensiones(
        matriz_b,
        matriz_c
    )

    suma_bc = sumar_matrices(
        matriz_b,
        matriz_c
    )

    lado_izquierdo = multiplicar_matrices(
        suma_bc,
        matriz_a
    )

    producto_ba = multiplicar_matrices(
        matriz_b,
        matriz_a
    )

    producto_ca = multiplicar_matrices(
        matriz_c,
        matriz_a
    )

    lado_derecho = sumar_matrices(
        producto_ba,
        producto_ca
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "(B + C)A = BA + CA",

        "suma_bc":
            suma_bc,

        "producto_ba":
            producto_ba,

        "producto_ca":
            producto_ca,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# ESCALAR Y PRODUCTO DE MATRICES
#
# r(AB) = (rA)B = A(rB)
# ==========================================================

def verificar_escalar_producto(
    matriz_a,
    matriz_b,
    escalar
):

    escalar = Fraction(
        escalar
    )

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    # r(AB)
    resultado_1 = multiplicar_matriz_escalar(
        producto_ab,
        escalar
    )

    # (rA)B
    r_a = multiplicar_matriz_escalar(
        matriz_a,
        escalar
    )

    resultado_2 = multiplicar_matrices(
        r_a,
        matriz_b
    )

    # A(rB)
    r_b = multiplicar_matriz_escalar(
        matriz_b,
        escalar
    )

    resultado_3 = multiplicar_matrices(
        matriz_a,
        r_b
    )

    cumple = (
        matrices_iguales(
            resultado_1,
            resultado_2
        )
        and
        matrices_iguales(
            resultado_2,
            resultado_3
        )
    )

    return {
        "propiedad":
            "r(AB) = (rA)B = A(rB)",

        "escalar":
            escalar,

        "producto_ab":
            producto_ab,

        "r_a":
            r_a,

        "r_b":
            r_b,

        "resultado_1":
            resultado_1,

        "resultado_2":
            resultado_2,

        "resultado_3":
            resultado_3,

        "cumple":
            cumple
    }


# ==========================================================
# IDENTIDAD MULTIPLICATIVA
#
# I A = A = A I
# ==========================================================

def verificar_identidad_multiplicacion(
    matriz_a
):

    validar_matriz(
        matriz_a
    )

    filas = len(
        matriz_a
    )

    columnas = len(
        matriz_a[0]
    )

    # La identidad izquierda debe tener tantas
    # filas y columnas como filas tiene A.
    identidad_izquierda = crear_matriz_identidad(
        filas
    )

    # La identidad derecha debe tener tantas
    # filas y columnas como columnas tiene A.
    identidad_derecha = crear_matriz_identidad(
        columnas
    )

    producto_izquierdo = multiplicar_matrices(
        identidad_izquierda,
        matriz_a
    )

    producto_derecho = multiplicar_matrices(
        matriz_a,
        identidad_derecha
    )

    cumple = (
        matrices_iguales(
            producto_izquierdo,
            matriz_a
        )
        and
        matrices_iguales(
            producto_derecho,
            matriz_a
        )
    )

    return {
        "propiedad":
            "IA = A = AI",

        "identidad_izquierda":
            identidad_izquierda,

        "identidad_derecha":
            identidad_derecha,

        "producto_izquierdo":
            producto_izquierdo,

        "producto_derecho":
            producto_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# TRANSPUESTA DOBLE
#
# (Aᵀ)ᵀ = A
# ==========================================================

def verificar_transpuesta_doble(
    matriz_a
):

    validar_matriz(
        matriz_a
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    transpuesta_doble = transponer_matriz(
        transpuesta_a
    )

    cumple = matrices_iguales(
        transpuesta_doble,
        matriz_a
    )

    return {
        "propiedad":
            "(Aᵀ)ᵀ = A",

        "transpuesta_a":
            transpuesta_a,

        "transpuesta_doble":
            transpuesta_doble,

        "resultado_esperado":
            matriz_a,

        "cumple":
            cumple
    }


# ==========================================================
# TRANSPUESTA DE UNA SUMA
#
# (A + B)ᵀ = Aᵀ + Bᵀ
# ==========================================================

def verificar_transpuesta_suma(
    matriz_a,
    matriz_b
):

    validar_mismas_dimensiones(
        matriz_a,
        matriz_b
    )

    suma_ab = sumar_matrices(
        matriz_a,
        matriz_b
    )

    lado_izquierdo = transponer_matriz(
        suma_ab
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    transpuesta_b = transponer_matriz(
        matriz_b
    )

    lado_derecho = sumar_matrices(
        transpuesta_a,
        transpuesta_b
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "(A + B)ᵀ = Aᵀ + Bᵀ",

        "suma_ab":
            suma_ab,

        "transpuesta_a":
            transpuesta_a,

        "transpuesta_b":
            transpuesta_b,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# TRANSPUESTA DE UN MÚLTIPLO ESCALAR
#
# (rA)ᵀ = rAᵀ
# ==========================================================

def verificar_transpuesta_escalar(
    matriz_a,
    escalar
):

    validar_matriz(
        matriz_a
    )

    escalar = Fraction(
        escalar
    )

    r_a = multiplicar_matriz_escalar(
        matriz_a,
        escalar
    )

    lado_izquierdo = transponer_matriz(
        r_a
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    lado_derecho = multiplicar_matriz_escalar(
        transpuesta_a,
        escalar
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "(rA)ᵀ = rAᵀ",

        "escalar":
            escalar,

        "r_a":
            r_a,

        "transpuesta_a":
            transpuesta_a,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }


# ==========================================================
# TRANSPUESTA DE UN PRODUCTO
#
# (AB)ᵀ = BᵀAᵀ
# ==========================================================

def verificar_transpuesta_producto(
    matriz_a,
    matriz_b
):

    producto_ab = multiplicar_matrices(
        matriz_a,
        matriz_b
    )

    lado_izquierdo = transponer_matriz(
        producto_ab
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    transpuesta_b = transponer_matriz(
        matriz_b
    )

    lado_derecho = multiplicar_matrices(
        transpuesta_b,
        transpuesta_a
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "(AB)ᵀ = BᵀAᵀ",

        "producto_ab":
            producto_ab,

        "transpuesta_a":
            transpuesta_a,

        "transpuesta_b":
            transpuesta_b,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }

# ==========================================================
# DISTRIBUTIVA DEL ESCALAR Y LA TRANSPUESTA SOBRE UNA SUMA
#
# (r(A + B))ᵀ = rAᵀ + rBᵀ
# ==========================================================

def verificar_distributiva_escalar_transpuesta(
    matriz_a,
    matriz_b,
    escalar
):
    """Verifica (r(A + B))ᵀ = rAᵀ + rBᵀ y devuelve sus pasos."""
    validar_mismas_dimensiones(
        matriz_a,
        matriz_b
    )

    escalar = Fraction(
        escalar
    )

    suma_ab = sumar_matrices(
        matriz_a,
        matriz_b
    )

    r_suma = multiplicar_matriz_escalar(
        suma_ab,
        escalar
    )

    lado_izquierdo = transponer_matriz(
        r_suma
    )

    transpuesta_a = transponer_matriz(
        matriz_a
    )

    transpuesta_b = transponer_matriz(
        matriz_b
    )

    r_transpuesta_a = multiplicar_matriz_escalar(
        transpuesta_a,
        escalar
    )

    r_transpuesta_b = multiplicar_matriz_escalar(
        transpuesta_b,
        escalar
    )

    lado_derecho = sumar_matrices(
        r_transpuesta_a,
        r_transpuesta_b
    )

    cumple = matrices_iguales(
        lado_izquierdo,
        lado_derecho
    )

    return {
        "propiedad":
            "(r(A + B))ᵀ = rAᵀ + rBᵀ",

        "escalar":
            escalar,

        "suma_ab":
            suma_ab,

        "r_suma":
            r_suma,

        "transpuesta_a":
            transpuesta_a,

        "transpuesta_b":
            transpuesta_b,

        "r_transpuesta_a":
            r_transpuesta_a,

        "r_transpuesta_b":
            r_transpuesta_b,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "cumple":
            cumple
    }

