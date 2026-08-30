from copy import deepcopy


# Verificamos un intercambio de filas
def verificar_intercambio(
    matriz_antes,
    matriz_despues,
    i_1,
    i_2
):
    esperada = deepcopy(matriz_antes)

    esperada[i_1], esperada[i_2] = (
        esperada[i_2],
        esperada[i_1]
    )

    return esperada == matriz_despues


# Verificamos la multiplicación de una fila
def verificar_escalamiento(
    matriz_antes,
    matriz_despues,
    i,
    escalar
):
    esperada = deepcopy(matriz_antes)

    for j in range(len(esperada[i])):
        esperada[i][j] *= escalar

    return esperada == matriz_despues


# Verificamos una operación Fi -> Fi + kFj
def verificar_reemplazo(
    matriz_antes,
    matriz_despues,
    i_destino,
    i_origen,
    escalar
):
    esperada = deepcopy(matriz_antes)

    for j in range(len(esperada[i_destino])):
        esperada[i_destino][j] = (
            matriz_antes[i_destino][j]
            + escalar * matriz_antes[i_origen][j]
        )

    return esperada == matriz_despues