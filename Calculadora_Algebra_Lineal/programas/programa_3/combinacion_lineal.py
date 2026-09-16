from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)


# Revisamos que los vectores tengan una dimensión válida
def validar_vectores(vectores, vector_b):

    if not vectores:
        raise ValueError(
            "Debe existir al menos un vector."
        )

    if not vector_b:
        raise ValueError(
            "El vector b no puede estar vacío."
        )

    dimension = len(vector_b)

    for i in range(len(vectores)):

        if len(vectores[i]) != dimension:
            raise ValueError(
                "Todos los vectores deben tener "
                "la misma dimensión que el vector b."
            )


# Construimos la matriz aumentada [A|b]
def construir_matriz_combinacion(vectores, vector_b):

    validar_vectores(
        vectores,
        vector_b
    )

    dimension = len(vector_b)
    numero_vectores = len(vectores)

    matriz = []

    # i representa cada componente o fila
    for i in range(dimension):
        fila = []

        # j representa cada vector o columna
        for j in range(numero_vectores):
            fila.append(
                vectores[j][i]
            )

        fila.append(
            vector_b[i]
        )

        matriz.append(fila)

    return matriz


# Evaluamos si b es combinación lineal de los vectores
def evaluar_combinacion_lineal(vectores, vector_b):

    matriz = construir_matriz_combinacion(
        vectores,
        vector_b
    )

    numero_vectores = len(vectores)

    # Los coeficientes de la combinación son las incógnitas
    resultado = resolver_programa_2(
        matriz,
        numero_vectores
    )

    es_combinacion = (
        resultado["tipo"] != "inconsistente"
    )

    return {
        "es_combinacion": es_combinacion,
        "matriz_aumentada": matriz,
        "resultado_sistema": resultado,
        "tipo": resultado["tipo"],
        "coeficientes": resultado[
            "solucion_formateada"
        ]
    }