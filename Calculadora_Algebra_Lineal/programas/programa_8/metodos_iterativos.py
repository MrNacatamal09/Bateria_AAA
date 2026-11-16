"""Resuelve sistemas lineales con Jacobi y Gauss-Seidel manuales.

Tema: métodos iterativos, dominancia diagonal, error y residuo infinito.
Autores: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from math import isfinite


def _validar_sistema(matriz, vector):
    """Copia un sistema cuadrado finito y valida sus dimensiones."""
    try:
        orden = len(matriz)
        if orden == 0 or any(len(fila) != orden for fila in matriz):
            raise ValueError("La matriz A debe ser cuadrada y no estar vacía.")
        if len(vector) != orden:
            raise ValueError("El vector b debe tener la misma dimensión que A.")
    except TypeError as error:
        raise ValueError("A y b deben tener dimensiones válidas.") from error
    try:
        matriz_copia = [[float(valor) for valor in fila] for fila in matriz]
        vector_copia = [float(valor) for valor in vector]
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("A y b deben contener números finitos.") from error

    if any(not isfinite(valor) for fila in matriz_copia for valor in fila):
        raise ValueError("La matriz A debe contener números finitos.")
    if any(not isfinite(valor) for valor in vector_copia):
        raise ValueError("El vector b debe contener números finitos.")
    return matriz_copia, vector_copia


def _validar_argumentos_sin_diagonal(matriz, vector, inicial, epsilon, maximo):
    """Valida entradas antes de permitir que la permutación repare ceros."""
    matriz_copia, vector_copia = _validar_sistema(matriz, vector)
    try:
        inicial_copia = [float(valor) for valor in inicial]
        tolerancia = float(epsilon)
    except (TypeError, ValueError, OverflowError) as error:
        raise ValueError("x⁽⁰⁾ y ε deben contener números finitos.") from error

    if len(inicial_copia) != len(matriz_copia):
        raise ValueError("El vector x⁽⁰⁾ debe tener la misma dimensión que A.")
    if any(not isfinite(valor) for valor in inicial_copia):
        raise ValueError("El vector x⁽⁰⁾ debe contener números finitos.")
    if not isfinite(tolerancia) or tolerancia <= 0:
        raise ValueError("La tolerancia ε debe ser un decimal positivo.")
    if isinstance(maximo, bool) or not isinstance(maximo, int) or maximo <= 0:
        raise ValueError("El máximo de iteraciones debe ser un entero positivo.")
    return matriz_copia, vector_copia, inicial_copia, tolerancia


def _validar_argumentos(matriz, vector, inicial, epsilon, maximo):
    """Añade la comprobación de diagonal antes de iterar directamente."""
    matriz_copia, vector_copia, inicial_copia, tolerancia = (
        _validar_argumentos_sin_diagonal(matriz, vector, inicial, epsilon, maximo)
    )
    if any(fila[i] == 0 for i, fila in enumerate(matriz_copia)):
        raise ValueError("La diagonal principal contiene ceros; evalúe reordenar las filas.")
    return matriz_copia, vector_copia, inicial_copia, tolerancia


def _dominante_estricta(matriz):
    """Comprueba |aᵢᵢ| > suma de los otros valores absolutos por fila."""
    return all(
        abs(fila[i]) > sum(abs(valor) for j, valor in enumerate(fila) if j != i)
        for i, fila in enumerate(matriz)
    )


def _permutacion_por_columnas(matriz, estricta):
    """Busca una asignación de filas a posiciones diagonales sin factoriales."""
    orden = len(matriz)
    candidatos = []
    for columna in range(orden):
        opciones = []
        for fila in range(orden):
            diagonal = abs(matriz[fila][columna])
            otros = sum(abs(matriz[fila][j]) for j in range(orden) if j != columna)
            if diagonal != 0 and (not estricta or diagonal > otros):
                opciones.append(fila)
        # Preferir un coeficiente diagonal grande hace el orden reproducible.
        candidatos.append(sorted(opciones, key=lambda fila: (-abs(matriz[fila][columna]), fila)))

    columna_de_fila = [None] * orden

    def asignar(columna, visitadas):
        """Amplía el emparejamiento sin repetir una fila en la diagonal."""
        for fila in candidatos[columna]:
            if fila in visitadas:
                continue
            visitadas.add(fila)
            anterior = columna_de_fila[fila]
            if anterior is None or asignar(anterior, visitadas):
                columna_de_fila[fila] = columna
                return True
        return False

    for columna in range(orden):
        if not asignar(columna, set()):
            return None

    filas_ordenadas = [None] * orden
    for fila, columna in enumerate(columna_de_fila):
        filas_ordenadas[columna] = fila
    return filas_ordenadas


def preparar_sistema(matriz, vector):
    """Evalúa dominancia y permuta A y b juntos cuando aporta un beneficio."""
    original, b_original = _validar_sistema(matriz, vector)
    orden = len(original)
    identidad = list(range(orden))
    ceros = any(original[i][i] == 0 for i in range(orden))
    dominante_original = _dominante_estricta(original)

    permutacion = identidad
    if not dominante_original:
        dominante = _permutacion_por_columnas(original, estricta=True)
        if dominante is not None:
            permutacion = dominante
        elif ceros:
            no_nula = _permutacion_por_columnas(original, estricta=False)
            if no_nula is None:
                mensaje = (
                    "No se encontró un reordenamiento adecuado: todo orden posible "
                    "deja al menos un cero en la diagonal principal."
                )
                return {
                    "A_original": original,
                    "b_original": b_original,
                    "A_usada": original,
                    "b_usado": b_original,
                    "dominancia_original": dominante_original,
                    "dominancia_usada": dominante_original,
                    "reordenamiento": {
                        "aplicado": False,
                        "orden": [i + 1 for i in identidad],
                        "mensaje": mensaje,
                        "ejecutable": False,
                        "diagonal_original_con_ceros": ceros,
                    },
                }
            permutacion = no_nula

    usada = [original[i].copy() for i in permutacion]
    b_usado = [b_original[i] for i in permutacion]
    dominante_usada = _dominante_estricta(usada)
    aplicado = permutacion != identidad
    if aplicado:
        mensaje = (
            "Se encontró un reordenamiento válido de ecuaciones. "
            "Cada elemento de b se movió con su fila de A."
        )
    elif dominante_usada:
        mensaje = "Se conserva el orden original: la diagonal es estrictamente dominante."
    else:
        mensaje = (
            "No se encontró una permutación con dominancia estricta; se conserva "
            "el orden original. Esto no implica automáticamente divergencia."
        )

    return {
        "A_original": original,
        "b_original": b_original,
        "A_usada": usada,
        "b_usado": b_usado,
        "dominancia_original": dominante_original,
        "dominancia_usada": dominante_usada,
        "reordenamiento": {
            "aplicado": aplicado,
            "orden": [i + 1 for i in permutacion],
            "mensaje": mensaje,
            "ejecutable": True,
            "diagonal_original_con_ceros": ceros,
        },
    }


def norma_infinito_diferencia(primero, segundo):
    """Devuelve la mayor diferencia absoluta entre dos vectores."""
    return max(abs(a - b) for a, b in zip(primero, segundo))


def residuo_infinito(matriz, vector, solucion):
    """Calcula ||Ax-b||∞ con las ecuaciones recibidas."""
    return max(
        abs(sum(a * x for a, x in zip(fila, solucion)) - vector[i])
        for i, fila in enumerate(matriz)
    )


def _resultado_inicial(metodo, matriz, vector, inicial):
    """Inicia el historial con x⁽⁰⁾ y su residuo, sin error previo."""
    residuo = residuo_infinito(matriz, vector, inicial)
    if not isfinite(residuo):
        return {
            "metodo": metodo,
            "solucion": None,
            "iteraciones": [],
            "numero_iteraciones": 0,
            "error_final": None,
            "residuo_final": None,
            "convergio": False,
            "estado": "Posible no convergencia: residuo inicial no finito.",
        }
    return {
        "metodo": metodo,
        "solucion": inicial.copy(),
        "iteraciones": [{"numero": 0, "x": inicial.copy(), "error": None, "residuo": residuo}],
        "numero_iteraciones": 0,
        "error_final": None,
        "residuo_final": residuo,
        "convergio": False,
        "estado": "En proceso.",
    }


def _registrar_paso(resultado, matriz, vector, anterior, nuevo, numero, epsilon):
    """Guarda un paso finito y aplica el mismo criterio a ambos métodos."""
    if any(not isfinite(valor) for valor in nuevo):
        resultado["estado"] = "Posible no convergencia: aparecieron valores no finitos."
        return False
    error = norma_infinito_diferencia(nuevo, anterior)
    residuo = residuo_infinito(matriz, vector, nuevo)
    if not isfinite(error) or not isfinite(residuo):
        resultado["estado"] = "Posible no convergencia: error o residuo no finito."
        return False

    resultado["iteraciones"].append({
        "numero": numero,
        "x": nuevo.copy(),
        "error": error,
        "residuo": residuo,
    })
    resultado["solucion"] = nuevo.copy()
    resultado["numero_iteraciones"] = numero
    resultado["error_final"] = error
    resultado["residuo_final"] = residuo
    if error <= epsilon:
        resultado["convergio"] = True
        resultado["estado"] = "Convergencia alcanzada: ||x⁽ᵏ⁾ - x⁽ᵏ⁻¹⁾||∞ ≤ ε."
        return False

    pasos = resultado["iteraciones"]
    if len(pasos) >= 7:
        recientes = [paso["error"] for paso in pasos[-6:]]
        if (all(siguiente >= 2 * previo for previo, siguiente in zip(recientes, recientes[1:]))
                and recientes[-1] > 1_000_000 * max(pasos[1]["error"], epsilon)):
            resultado["estado"] = (
                "Posible no convergencia: el error creció de forma sostenida y muy marcada."
            )
            return False
    return True


def _estado_al_limite(resultado):
    """Describe la parada por límite sin afirmar divergencia no probada."""
    errores = [paso["error"] for paso in resultado["iteraciones"][1:]]
    if (len(errores) >= 4
            and all(siguiente > previo for previo, siguiente in zip(errores[-4:], errores[-3:]))
            and errores[-1] > 10 * errores[0]):
        resultado["estado"] = (
            "Máximo de iteraciones alcanzado; posible no convergencia "
            "porque el error aumentó."
        )
    else:
        resultado["estado"] = "Máximo de iteraciones alcanzado sin lograr la tolerancia."
    return resultado


def jacobi(matriz, vector, inicial, epsilon, maximo):
    """Actualiza cada xᵢ solo con los valores de la iteración anterior."""
    matriz, vector, anterior, epsilon = _validar_argumentos(
        matriz, vector, inicial, epsilon, maximo
    )
    resultado = _resultado_inicial("Jacobi", matriz, vector, anterior)
    if not resultado["iteraciones"]:
        return resultado
    orden = len(matriz)

    for numero in range(1, maximo + 1):
        nuevo = []
        for i in range(orden):
            suma_anterior = sum(
                matriz[i][j] * anterior[j] for j in range(orden) if j != i
            )
            nuevo.append((vector[i] - suma_anterior) / matriz[i][i])

        if not _registrar_paso(resultado, matriz, vector, anterior, nuevo, numero, epsilon):
            return resultado
        anterior = nuevo
    return _estado_al_limite(resultado)


def gauss_seidel(matriz, vector, inicial, epsilon, maximo):
    """Usa xⱼ recién obtenido cuando j<i y el anterior cuando j>i."""
    matriz, vector, anterior, epsilon = _validar_argumentos(
        matriz, vector, inicial, epsilon, maximo
    )
    resultado = _resultado_inicial("Gauss-Seidel", matriz, vector, anterior)
    if not resultado["iteraciones"]:
        return resultado
    orden = len(matriz)

    for numero in range(1, maximo + 1):
        nuevo = anterior.copy()
        for i in range(orden):
            suma_nueva = sum(matriz[i][j] * nuevo[j] for j in range(i))
            suma_anterior = sum(matriz[i][j] * anterior[j] for j in range(i + 1, orden))
            nuevo[i] = (vector[i] - suma_nueva - suma_anterior) / matriz[i][i]

        if not _registrar_paso(resultado, matriz, vector, anterior, nuevo, numero, epsilon):
            return resultado
        anterior = nuevo
    return _estado_al_limite(resultado)


def _resultado_diagonal_invalida(metodo, mensaje):
    """Explica por qué no es seguro iniciar un método iterativo."""
    return {
        "metodo": metodo,
        "solucion": None,
        "iteraciones": [],
        "numero_iteraciones": 0,
        "error_final": None,
        "residuo_final": None,
        "convergio": False,
        "estado": "No se pudo ejecutar por diagonal inválida. " + mensaje,
    }


def resolver_metodos(matriz, vector, inicial, epsilon, maximo):
    """Prepara el sistema y ejecuta ambos métodos con las mismas entradas."""
    matriz, vector, inicial, epsilon = _validar_argumentos_sin_diagonal(
        matriz, vector, inicial, epsilon, maximo
    )
    preparacion = preparar_sistema(matriz, vector)
    if not preparacion["reordenamiento"]["ejecutable"]:
        mensaje = preparacion["reordenamiento"]["mensaje"]
        preparacion["jacobi"] = _resultado_diagonal_invalida("Jacobi", mensaje)
        preparacion["gauss_seidel"] = _resultado_diagonal_invalida("Gauss-Seidel", mensaje)
    else:
        usada = preparacion["A_usada"]
        b_usado = preparacion["b_usado"]
        preparacion["jacobi"] = jacobi(usada, b_usado, inicial, epsilon, maximo)
        preparacion["gauss_seidel"] = gauss_seidel(usada, b_usado, inicial, epsilon, maximo)
    preparacion["x0"] = inicial
    return preparacion
