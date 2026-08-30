# Buscamos las columnas que contienen pivotes
def obtener_columnas_pivote(matriz, numero_variables):
    columnas_pivote = []

    for i in range(len(matriz)):
        for j in range(numero_variables):

            if matriz[i][j] != 0:
                columnas_pivote.append(j)
                break

    return columnas_pivote


# Buscamos las variables que no tienen pivote
def obtener_variables_libres(columnas_pivote, numero_variables):
    variables_libres = []

    for j in range(numero_variables):

        if j not in columnas_pivote:
            variables_libres.append(j)

    return variables_libres


# Revisamos si existe una fila del tipo 0 = b
def es_inconsistente(matriz, numero_variables):

    for i in range(len(matriz)):
        coeficientes_cero = True

        for j in range(numero_variables):

            if matriz[i][j] != 0:
                coeficientes_cero = False
                break

        if (
            coeficientes_cero
            and matriz[i][numero_variables] != 0
        ):
            return True

    return False


# Clasificamos el sistema usando la matriz escalonada
def clasificar_sistema(matriz, numero_variables):

    # Revisamos primero si existe una contradicción
    if es_inconsistente(matriz, numero_variables):
        return {
            "tipo": "inconsistente",
            "nombre": "Sistema Inconsistente",
            "descripcion": "Sin Solución",
            "columnas_pivote": [],
            "variables_basicas": [],
            "variables_libres": []
        }

    columnas_pivote = obtener_columnas_pivote(
        matriz,
        numero_variables
    )

    variables_libres = obtener_variables_libres(
        columnas_pivote,
        numero_variables
    )

    # Sin variables libres tenemos solución única
    if not variables_libres:
        return {
            "tipo": "determinado",
            "nombre": "Sistema Consistente Determinado",
            "descripcion": "Presenta Solución Única",
            "columnas_pivote": columnas_pivote,
            "variables_basicas": columnas_pivote.copy(),
            "variables_libres": []
        }

    # Con variables libres tenemos infinitas soluciones
    return {
        "tipo": "indeterminado",
        "nombre": "Sistema Consistente Indeterminado",
        "descripcion": "Presenta Infinitas Soluciones",
        "columnas_pivote": columnas_pivote,
        "variables_basicas": columnas_pivote.copy(),
        "variables_libres": variables_libres
    }