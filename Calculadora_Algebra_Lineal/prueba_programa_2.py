from controladores.programa_2_controller import procesar_programa_2


# Pedimos un número entero positivo
def pedir_entero_positivo(mensaje):

    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero

            print("El valor debe ser mayor que cero.")

        except ValueError:
            print("Debe ingresar un número entero.")


# Pedimos los valores de la matriz aumentada
def pedir_datos_matriz(numero_ecuaciones, numero_variables):
    datos = []

    print("\nINGRESO DE LA MATRIZ AUMENTADA")
    print(
        "Puede ingresar enteros, decimales "
        "o fracciones como 3/4."
    )

    for i in range(numero_ecuaciones):
        fila = []

        print(f"\nEcuación {i + 1}")

        for j in range(numero_variables):
            valor = input(
                f"Coeficiente de x{j + 1}: "
            )

            fila.append(valor)

        independiente = input(
            "Término independiente: "
        )

        fila.append(independiente)
        datos.append(fila)

    return datos


# Mostramos una matriz
def mostrar_matriz(matriz):

    for i in range(len(matriz)):
        valores = []

        for j in range(len(matriz[i])):
            valores.append(
                str(matriz[i][j])
            )

        print("[ " + "   ".join(valores) + " ]")


# Mostramos variables con formato x1, x2, x3...
def mostrar_variables(variables):

    if not variables:
        print("Ninguna")
        return

    texto = []

    for j in variables:
        texto.append(f"x{j + 1}")

    print(", ".join(texto))


# Mostramos el resultado completo
def mostrar_resultado(resultado):

    print("\n" + "=" * 50)
    print("PROGRAMA 2 - GAUSS-JORDAN")
    print("=" * 50)

    print("\nMatriz original:")
    mostrar_matriz(
        resultado["matriz_original"]
    )

    print("\nProcedimiento:")

    for numero, paso in enumerate(
        resultado["historial"],
        start=1
    ):

        print(
            f"\nPaso {numero}: "
            f"{paso['operacion']}"
        )

        mostrar_matriz(
            paso["matriz"]
        )

        if paso["verificada"] is True:
            print(
                "Comprobación del paso: Correcto"
            )

        elif paso["verificada"] is False:
            print(
                "Comprobación del paso: Incorrecto"
            )

    print("\nMatriz RREF:")
    mostrar_matriz(
        resultado["matriz_reducida"]
    )

    print("\nColumnas pivote:")

    columnas = []

    for j in resultado["columnas_pivote"]:
        columnas.append(
            str(j + 1)
        )

    print(", ".join(columnas))

    print("\nVariables básicas:")
    mostrar_variables(
        resultado["variables_basicas"]
    )

    print("\nVariables libres:")
    mostrar_variables(
        resultado["variables_libres"]
    )

    print("\nSolución:")

    for linea in resultado["solucion_formateada"]:
        print(linea)


# Iniciamos la prueba interactiva
def main():

    print("\nCALCULADORA DE ÁLGEBRA LINEAL")
    print(
        "Programa 2 - Reducción a RREF "
        "e identificación de pivotes"
    )

    numero_ecuaciones = pedir_entero_positivo(
        "\nNúmero de ecuaciones: "
    )

    numero_variables = pedir_entero_positivo(
        "Número de variables: "
    )

    datos = pedir_datos_matriz(
        numero_ecuaciones,
        numero_variables
    )

    try:
        resultado = procesar_programa_2(
            datos,
            numero_ecuaciones,
            numero_variables
        )

        mostrar_resultado(resultado)

    except ValueError as error:
        print("\nERROR")
        print(error)


if __name__ == "__main__":
    main()