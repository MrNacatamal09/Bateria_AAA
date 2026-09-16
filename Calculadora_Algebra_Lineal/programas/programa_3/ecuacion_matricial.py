from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)


# Revisamos que A y b tengan dimensiones válidas
def validar_ecuacion_matricial(matriz_a, vector_b):

    if not matriz_a:
        raise ValueError(
            "La matriz A no puede estar vacía."
        )

    if not vector_b:
        raise ValueError(
            "El vector b no puede estar vacío."
        )

    numero_columnas = len(matriz_a[0])

    if numero_columnas == 0:
        raise ValueError(
            "La matriz A debe tener al menos una columna."
        )

    # Revisamos que A sea una matriz rectangular
    for i in range(len(matriz_a)):

        if len(matriz_a[i]) != numero_columnas:
            raise ValueError(
                "Todas las filas de A deben tener "
                "la misma cantidad de columnas."
            )

    # b debe tener una entrada por cada fila de A
    if len(vector_b) != len(matriz_a):
        raise ValueError(
            "El vector b debe tener la misma cantidad "
            "de elementos que filas tiene A."
        )


# Construimos la matriz aumentada [A|b]
def construir_matriz_aumentada(matriz_a, vector_b):

    validar_ecuacion_matricial(
        matriz_a,
        vector_b
    )

    matriz_aumentada = []

    # i representa las filas
    for i in range(len(matriz_a)):

        fila = []

        # j representa las columnas de A
        for j in range(len(matriz_a[i])):
            fila.append(
                matriz_a[i][j]
            )

        fila.append(
            vector_b[i]
        )

        matriz_aumentada.append(fila)

    return matriz_aumentada


# Resolvemos la ecuación matricial Ax = b
def resolver_ecuacion_matricial(matriz_a, vector_b):

    matriz_aumentada = construir_matriz_aumentada(
        matriz_a,
        vector_b
    )

    numero_variables = len(matriz_a[0])

    resultado = resolver_programa_2(
        matriz_aumentada,
        numero_variables
    )

    return {
        "matriz_a": matriz_a,
        "vector_b": vector_b,
        "matriz_aumentada": matriz_aumentada,
        "tipo": resultado["tipo"],
        "solucion": resultado["solucion"],
        "solucion_formateada": resultado[
            "solucion_formateada"
        ],
        "matriz_reducida": resultado[
            "matriz_reducida"
        ],
        "columnas_pivote": resultado[
            "columnas_pivote"
        ],
        "variables_basicas": resultado[
            "variables_basicas"
        ],
        "variables_libres": resultado[
            "variables_libres"
        ],
        "historial": resultado["historial"],
        "verificacion": resultado["verificacion"]
    }