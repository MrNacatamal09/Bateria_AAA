from utilidades.estructuras_entrada import (
    convertir_vector,
    convertir_matriz
)

from utilidades.numeros import (
    convertir_a_fraccion
)

from programas.programa_3.resolver_programa_3 import (
    resolver_vectores,
    resolver_matrices,
    resolver_combinacion_lineal,
    resolver_ax_b
)

from programas.programa_3.propiedades_matriz import (
    verificar_propiedades_matriz
)


# ==========================================================
# OPERACIONES CON VECTORES
# ==========================================================

def procesar_vectores(
    operacion,
    vector_1=None,
    vector_2=None,
    escalar=None,
    vectores=None
):

    # ======================================================
    # SUMA O RESTA DE VARIOS VECTORES
    # ======================================================

    if vectores is not None:

        vectores_convertidos = []

        for vector in vectores:

            vectores_convertidos.append(
                convertir_vector(
                    vector
                )
            )

        return resolver_vectores(
            operacion,
            vectores=vectores_convertidos
        )

    # ======================================================
    # PRIMER VECTOR
    # ======================================================

    if vector_1 is not None:

        vector_1 = convertir_vector(
            vector_1
        )

    # ======================================================
    # SEGUNDO VECTOR
    # ======================================================

    if vector_2 is not None:

        vector_2 = convertir_vector(
            vector_2
        )

    # ======================================================
    # ESCALAR
    # ======================================================

    if escalar is not None:

        escalar = convertir_a_fraccion(
            escalar
        )

    return resolver_vectores(
        operacion,
        vector_1,
        vector_2,
        escalar
    )


# ==========================================================
# OPERACIONES CON MATRICES
# ==========================================================

def procesar_matrices(
    operacion,
    matriz_1,
    matriz_2=None,
    escalar=None
):

    matriz_1 = convertir_matriz(
        matriz_1
    )

    if matriz_2 is not None:

        matriz_2 = convertir_matriz(
            matriz_2
        )

    if escalar is not None:

        escalar = convertir_a_fraccion(
            escalar
        )

    return resolver_matrices(
        operacion,
        matriz_1,
        matriz_2,
        escalar
    )


# ==========================================================
# COMBINACIÓN LINEAL
# ==========================================================

def procesar_combinacion_lineal(
    vectores,
    vector_b
):

    vectores_convertidos = []

    for vector in vectores:

        vectores_convertidos.append(
            convertir_vector(
                vector
            )
        )

    vector_b = convertir_vector(
        vector_b
    )

    return resolver_combinacion_lineal(
        vectores_convertidos,
        vector_b
    )


# ==========================================================
# ECUACIÓN MATRICIAL Ax = b
# ==========================================================

def procesar_ecuacion_matricial(
    matriz_a,
    vector_b
):

    matriz_a = convertir_matriz(
        matriz_a
    )

    vector_b = convertir_vector(
        vector_b
    )

    return resolver_ax_b(
        matriz_a,
        vector_b
    )


# ==========================================================
# PROPIEDADES DE A
# ==========================================================

def procesar_propiedades_matriz(
    operacion,
    matriz_a,
    vector_u,
    vector_v=None,
    escalar=None
):

    # ======================================================
    # MATRIZ A
    # ======================================================

    matriz_a = convertir_matriz(
        matriz_a
    )

    # ======================================================
    # VECTOR u
    # ======================================================

    vector_u = convertir_vector(
        vector_u
    )

    # ======================================================
    # VECTOR v
    #
    # Solo se convierte cuando la propiedad seleccionada
    # necesita el vector v.
    # ======================================================

    if vector_v is not None:

        vector_v = convertir_vector(
            vector_v
        )

    # ======================================================
    # ESCALAR c
    #
    # Solo se convierte cuando la propiedad seleccionada
    # necesita un escalar.
    # ======================================================

    if escalar is not None:

        escalar = convertir_a_fraccion(
            escalar
        )

    # ======================================================
    # MOTOR MATEMÁTICO
    # ======================================================

    return verificar_propiedades_matriz(
        operacion,
        matriz_a,
        vector_u,
        vector_v,
        escalar
    )