from .numeros import convertir_a_fraccion


# Revisamos que la cantidad de ecuaciones sea válida
def validar_numero_ecuaciones(numero_ecuaciones):

    if not isinstance(numero_ecuaciones, int) or numero_ecuaciones <= 0:
        raise ValueError(
            "El número de ecuaciones debe ser un entero mayor que cero."
        )


# Revisamos que la cantidad de variables sea válida
def validar_numero_variables(numero_variables):

    if not isinstance(numero_variables, int) or numero_variables <= 0:
        raise ValueError(
            "El número de variables debe ser un entero mayor que cero."
        )


# Convertimos los datos en una matriz aumentada
def construir_matriz_aumentada(
    datos,
    numero_ecuaciones,
    numero_variables
):

    validar_numero_ecuaciones(numero_ecuaciones)
    validar_numero_variables(numero_variables)

    if len(datos) != numero_ecuaciones:
        raise ValueError(
            "La cantidad de filas no coincide "
            "con el número de ecuaciones."
        )

    columnas_esperadas = numero_variables + 1
    matriz = []

    # i representa las filas
    for i in range(numero_ecuaciones):

        if len(datos[i]) != columnas_esperadas:
            raise ValueError(
                f"La ecuación {i + 1} debe contener "
                f"{columnas_esperadas} valores."
            )

        fila = []

        # j representa las columnas
        for j in range(columnas_esperadas):

            try:
                valor = convertir_a_fraccion(
                    datos[i][j]
                )

            except ValueError as error:
                raise ValueError(
                    f"Error en la fila {i + 1}, "
                    f"columna {j + 1}: {error}"
                ) from None

            fila.append(valor)

        matriz.append(fila)

    return matriz