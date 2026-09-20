import re


# Convertimos números normales a subíndices Unicode
def convertir_numero_subindice(numero):

    equivalencias = str.maketrans(
        "0123456789",
        "₀₁₂₃₄₅₆₇₈₉"
    )

    return str(numero).translate(
        equivalencias
    )


# Obtenemos el nombre visual de una variable
# El índice recibido comienza desde 0
# Ejemplo:
# 0 -> x₁
# 1 -> x₂
# 2 -> x₃
def nombre_variable(indice):

    return (
        "x"
        + convertir_numero_subindice(
            indice + 1
        )
    )


# Obtenemos el nombre visual de un parámetro
# El índice recibido comienza desde 0
# Ejemplo:
# 0 -> t₁
# 1 -> t₂
# 2 -> t₃
def nombre_parametro(indice):

    return (
        "t"
        + convertir_numero_subindice(
            indice + 1
        )
    )


# Convertimos expresiones escritas con x1, x2, x3...
# y t1, t2, t3... a notación con subíndices
def formatear_texto_matematico(texto):

    texto = str(texto)

    def reemplazar_variable(coincidencia):

        letra = coincidencia.group(1)
        numero = coincidencia.group(2)

        return (
            letra
            + convertir_numero_subindice(
                numero
            )
        )

    texto = re.sub(
        r"\b([xt])(\d+)\b",
        reemplazar_variable,
        texto
    )

    return texto