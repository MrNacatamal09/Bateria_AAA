"""
Implementa los métodos de cálculo de determinantes usados en el Programa 5.
Incluye cofactores, regla de Sarrus y reducción a forma triangular.
Tema de clase: determinantes, menores, cofactores y operaciones de fila.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from copy import deepcopy
from fractions import Fraction


def validar_matriz(matriz):
    """Valida que la estructura recibida represente una matriz no vacía."""
    if not isinstance(matriz, list) or not matriz:
        raise ValueError(
            "La matriz no puede estar vacía."
        )

    if not isinstance(matriz[0], list) or not matriz[0]:
        raise ValueError(
            "La matriz debe contener filas y columnas."
        )

    columnas = len(
        matriz[0]
    )

    for fila in matriz:
        if not isinstance(fila, list):
            raise ValueError(
                "Cada fila de la matriz debe ser una lista."
            )

        if len(fila) != columnas:
            raise ValueError(
                "Todas las filas deben tener "
                "la misma cantidad de columnas."
            )


def validar_matriz_cuadrada(matriz):
    """Valida que una matriz tenga la misma cantidad de filas y columnas."""
    validar_matriz(
        matriz
    )

    filas = len(
        matriz
    )

    columnas = len(
        matriz[0]
    )

    if filas != columnas:
        raise ValueError(
            "El determinante solamente está definido "
            "para matrices cuadradas."
        )


def obtener_menor(matriz, fila_eliminar, columna_eliminar):
    """Devuelve la matriz obtenida al eliminar una fila y una columna."""
    validar_matriz_cuadrada(
        matriz
    )

    menor = []

    for fila, valores in enumerate(matriz):
        if fila == fila_eliminar:
            continue

        nueva_fila = []

        for columna, valor in enumerate(valores):
            if columna == columna_eliminar:
                continue

            nueva_fila.append(
                valor
            )

        menor.append(
            nueva_fila
        )

    return menor


def obtener_signo_cofactor(fila, columna):
    """Devuelve 1 o -1 según el signo (-1)^(i+j) del cofactor."""
    if (
        fila + columna
    ) % 2 == 0:
        return Fraction(1)

    return Fraction(-1)


def contar_ceros_fila(matriz, fila):
    """Cuenta los elementos iguales a cero de una fila."""
    return sum(
        1
        for valor in matriz[fila]
        if valor == 0
    )


def contar_ceros_columna(matriz, columna):
    """Cuenta los elementos iguales a cero de una columna."""
    return sum(
        1
        for fila in matriz
        if fila[columna] == 0
    )


def seleccionar_fila_o_columna(matriz):
    """Selecciona la fila o columna con más ceros para reducir el desarrollo."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    mejor_tipo = "fila"
    mejor_indice = 0
    mayor_cantidad_ceros = -1

    for fila in range(orden):
        cantidad = contar_ceros_fila(
            matriz,
            fila
        )

        if cantidad > mayor_cantidad_ceros:
            mayor_cantidad_ceros = cantidad
            mejor_tipo = "fila"
            mejor_indice = fila

    for columna in range(orden):
        cantidad = contar_ceros_columna(
            matriz,
            columna
        )

        if cantidad > mayor_cantidad_ceros:
            mayor_cantidad_ceros = cantidad
            mejor_tipo = "columna"
            mejor_indice = columna

    return mejor_tipo, mejor_indice


def calcular_determinante_2x2(matriz):
    """Calcula el determinante de una matriz 2x2 mediante ad - bc."""
    validar_matriz_cuadrada(
        matriz
    )

    if len(matriz) != 2:
        raise ValueError(
            "Este método requiere una matriz de orden 2."
        )

    return (
        matriz[0][0] * matriz[1][1]
        - matriz[0][1] * matriz[1][0]
    )


def calcular_determinante(matriz):
    """Calcula el determinante de una matriz cuadrada mediante cofactores."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    if orden == 1:
        return matriz[0][0]

    if orden == 2:
        return calcular_determinante_2x2(
            matriz
        )

    tipo, indice = seleccionar_fila_o_columna(
        matriz
    )

    determinante = Fraction(0)

    if tipo == "fila":
        for columna in range(orden):
            elemento = matriz[indice][columna]

            # Los términos con elemento cero no aportan al desarrollo.
            if elemento == 0:
                continue

            determinante += (
                elemento
                * calcular_cofactor(
                    matriz,
                    indice,
                    columna
                )
            )

    else:
        for fila in range(orden):
            elemento = matriz[fila][indice]

            # Los términos con elemento cero no aportan al desarrollo.
            if elemento == 0:
                continue

            determinante += (
                elemento
                * calcular_cofactor(
                    matriz,
                    fila,
                    indice
                )
            )

    return determinante


def calcular_determinante_sarrus(matriz):
    """Calcula el determinante de una matriz 3x3 mediante la regla de Sarrus."""
    validar_matriz_cuadrada(
        matriz
    )

    if len(matriz) != 3:
        raise ValueError(
            "La regla de Sarrus solamente se aplica "
            "a matrices de orden 3."
        )

    a, b, c = matriz[0]
    d, e, f = matriz[1]
    g, h, i = matriz[2]

    suma_positiva = (
        a * e * i
        + b * f * g
        + c * d * h
    )

    suma_negativa = (
        c * e * g
        + b * d * i
        + a * f * h
    )

    return (
        suma_positiva
        - suma_negativa
    )


def buscar_fila_pivote(
    matriz,
    fila_inicio,
    columna
):
    """Busca desde una fila inicial una entrada no nula para usarla como pivote."""
    for fila in range(
        fila_inicio,
        len(matriz)
    ):
        if matriz[fila][columna] != 0:
            return fila

    return None


def _crear_texto_reemplazo(
    fila_destino,
    fila_pivote,
    factor
):
    """Representa una operación de eliminación usando un signo natural."""
    if factor < 0:
        return (
            f"F{fila_destino + 1} -> "
            f"F{fila_destino + 1} + "
            f"({-factor})F{fila_pivote + 1}"
        )

    return (
        f"F{fila_destino + 1} -> "
        f"F{fila_destino + 1} - "
        f"({factor})F{fila_pivote + 1}"
    )


def _guardar_paso(
    historial,
    operacion,
    matriz
):
    """Agrega al historial una operación y una copia del estado de la matriz."""
    historial.append(
        {
            "operacion": operacion,
            "matriz": deepcopy(
                matriz
            )
        }
    )


def triangularizar_para_determinante(matriz_original):
    """Reduce A a forma triangular y conserva los datos usados para det(A)."""
    validar_matriz_cuadrada(
        matriz_original
    )

    matriz = deepcopy(
        matriz_original
    )

    orden = len(
        matriz
    )

    historial = []

    _guardar_paso(
        historial,
        "Matriz inicial",
        matriz
    )

    intercambios = 0
    factores_eliminacion = []
    fila_pivote_actual = 0

    for columna in range(orden):
        if fila_pivote_actual >= orden:
            break

        fila_encontrada = buscar_fila_pivote(
            matriz,
            fila_pivote_actual,
            columna
        )

        # Una columna sin pivote indica pérdida de rango, pero pueden existir
        # pivotes en columnas posteriores y deben contarse correctamente.
        if fila_encontrada is None:
            continue

        if fila_encontrada != fila_pivote_actual:
            matriz[
                fila_pivote_actual
            ], matriz[
                fila_encontrada
            ] = (
                matriz[fila_encontrada],
                matriz[fila_pivote_actual]
            )

            intercambios += 1

            _guardar_paso(
                historial,
                (
                    f"F{fila_pivote_actual + 1} "
                    f"<-> F{fila_encontrada + 1}"
                ),
                matriz
            )

        pivote = matriz[
            fila_pivote_actual
        ][
            columna
        ]

        for fila in range(
            fila_pivote_actual + 1,
            orden
        ):
            valor = matriz[
                fila
            ][
                columna
            ]

            if valor == 0:
                continue

            factor = (
                valor
                / pivote
            )

            for j in range(
                columna,
                orden
            ):
                matriz[fila][j] -= (
                    factor
                    * matriz[
                        fila_pivote_actual
                    ][j]
                )

            factores_eliminacion.append(
                {
                    "fila_destino":
                        fila,

                    "fila_pivote":
                        fila_pivote_actual,

                    "factor":
                        factor
                }
            )

            _guardar_paso(
                historial,
                _crear_texto_reemplazo(
                    fila,
                    fila_pivote_actual,
                    factor
                ),
                matriz
            )

        fila_pivote_actual += 1

    num_pivotes = fila_pivote_actual

    producto_diagonal = Fraction(1)

    for indice in range(orden):
        producto_diagonal *= matriz[
            indice
        ][
            indice
        ]

    signo = (
        Fraction(-1)
        if intercambios % 2 != 0
        else Fraction(1)
    )

    determinante = (
        signo
        * producto_diagonal
    )

    return {
        "matriz_original":
            matriz_original,

        "matriz_triangular":
            matriz,

        "historial":
            historial,

        "intercambios":
            intercambios,

        "factores_eliminacion":
            factores_eliminacion,

        "num_pivotes":
            num_pivotes,

        "producto_diagonal":
            producto_diagonal,

        "determinante":
            determinante
    }


def calcular_determinante_triangular(matriz):
    """Calcula det(A) mediante reducción triangular y producto de la diagonal."""
    resultado = triangularizar_para_determinante(
        matriz
    )

    return resultado[
        "determinante"
    ]


def comparar_metodos_determinante(matriz):
    """Compara cofactores, reducción triangular y Sarrus cuando corresponde."""
    validar_matriz_cuadrada(
        matriz
    )

    cofactores = calcular_determinante(
        matriz
    )

    triangular = calcular_determinante_triangular(
        matriz
    )

    sarrus = None

    if len(matriz) == 3:
        sarrus = calcular_determinante_sarrus(
            matriz
        )

    coinciden = (
        cofactores
        == triangular
    )

    if sarrus is not None:
        coinciden = (
            coinciden
            and cofactores == sarrus
        )

    return {
        "cofactores":
            cofactores,

        "sarrus":
            sarrus,

        "triangular":
            triangular,

        "coinciden":
            coinciden
    }


def calcular_cofactor(
    matriz,
    fila,
    columna
):
    """Calcula el cofactor Cij asociado con una entrada de una matriz cuadrada."""
    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    if fila < 0 or fila >= orden:
        raise ValueError(
            "La fila del cofactor no existe."
        )

    if columna < 0 or columna >= orden:
        raise ValueError(
            "La columna del cofactor no existe."
        )

    # El menor de la única entrada de una matriz 1x1 tiene determinante 1.
    if orden == 1:
        return Fraction(1)

    menor = obtener_menor(
        matriz,
        fila,
        columna
    )

    return (
        obtener_signo_cofactor(
            fila,
            columna
        )
        * calcular_determinante(
            menor
        )
    )


def es_matriz_invertible(matriz):
    """Devuelve True cuando una matriz cuadrada tiene determinante distinto de cero."""
    validar_matriz_cuadrada(
        matriz
    )

    return (
        calcular_determinante(
            matriz
        )
        != 0
    )