from controladores.programa_3_controller import (
    procesar_vectores,
    procesar_matrices,
    procesar_combinacion_lineal,
    procesar_ecuacion_matricial
)


# Mostramos un vector
def mostrar_vector(vector):
    print(
        "[ "
        + "   ".join(
            str(valor)
            for valor in vector
        )
        + " ]"
    )


# Mostramos una matriz
def mostrar_matriz(matriz):

    for i in range(len(matriz)):
        print(
            "[ "
            + "   ".join(
                str(matriz[i][j])
                for j in range(len(matriz[i]))
            )
            + " ]"
        )


# Probamos operaciones con vectores
def probar_vectores():

    print("\n" + "=" * 50)
    print("PRUEBA 1 - OPERACIONES CON VECTORES")
    print("=" * 50)

    vector_1 = [
        "1",
        "2/3",
        "-3"
    ]

    vector_2 = [
        "4",
        "1/3",
        "2"
    ]

    suma = procesar_vectores(
        "suma",
        vector_1,
        vector_2
    )

    resta = procesar_vectores(
        "resta",
        vector_1,
        vector_2
    )

    escalar = procesar_vectores(
        "escalar",
        vector_1,
        escalar="3/2"
    )

    print("\nSuma:")
    mostrar_vector(
        suma["resultado"]
    )

    print("\nResta:")
    mostrar_vector(
        resta["resultado"]
    )

    print("\nMultiplicación por 3/2:")
    mostrar_vector(
        escalar["resultado"]
    )


# Probamos operaciones con matrices
def probar_matrices():

    print("\n" + "=" * 50)
    print("PRUEBA 2 - OPERACIONES CON MATRICES")
    print("=" * 50)

    matriz_1 = [
        ["1", "2"],
        ["3/2", "4"]
    ]

    matriz_2 = [
        ["5", "6"],
        ["7", "8"]
    ]

    suma = procesar_matrices(
        "suma",
        matriz_1,
        matriz_2
    )

    resta = procesar_matrices(
        "resta",
        matriz_1,
        matriz_2
    )

    escalar = procesar_matrices(
        "escalar",
        matriz_1,
        escalar="2"
    )

    multiplicacion = procesar_matrices(
        "multiplicacion",
        matriz_1,
        matriz_2
    )

    print("\nSuma:")
    mostrar_matriz(
        suma["resultado"]
    )

    print("\nResta:")
    mostrar_matriz(
        resta["resultado"]
    )

    print("\nMultiplicación por escalar:")
    mostrar_matriz(
        escalar["resultado"]
    )

    print("\nMultiplicación de matrices:")
    mostrar_matriz(
        multiplicacion["resultado"]
    )


# Probamos dimensiones incompatibles
def probar_dimensiones_incompatibles():

    print("\n" + "=" * 50)
    print("PRUEBA 3 - DIMENSIONES INCOMPATIBLES")
    print("=" * 50)

    matriz_1 = [
        ["1", "2", "3"],
        ["4", "5", "6"]
    ]

    matriz_2 = [
        ["1", "2"],
        ["3", "4"]
    ]

    try:
        procesar_matrices(
            "multiplicacion",
            matriz_1,
            matriz_2
        )

    except ValueError as error:
        print("\nValidación correcta:")
        print(error)


# Probamos una combinación lineal
def probar_combinacion_lineal():

    print("\n" + "=" * 50)
    print("PRUEBA 4 - COMBINACIÓN LINEAL")
    print("=" * 50)

    vectores = [
        ["1", "2"],
        ["3", "1"]
    ]

    vector_b = [
        "7",
        "5"
    ]

    resultado = procesar_combinacion_lineal(
        vectores,
        vector_b
    )["resultado"]

    print("\n¿Es combinación lineal?")

    if resultado["es_combinacion"]:

        print("Sí")

        print("\nCoeficientes:")

        for linea in resultado["coeficientes"]:
            print(linea)

    else:
        print("No")


# Probamos la ecuación matricial Ax = b
def probar_ecuacion_matricial():

    print("\n" + "=" * 50)
    print("PRUEBA 5 - ECUACIÓN MATRICIAL Ax = b")
    print("=" * 50)

    matriz_a = [
        ["1", "2"],
        ["3", "4"]
    ]

    vector_b = [
        "5",
        "11"
    ]

    resultado = procesar_ecuacion_matricial(
        matriz_a,
        vector_b
    )["resultado"]

    print("\nMatriz reducida:")
    mostrar_matriz(
        resultado["matriz_reducida"]
    )

    print("\nSolución:")

    for linea in resultado["solucion_formateada"]:
        print(linea)

    print("\nVerificación:")
    print(
        resultado["verificacion"]
    )


# Ejecutamos todas las pruebas
def main():

    print("\nPROGRAMA 3 - PRUEBAS GENERALES")

    probar_vectores()
    probar_matrices()
    probar_dimensiones_incompatibles()
    probar_combinacion_lineal()
    probar_ecuacion_matricial()


if __name__ == "__main__":
    main()