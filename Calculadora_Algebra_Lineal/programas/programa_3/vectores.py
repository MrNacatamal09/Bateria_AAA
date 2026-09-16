from fractions import Fraction


# Revisamos que dos vectores tengan la misma dimensión
def validar_misma_dimension(vector_1, vector_2):

    if len(vector_1) != len(vector_2):
        raise ValueError(
            "Los vectores deben tener la misma dimensión."
        )


# Sumamos dos vectores componente a componente
def sumar_vectores(vector_1, vector_2):

    validar_misma_dimension(
        vector_1,
        vector_2
    )

    resultado = []

    for i in range(len(vector_1)):
        resultado.append(
            vector_1[i] + vector_2[i]
        )

    return resultado


# Restamos dos vectores componente a componente
def restar_vectores(vector_1, vector_2):

    validar_misma_dimension(
        vector_1,
        vector_2
    )

    resultado = []

    for i in range(len(vector_1)):
        resultado.append(
            vector_1[i] - vector_2[i]
        )

    return resultado


# Multiplicamos un vector por un escalar
def multiplicar_vector_escalar(vector, escalar):

    escalar = Fraction(escalar)

    resultado = []

    for i in range(len(vector)):
        resultado.append(
            vector[i] * escalar
        )

    return resultado