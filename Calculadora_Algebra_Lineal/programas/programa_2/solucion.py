from .analisis_pivotes import analizar_pivotes


# Revisamos si existe una fila contradictoria
def es_inconsistente(matriz, numero_variables):

    for i in range(len(matriz)):
        coeficientes_cero = True

        for j in range(numero_variables):

            if matriz[i][j] != 0:
                coeficientes_cero = False
                break

        # Detectamos una fila del tipo 0 = b
        if (
            coeficientes_cero
            and matriz[i][numero_variables] != 0
        ):
            return True

    return False


# Asignamos un parámetro a cada variable libre
def crear_parametros(variables_libres):
    parametros = {}

    for numero, j in enumerate(variables_libres):
        parametros[j] = f"t{numero + 1}"

    return parametros


# Obtenemos la solución desde la matriz reducida
def obtener_solucion(
    matriz_reducida,
    posiciones_pivote,
    numero_variables
):

    analisis = analizar_pivotes(
        posiciones_pivote,
        numero_variables
    )

    # Si aparece una contradicción, no existe solución
    if es_inconsistente(
        matriz_reducida,
        numero_variables
    ):
        return {
            "tipo": "inconsistente",
            "analisis": analisis,
            "expresiones": {},
            "parametros": {}
        }

    variables_libres = analisis["variables_libres"]
    parametros = crear_parametros(variables_libres)
    expresiones = {}

    # Cada pivote corresponde a una variable básica
    for i, j_pivote in posiciones_pivote:

        constante = matriz_reducida[i][numero_variables]
        terminos = {}

        # Pasamos las variables libres al otro lado
        for j in variables_libres:

            coeficiente = matriz_reducida[i][j]

            if coeficiente != 0:
                terminos[j] = -coeficiente

        expresiones[j_pivote] = {
            "constante": constante,
            "parametros": terminos
        }

    tipo = (
        "determinado"
        if not variables_libres
        else "indeterminado"
    )

    return {
        "tipo": tipo,
        "analisis": analisis,
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

    for j, coeficiente in terminos.items():

        parametro = parametros[j]

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