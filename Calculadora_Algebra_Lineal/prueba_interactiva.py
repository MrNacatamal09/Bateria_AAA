from controladores.programa_1_controller import procesar_sistema


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


# Permitimos seleccionar el método
def pedir_metodo():

    while True:
        print("\nSeleccione el método:")
        print("1. Gauss")
        print("2. Gauss-Jordan")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            return "gauss"

        if opcion == "2":
            return "gauss_jordan"

        print("Seleccione una opción válida.")


# Pedimos los valores de la matriz aumentada
def pedir_datos_matriz(numero_ecuaciones, numero_variables):
    datos = []

    print("\nINGRESO DE LA MATRIZ AUMENTADA")
    print(
        "Puede ingresar enteros, decimales "
        "o fracciones como 3/4."
    )

    # i representa las filas
    for i in range(numero_ecuaciones):
        fila = []

        print(f"\nEcuación {i + 1}")

        # j representa las columnas de las variables
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


# Mostramos el procedimiento realizado
def mostrar_procedimiento(historial):

    print("\nProcedimiento:")

    for numero, paso in enumerate(historial, start=1):

        print(
            f"\nPaso {numero}: "
            f"{paso['operacion']}"
        )

        mostrar_matriz(
            paso["matriz"]
        )

        # Comprobamos las operaciones elementales
        if paso["verificada"] is True:
            print("Comprobación del paso: Correcto")

        elif paso["verificada"] is False:
            print("Comprobación del paso: Incorrecto")


# Mostramos la verificación de la solución
def mostrar_verificacion(verificacion):

    if not verificacion["aplica"]:
        return

    print("\nVerificación de la solución:")

    for ecuacion in verificacion["ecuaciones"]:

        print(
            f"Ecuación {ecuacion['ecuacion']}: "
            f"{ecuacion['lado_izquierdo']} = "
            f"{ecuacion['lado_derecho']}"
        )

    if verificacion["correcta"]:
        print(
            "La solución fue verificada correctamente."
        )

    else:
        print(
            "La solución no pasó la verificación."
        )


# Mostramos toda la información obtenida
def mostrar_resultado(resultado):

    print("\n" + "=" * 50)
    print("RESULTADO")
    print("=" * 50)

    print("\nMétodo utilizado:")

    if resultado["metodo"] == "gauss":
        print("Gauss")
    else:
        print("Gauss-Jordan")

    print("\nMatriz inicial:")
    mostrar_matriz(
        resultado["matriz_original"]
    )

    mostrar_procedimiento(
        resultado["historial"]
    )

    print("\nMatriz resultante:")
    mostrar_matriz(
        resultado["matriz_resultado"]
    )

    print("\nClasificación:")
    print(
        resultado["clasificacion"]["nombre"]
    )
    print(
        resultado["clasificacion"]["descripcion"]
    )

    print("\nSolución:")

    for linea in resultado["solucion_formateada"]:
        print(linea)

    mostrar_verificacion(
        resultado["verificacion"]
    )


# Iniciamos la prueba interactiva
def main():

    print("\nCALCULADORA DE ÁLGEBRA LINEAL")
    print(
        "Programa 1 - Sistemas de ecuaciones lineales"
    )

    numero_ecuaciones = pedir_entero_positivo(
        "\nNúmero de ecuaciones: "
    )

    numero_variables = pedir_entero_positivo(
        "Número de variables: "
    )

    metodo = pedir_metodo()

    datos = pedir_datos_matriz(
        numero_ecuaciones,
        numero_variables
    )

    try:
        resultado = procesar_sistema(
            datos,
            numero_ecuaciones,
            numero_variables,
            metodo
        )

        mostrar_resultado(resultado)

    except ValueError as error:
        print("\nERROR")
        print(error)


if __name__ == "__main__":
    main()