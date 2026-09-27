from utilidades.estructuras_entrada import (
    convertir_matriz
)

from utilidades.numeros import (
    convertir_a_fraccion
)

from programas.programa_3.matrices import (
    sumar_matrices,
    restar_matrices,
    multiplicar_matriz_escalar,
    multiplicar_matrices_con_procedimiento,
    transponer_matriz
)

from programas.matrices.inversa import (
    calcular_inversa
)

from programas.programa_3.propiedades_matrices_generales import (
    verificar_asociativa_multiplicacion,
    verificar_distributiva_izquierda,
    verificar_distributiva_derecha,
    verificar_escalar_producto,
    verificar_identidad_multiplicacion,
    verificar_transpuesta_doble,
    verificar_transpuesta_suma,
    verificar_transpuesta_escalar,
    verificar_transpuesta_producto
)


# ==========================================================
# MÓDULO 3
# CONTROLADOR DE ÁLGEBRA DE MATRICES
# ==========================================================


# ==========================================================
# OPERACIONES BÁSICAS
#
# suma
# resta
# escalar
# ==========================================================

def procesar_operacion_basica(
    operacion,
    matriz_a,
    matriz_b=None,
    escalar=None
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    # ======================================================
    # SUMA
    # ======================================================

    if operacion == "suma":

        if matriz_b is None:

            raise ValueError(
                "Debe ingresar la matriz B."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        resultado = sumar_matrices(
            matriz_a,
            matriz_b
        )

        return {
            "operacion":
                "suma",

            "matriz_a":
                matriz_a,

            "matriz_b":
                matriz_b,

            "resultado":
                resultado
        }

    # ======================================================
    # RESTA
    # ======================================================

    if operacion == "resta":

        if matriz_b is None:

            raise ValueError(
                "Debe ingresar la matriz B."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        resultado = restar_matrices(
            matriz_a,
            matriz_b
        )

        return {
            "operacion":
                "resta",

            "matriz_a":
                matriz_a,

            "matriz_b":
                matriz_b,

            "resultado":
                resultado
        }

    # ======================================================
    # MULTIPLICACIÓN POR ESCALAR
    # ======================================================

    if operacion == "escalar":

        if escalar is None:

            raise ValueError(
                "Debe ingresar un escalar."
            )

        escalar = convertir_a_fraccion(
            escalar
        )

        resultado = multiplicar_matriz_escalar(
            matriz_a,
            escalar
        )

        return {
            "operacion":
                "escalar",

            "matriz_a":
                matriz_a,

            "escalar":
                escalar,

            "resultado":
                resultado
        }

    raise ValueError(
        "La operación básica seleccionada "
        "no es válida."
    )


# ==========================================================
# MULTIPLICACIÓN DE MATRICES
#
# AB mediante regla fila-columna.
# ==========================================================

def procesar_multiplicacion_matrices(
    matriz_a,
    matriz_b
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    matriz_b = convertir_matriz(
        matriz_b
    )

    resultado = (
        multiplicar_matrices_con_procedimiento(
            matriz_a,
            matriz_b
        )
    )

    return {
        "operacion":
            "multiplicacion",

        "matriz_a":
            matriz_a,

        "matriz_b":
            matriz_b,

        "resultado":
            resultado["resultado"],

        "procedimiento":
            resultado["procedimiento"]
    }


# ==========================================================
# TRANSPUESTA
# ==========================================================

def procesar_transpuesta(
    matriz_a
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    transpuesta = transponer_matriz(
        matriz_a
    )

    return {
        "operacion":
            "transpuesta",

        "matriz_a":
            matriz_a,

        "resultado":
            transpuesta
    }


# ==========================================================
# MATRIZ INVERSA
#
# [A | I] -> [I | A⁻¹]
# ==========================================================

def procesar_inversa(
    matriz_a
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    resultado = calcular_inversa(
        matriz_a
    )

    return {
        "operacion":
            "inversa",

        "resultado":
            resultado
    }


# ==========================================================
# PROPIEDADES GENERALES
# ==========================================================

def procesar_propiedad_matrices(
    propiedad,
    matriz_a,
    matriz_b=None,
    matriz_c=None,
    escalar=None
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    # ======================================================
    # A(BC) = (AB)C
    # ======================================================

    if propiedad == "asociativa":

        if (
            matriz_b is None
            or matriz_c is None
        ):

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A, B y C."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        matriz_c = convertir_matriz(
            matriz_c
        )

        return verificar_asociativa_multiplicacion(
            matriz_a,
            matriz_b,
            matriz_c
        )

    # ======================================================
    # A(B + C) = AB + AC
    # ======================================================

    if propiedad == "distributiva_izquierda":

        if (
            matriz_b is None
            or matriz_c is None
        ):

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A, B y C."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        matriz_c = convertir_matriz(
            matriz_c
        )

        return verificar_distributiva_izquierda(
            matriz_a,
            matriz_b,
            matriz_c
        )

    # ======================================================
    # (B + C)A = BA + CA
    # ======================================================

    if propiedad == "distributiva_derecha":

        if (
            matriz_b is None
            or matriz_c is None
        ):

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A, B y C."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        matriz_c = convertir_matriz(
            matriz_c
        )

        return verificar_distributiva_derecha(
            matriz_a,
            matriz_b,
            matriz_c
        )

    # ======================================================
    # r(AB) = (rA)B = A(rB)
    # ======================================================

    if propiedad == "escalar_producto":

        if matriz_b is None:

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A y B."
            )

        if escalar is None:

            raise ValueError(
                "Esta propiedad requiere "
                "un escalar."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        escalar = convertir_a_fraccion(
            escalar
        )

        return verificar_escalar_producto(
            matriz_a,
            matriz_b,
            escalar
        )

    # ======================================================
    # IA = A = AI
    # ======================================================

    if propiedad == "identidad":

        return verificar_identidad_multiplicacion(
            matriz_a
        )

    # ======================================================
    # (Aᵀ)ᵀ = A
    # ======================================================

    if propiedad == "transpuesta_doble":

        return verificar_transpuesta_doble(
            matriz_a
        )

    # ======================================================
    # (A + B)ᵀ = Aᵀ + Bᵀ
    # ======================================================

    if propiedad == "transpuesta_suma":

        if matriz_b is None:

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A y B."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        return verificar_transpuesta_suma(
            matriz_a,
            matriz_b
        )

    # ======================================================
    # (rA)ᵀ = rAᵀ
    # ======================================================

    if propiedad == "transpuesta_escalar":

        if escalar is None:

            raise ValueError(
                "Esta propiedad requiere "
                "un escalar."
            )

        escalar = convertir_a_fraccion(
            escalar
        )

        return verificar_transpuesta_escalar(
            matriz_a,
            escalar
        )

    # ======================================================
    # (AB)ᵀ = BᵀAᵀ
    # ======================================================

    if propiedad == "transpuesta_producto":

        if matriz_b is None:

            raise ValueError(
                "Esta propiedad requiere "
                "las matrices A y B."
            )

        matriz_b = convertir_matriz(
            matriz_b
        )

        return verificar_transpuesta_producto(
            matriz_a,
            matriz_b
        )

    raise ValueError(
        "La propiedad seleccionada "
        "no es válida."
    )