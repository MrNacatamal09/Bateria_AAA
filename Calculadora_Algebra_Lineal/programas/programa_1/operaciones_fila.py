from fractions import Fraction


# Intercambiamos dos filas de la matriz
def intercambiar_filas(matriz, i_1, i_2):
    matriz[i_1], matriz[i_2] = matriz[i_2], matriz[i_1]


# Multiplicamos una fila por un escalar
def multiplicar_fila(matriz, i, escalar):
    escalar = Fraction(escalar)

    if escalar == 0:
        raise ValueError("El escalar no puede ser cero.")

    for j in range(len(matriz[i])):
        matriz[i][j] *= escalar


# Sumamos a una fila un múltiplo de otra
def sumar_multiplo_fila(matriz, i_destino, i_origen, escalar):
    escalar = Fraction(escalar)

    for j in range(len(matriz[i_destino])):
        matriz[i_destino][j] += (
            escalar * matriz[i_origen][j]
        )