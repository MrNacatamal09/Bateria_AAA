from utilidades.estructuras_entrada import (
    convertir_vector,
    convertir_matriz
)

from utilidades.numeros import convertir_a_fraccion

from programas.programa_3.resolver_programa_3 import (
    resolver_vectores,
    resolver_matrices,
    resolver_combinacion_lineal,
    resolver_ax_b
)


# Preparamos y ejecutamos una operación vectorial
def procesar_vectores(
    operacion,
    vector_1=None,
    vector_2=None,
    escalar=None,
    vectores=None
):

    # Para suma de varios vectores
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

    # Operaciones tradicionales
    if vector_1 is not None:

        vector_1 = convertir_vector(
            vector_1
        )

    if vector_2 is not None:

        vector_2 = convertir_vector(
            vector_2
        )

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


# Preparamos y ejecutamos una operación matricial
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


# Preparamos y evaluamos una combinación lineal
def procesar_combinacion_lineal(
    vectores,
    vector_b
):

    vectores_convertidos = []

    for i in range(len(vectores)):

        vectores_convertidos.append(
            convertir_vector(
                vectores[i]
            )
        )

    vector_b = convertir_vector(
        vector_b
    )

    return resolver_combinacion_lineal(
        vectores_convertidos,
        vector_b
    )


# Preparamos y resolvemos una ecuación matricial Ax = b
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