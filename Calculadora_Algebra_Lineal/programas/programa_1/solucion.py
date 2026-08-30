from fractions import Fraction

from .clasificacion import clasificar_sistema


# Buscamos la columna pivote de una fila
def buscar_pivote_fila(fila, numero_variables):

    for j in range(numero_variables):

        if fila[j] != 0:
            return j

    return None


# Preparamos las variables libres y sus parámetros
def crear_variables_libres(variables_libres):
    expresiones = {}
    parametros = {}

    for numero, j in enumerate(variables_libres):

        parametro = f"t{numero + 1}"

        parametros[j] = parametro

        expresiones[j] = {
            "constante": Fraction(0),
            "parametros": {
                j: Fraction(1)
            }
        }

    return expresiones, parametros


# Obtenemos la solución desde la matriz escalonada
def obtener_solucion(matriz_escalonada, numero_variables):

    clasificacion = clasificar_sistema(
        matriz_escalonada,
        numero_variables
    )

    # Si existe contradicción, no hay solución
    if clasificacion["tipo"] == "inconsistente":
        return {
            "tipo": "inconsistente",
            "clasificacion": clasificacion,
            "expresiones": {},
            "parametros": {}
        }

    expresiones, parametros = crear_variables_libres(
        clasificacion["variables_libres"]
    )

    # Sustituimos desde la última fila hacia arriba
    for i in range(len(matriz_escalonada) - 1, -1, -1):

        fila = matriz_escalonada[i]

        j_pivote = buscar_pivote_fila(
            fila,
            numero_variables
        )

        if j_pivote is None:
            continue

        pivote = fila[j_pivote]

        constante = (
            fila[numero_variables] / pivote
        )

        parametros_actuales = {}

        # Sustituimos las variables a la derecha del pivote
        for j in range(j_pivote + 1, numero_variables):

            coeficiente = fila[j] / pivote

            if coeficiente == 0:
                continue

            expresion = expresiones[j]

            constante -= (
                coeficiente
                * expresion["constante"]
            )

            # Agregamos los términos con parámetros
            for variable_libre, valor in (
                expresion["parametros"].items()
            ):

                parametros_actuales[variable_libre] = (
                    parametros_actuales.get(
                        variable_libre,
                        Fraction(0)
                    )
                    - coeficiente * valor
                )

        expresiones[j_pivote] = {
            "constante": constante,
            "parametros": parametros_actuales
        }

    return {
        "tipo": clasificacion["tipo"],
        "clasificacion": clasificacion,
        "expresiones": expresiones,
        "parametros": parametros
    }


# Convertimos una expresión matemática a texto
def expresion_a_texto(expresion, parametros):

    constante = expresion["constante"]
    terminos = expresion["parametros"]

    partes = []

    if constante != 0 or not terminos:
        partes.append(str(constante))

    for variable_libre, coeficiente in terminos.items():

        if coeficiente == 0:
            continue

        parametro = parametros[variable_libre]

        # Primer término de la expresión
        if not partes:

            if coeficiente == 1:
                partes.append(parametro)

            elif coeficiente == -1:
                partes.append(f"-{parametro}")

            else:
                partes.append(
                    f"{coeficiente}{parametro}"
                )

            continue

        # Términos positivos
        if coeficiente > 0:

            if coeficiente == 1:
                partes.append(f"+ {parametro}")

            else:
                partes.append(
                    f"+ {coeficiente}{parametro}"
                )

        # Términos negativos
        else:

            valor = -coeficiente

            if valor == 1:
                partes.append(f"- {parametro}")

            else:
                partes.append(
                    f"- {valor}{parametro}"
                )

    return " ".join(partes)


# Preparamos la solución para mostrarla
def formatear_solucion(resultado, numero_variables):

    if resultado["tipo"] == "inconsistente":
        return ["El sistema no tiene solución."]

    expresiones = resultado["expresiones"]
    parametros = resultado["parametros"]

    lineas = []

    for j in range(numero_variables):

        # Mostramos directamente las variables libres
        if j in parametros:
            lineas.append(
                f"x{j + 1} = {parametros[j]}"
            )
            continue

        texto = expresion_a_texto(
            expresiones[j],
            parametros
        )

        lineas.append(
            f"x{j + 1} = {texto}"
        )

    return lineas