from .numeros import convertir_a_fraccion


# Convertimos los datos de un vector
def convertir_vector(datos):

    if not datos:
        raise ValueError(
            "El vector no puede estar vacío."
        )

    vector = []

    for i in range(len(datos)):

        try:
            vector.append(
                convertir_a_fraccion(datos[i])
            )

        except ValueError as error:
            raise ValueError(
                f"Error en la componente {i + 1}: "
                f"{error}"
            ) from None

    return vector


# Convertimos los datos de una matriz
def convertir_matriz(datos):

    if not datos:
        raise ValueError(
            "La matriz no puede estar vacía."
        )

    if not datos[0]:
        raise ValueError(
            "La matriz debe tener al menos una columna."
        )

    numero_columnas = len(datos[0])
    matriz = []

    # i representa las filas
    for i in range(len(datos)):

        if len(datos[i]) != numero_columnas:
            raise ValueError(
                "Todas las filas deben tener "
                "la misma cantidad de columnas."
            )

        fila = []

        # j representa las columnas
        for j in range(numero_columnas):

            try:
                fila.append(
                    convertir_a_fraccion(
                        datos[i][j]
                    )
                )

            except ValueError as error:
                raise ValueError(
                    f"Error en la fila {i + 1}, "
                    f"columna {j + 1}: {error}"
                ) from None

        matriz.append(fila)

    return matriz