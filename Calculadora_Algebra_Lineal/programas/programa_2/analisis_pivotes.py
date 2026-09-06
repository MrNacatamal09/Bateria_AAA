# Obtenemos todas las columnas pivote de la matriz aumentada
def obtener_columnas_pivote(posiciones_pivote):

    return [
        j
        for i, j in posiciones_pivote
    ]


# Obtenemos solamente las columnas pivote
# correspondientes a variables
def obtener_columnas_pivote_variables(
    columnas_pivote,
    numero_variables
):

    return [
        j
        for j in columnas_pivote
        if j < numero_variables
    ]


# Revisamos si existe un pivote
# en la columna aumentada
def existe_pivote_columna_aumentada(
    columnas_pivote,
    numero_variables
):

    return numero_variables in columnas_pivote


# Identificamos las variables básicas
def obtener_variables_basicas(
    columnas_pivote_variables
):

    return list(
        columnas_pivote_variables
    )


# Identificamos las variables libres
def obtener_variables_libres(
    variables_basicas,
    numero_variables
):

    variables_libres = []

    for j in range(numero_variables):

        if j not in variables_basicas:

            variables_libres.append(j)

    return variables_libres


# Reunimos toda la información de los pivotes
def analizar_pivotes(
    posiciones_pivote,
    numero_variables
):

    columnas_pivote_matriz = (
        obtener_columnas_pivote(
            posiciones_pivote
        )
    )

    columnas_pivote_variables = (
        obtener_columnas_pivote_variables(
            columnas_pivote_matriz,
            numero_variables
        )
    )

    variables_basicas = (
        obtener_variables_basicas(
            columnas_pivote_variables
        )
    )

    variables_libres = (
        obtener_variables_libres(
            variables_basicas,
            numero_variables
        )
    )

    pivote_columna_aumentada = (
        existe_pivote_columna_aumentada(
            columnas_pivote_matriz,
            numero_variables
        )
    )

    return {
        "columnas_pivote":
            columnas_pivote_variables,

        "columnas_pivote_matriz":
            columnas_pivote_matriz,

        "pivote_columna_aumentada":
            pivote_columna_aumentada,

        "variables_basicas":
            variables_basicas,

        "variables_libres":
            variables_libres
    }