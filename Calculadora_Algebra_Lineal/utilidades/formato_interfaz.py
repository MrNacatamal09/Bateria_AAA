# Convertimos números normales a caracteres de subíndice
def convertir_a_subindice(numero):

    equivalencias = {
        "0": "₀",
        "1": "₁",
        "2": "₂",
        "3": "₃",
        "4": "₄",
        "5": "₅",
        "6": "₆",
        "7": "₇",
        "8": "₈",
        "9": "₉"
    }

    resultado = ""

    for caracter in str(numero):
        resultado += equivalencias.get(
            caracter,
            caracter
        )

    return resultado


# Creamos el nombre visual de una variable
def nombre_variable(numero):

    return (
        "x"
        + convertir_a_subindice(numero)
    )


# Convertimos x1, x2, t1... dentro de un texto
def formatear_texto_matematico(texto):

    texto = str(texto)

    resultado = ""
    i = 0

    while i < len(texto):

        caracter = texto[i]

        # Buscamos variables x o parámetros t
        if (
            caracter in ("x", "t")
            and i + 1 < len(texto)
            and texto[i + 1].isdigit()
        ):

            resultado += caracter
            i += 1

            numero = ""

            while (
                i < len(texto)
                and texto[i].isdigit()
            ):

                numero += texto[i]
                i += 1

            resultado += convertir_a_subindice(
                numero
            )

            continue

        resultado += caracter
        i += 1

    return resultado