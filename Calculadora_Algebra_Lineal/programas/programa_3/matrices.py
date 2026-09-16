from fractions import Fraction


# Revisamos que una matriz tenga filas y columnas válidas
def validar_matriz(matriz):

    if not matriz:
        raise ValueError(
            "La matriz no puede estar vacía."
        )

    columnas = len(matriz[0])

    if columnas == 0:
        raise ValueError(
            "La matriz debe tener al menos una columna."
        )

    for i in range(len(matriz)):

        if len(matriz[i]) != columnas:
            raise ValueError(
                "Todas las filas deben tener "
                "la misma cantidad de columnas."
            )


# Revisamos que dos matrices tengan las mismas dimensiones
def validar_mismas_dimensiones(matriz_1, matriz_2):

    validar_matriz(matriz_1)
    validar_matriz(matriz_2)

    mismas_filas = (
        len(matriz_1) == len(matriz_2)
    )

    mismas_columnas = (
        len(matriz_1[0]) == len(matriz_2[0])
    )

    if not (
        mismas_filas
        and mismas_columnas
    ):
        raise ValueError(
            "Las matrices deben tener "
            "las mismas dimensiones."
        )


# Sumamos dos matrices elemento a elemento
def sumar_matrices(matriz_1, matriz_2):

    validar_mismas_dimensiones(
        matriz_1,
        matriz_2
    )

    resultado = []

    for i in range(len(matriz_1)):
        fila = []

        for j in range(len(matriz_1[i])):

            fila.append(
                matriz_1[i][j]
                + matriz_2[i][j]
            )

        resultado.append(fila)

    return resultado


# Restamos dos matrices elemento a elemento
def restar_matrices(matriz_1, matriz_2):

    validar_mismas_dimensiones(
        matriz_1,
        matriz_2
    )

    resultado = []

    for i in range(len(matriz_1)):
        fila = []

        for j in range(len(matriz_1[i])):

            fila.append(
                matriz_1[i][j]
                - matriz_2[i][j]
            )

        resultado.append(fila)

    return resultado


# Multiplicamos una matriz por un escalar
def multiplicar_matriz_escalar(matriz, escalar):

    validar_matriz(matriz)

    escalar = Fraction(escalar)
    resultado = []

    for i in range(len(matriz)):
        fila = []

        for j in range(len(matriz[i])):

            fila.append(
                matriz[i][j] * escalar
            )

        resultado.append(fila)

    return resultado


# Revisamos si dos matrices se pueden multiplicar
def validar_multiplicacion(matriz_1, matriz_2):

    validar_matriz(matriz_1)
    validar_matriz(matriz_2)

    columnas_matriz_1 = len(matriz_1[0])
    filas_matriz_2 = len(matriz_2)

    if columnas_matriz_1 != filas_matriz_2:
        raise ValueError(
            "Las columnas de la primera matriz "
            "deben ser iguales a las filas "
            "de la segunda matriz."
        )


# Multiplicamos dos matrices
def multiplicar_matrices(matriz_1, matriz_2):

    validar_multiplicacion(
        matriz_1,
        matriz_2
    )

    filas_resultado = len(matriz_1)
    columnas_resultado = len(matriz_2[0])
    dimension_comun = len(matriz_2)

    resultado = []

    # i recorre las filas de la primera matriz
    for i in range(filas_resultado):
        fila = []

        # j recorre las columnas de la segunda matriz
        for j in range(columnas_resultado):

            valor = 0

            # k recorre la dimensión compartida
            for k in range(dimension_comun):

                valor += (
                    matriz_1[i][k]
                    * matriz_2[k][j]
                )

            fila.append(valor)

        resultado.append(fila)

    return resultado