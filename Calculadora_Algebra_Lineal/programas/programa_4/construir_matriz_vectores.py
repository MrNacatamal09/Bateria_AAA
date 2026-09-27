# ==========================================================
# PROGRAMA 4
# CONSTRUCCIÓN DE LA MATRIZ DE VECTORES
# ==========================================================


def validar_vectores(
    vectores
):

    if not vectores:

        raise ValueError(
            "Debe ingresar al menos un vector."
        )

    dimension = len(
        vectores[0]
    )

    if dimension == 0:

        raise ValueError(
            "Los vectores deben tener al menos "
            "una componente."
        )

    for vector in vectores:

        if len(vector) != dimension:

            raise ValueError(
                "Todos los vectores deben tener "
                "la misma dimensión."
            )


def construir_matriz_columnas(
    vectores
):

    validar_vectores(
        vectores
    )

    cantidad_vectores = len(
        vectores
    )

    dimension = len(
        vectores[0]
    )

    matriz = []

    # i representa la componente del vector.
    for i in range(
        dimension
    ):

        fila = []

        # j representa el vector.
        for j in range(
            cantidad_vectores
        ):

            fila.append(
                vectores[j][i]
            )

        matriz.append(
            fila
        )

    return matriz


def construir_matriz_homogenea(
    vectores
):

    matriz_a = construir_matriz_columnas(
        vectores
    )

    matriz_aumentada = []

    for fila in matriz_a:

        nueva_fila = list(
            fila
        )

        # Sistema homogéneo Ax = 0
        nueva_fila.append(
            0
        )

        matriz_aumentada.append(
            nueva_fila
        )

    return matriz_aumentada