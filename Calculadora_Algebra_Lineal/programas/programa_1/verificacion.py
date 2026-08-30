from fractions import Fraction


# Obtenemos los valores de una solución única
def obtener_valores_numericos(resultado_solucion, numero_variables):

    if resultado_solucion["tipo"] != "determinado":
        return None

    valores = []

    for j in range(numero_variables):

        expresion = resultado_solucion["expresiones"][j]

        # Una solución única no debe tener parámetros
        if expresion["parametros"]:
            return None

        valores.append(
            expresion["constante"]
        )

    return valores


# Sustituimos la solución en una ecuación
def verificar_ecuacion(fila, valores, numero_variables):

    lado_izquierdo = Fraction(0)

    for j in range(numero_variables):
        lado_izquierdo += fila[j] * valores[j]

    lado_derecho = fila[numero_variables]

    return {
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "correcta": lado_izquierdo == lado_derecho
    }


# Verificamos la solución en el sistema original
def verificar_solucion(
    matriz_original,
    resultado_solucion,
    numero_variables
):

    valores = obtener_valores_numericos(
        resultado_solucion,
        numero_variables
    )

    # La comprobación numérica aplica a solución única
    if valores is None:
        return {
            "aplica": False,
            "correcta": None,
            "valores": [],
            "ecuaciones": []
        }

    ecuaciones = []
    solucion_correcta = True

    # Comprobamos cada ecuación original
    for i in range(len(matriz_original)):

        resultado = verificar_ecuacion(
            matriz_original[i],
            valores,
            numero_variables
        )

        resultado["ecuacion"] = i + 1
        ecuaciones.append(resultado)

        if not resultado["correcta"]:
            solucion_correcta = False

    return {
        "aplica": True,
        "correcta": solucion_correcta,
        "valores": valores,
        "ecuaciones": ecuaciones
    }