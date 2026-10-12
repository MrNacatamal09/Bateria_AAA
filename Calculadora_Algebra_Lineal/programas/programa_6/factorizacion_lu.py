"""
Implementa la factorización LU y la resolución de sistemas Ax = b.
Construye L y U sin intercambios y reutiliza Gauss-Jordan para Ly=b y Ux=y.
Tema de clase: factorización LU, reducción y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from modulos.modulo_matrices import producto_matricial
from modulos.modulo_sistemas import reducir_por_gauss_jordan


def _copiar_matriz(matriz):
    """Devuelve una copia independiente de una matriz."""
    return [
        fila.copy()
        for fila in matriz
    ]


def _crear_identidad(orden):
    """Construye una matriz identidad de orden n."""
    identidad = []

    for i in range(orden):
        fila = []

        for j in range(orden):
            fila.append(
                Fraction(1)
                if i == j
                else Fraction(0)
            )

        identidad.append(
            fila
        )

    return identidad


def _validar_matriz(matriz):
    """Valida que la entrada sea una matriz rectangular no vacía."""
    if not matriz or not matriz[0]:
        raise ValueError(
            "La matriz A no puede estar vacía."
        )

    columnas = len(
        matriz[0]
    )

    for fila in matriz:
        if len(fila) != columnas:
            raise ValueError(
                "Todas las filas de A deben tener la misma cantidad de columnas."
            )


def _validar_sistema_cuadrado(matriz_a, vector_b):
    """Valida las dimensiones necesarias para resolver Ax = b."""
    _validar_matriz(
        matriz_a
    )

    filas = len(
        matriz_a
    )

    columnas = len(
        matriz_a[0]
    )

    if filas != columnas:
        raise ValueError(
            "Para resolver Ax = b mediante LU, la matriz A debe ser cuadrada."
        )

    if len(vector_b) != filas:
        raise ValueError(
            "El vector b debe tener la misma cantidad de elementos que filas de A."
        )


def _validar_matriz_cuadrada_vector(
    matriz,
    vector,
    nombre_matriz,
    nombre_vector,
):
    """Valida una matriz cuadrada y un vector compatible para una reducción."""
    _validar_matriz(
        matriz
    )

    orden = len(
        matriz
    )

    if len(matriz[0]) != orden:
        raise ValueError(
            f"La matriz {nombre_matriz} debe ser cuadrada."
        )

    if len(vector) != orden:
        raise ValueError(
            f"El vector {nombre_vector} no es compatible con "
            f"la matriz {nombre_matriz}."
        )


def _texto_operacion_reemplazo(
    fila_destino,
    fila_pivote,
    multiplicador,
):
    """Construye la operación elemental usada durante la eliminación."""
    if multiplicador < 0:
        return (
            f"F{fila_destino + 1} -> F{fila_destino + 1} "
            f"+ ({-multiplicador})F{fila_pivote + 1}"
        )

    return (
        f"F{fila_destino + 1} -> F{fila_destino + 1} "
        f"- ({multiplicador})F{fila_pivote + 1}"
    )


def _requiere_intercambio(
    matriz_u,
    fila_pivote,
    columna,
):
    """Indica si una entrada inferior obligaría a intercambiar filas."""
    for fila in range(
        fila_pivote + 1,
        len(matriz_u)
    ):
        if matriz_u[fila][columna] != 0:
            return True

    return False


def _crear_matriz_aumentada(
    matriz,
    vector,
):
    """Construye [A|b] sin modificar la matriz ni el vector originales."""
    return [
        matriz[i].copy() + [vector[i]]
        for i in range(
            len(matriz)
        )
    ]


def _extraer_vector_reducido(
    resultado,
    orden,
    nombre_vector,
):
    """Extrae la última columna de [I|v] y valida una solución única."""
    matriz_reducida = resultado[
        "matriz_reducida"
    ]

    for i in range(orden):
        for j in range(orden):
            esperado = (
                Fraction(1)
                if i == j
                else Fraction(0)
            )

            if matriz_reducida[i][j] != esperado:
                raise ValueError(
                    "No se pudo obtener una solución única "
                    f"para {nombre_vector}."
                )

    return [
        matriz_reducida[i][-1]
        for i in range(orden)
    ]


def _crear_pasos_adelante_compatibilidad(
    matriz_l,
    vector_b,
    vector_y,
):
    """Conserva temporalmente la estructura usada por el formateador actual."""
    pasos = []

    for i in range(
        len(matriz_l)
    ):
        suma = Fraction(0)
        terminos = []

        for j in range(i):
            producto = (
                matriz_l[i][j]
                * vector_y[j]
            )

            suma += producto

            terminos.append(
                {
                    "coeficiente": matriz_l[i][j],
                    "variable": vector_y[j],
                    "producto": producto,
                    "indice": j,
                }
            )

        diagonal = matriz_l[i][i]

        numerador = (
            vector_b[i]
            - suma
        )

        pasos.append(
            {
                "indice": i,
                "terminos": terminos,
                "suma": suma,
                "b": vector_b[i],
                "diagonal": diagonal,
                "numerador": numerador,
                "resultado": vector_y[i],
            }
        )

    return pasos


def _crear_pasos_atras_compatibilidad(
    matriz_u,
    vector_y,
    vector_x,
):
    """Conserva temporalmente la estructura usada por el formateador actual."""
    pasos = []

    for i in range(
        len(matriz_u) - 1,
        -1,
        -1
    ):
        suma = Fraction(0)
        terminos = []

        for j in range(
            i + 1,
            len(matriz_u)
        ):
            producto = (
                matriz_u[i][j]
                * vector_x[j]
            )

            suma += producto

            terminos.append(
                {
                    "coeficiente": matriz_u[i][j],
                    "variable": vector_x[j],
                    "producto": producto,
                    "indice": j,
                }
            )

        diagonal = matriz_u[i][i]

        numerador = (
            vector_y[i]
            - suma
        )

        pasos.append(
            {
                "indice": i,
                "terminos": terminos,
                "suma": suma,
                "y": vector_y[i],
                "diagonal": diagonal,
                "numerador": numerador,
                "resultado": vector_x[i],
            }
        )

    return pasos


def factorizar_lu(matriz_a):
    """Construye A = LU sin intercambios y registra cada paso de reducción."""
    _validar_matriz(
        matriz_a
    )

    filas = len(
        matriz_a
    )

    columnas = len(
        matriz_a[0]
    )

    matriz_u = _copiar_matriz(
        matriz_a
    )

    matriz_l = _crear_identidad(
        filas
    )

    pasos = []
    multiplicadores = []
    posiciones_pivote = []

    fila_pivote = 0

    for columna in range(
        columnas
    ):
        if fila_pivote >= filas:
            break

        valor_pivote = matriz_u[
            fila_pivote
        ][
            columna
        ]

        if valor_pivote == 0:
            if _requiere_intercambio(
                matriz_u,
                fila_pivote,
                columna
            ):
                raise ValueError(
                    "La matriz no admite Factorización LU sin permutación "
                    "(requiere pivoteo parcial PA = LU)."
                )

            continue

        posiciones_pivote.append(
            (
                fila_pivote,
                columna
            )
        )

        for fila in range(
            fila_pivote + 1,
            filas
        ):
            elemento_eliminado = matriz_u[
                fila
            ][
                columna
            ]

            if elemento_eliminado == 0:
                matriz_l[
                    fila
                ][
                    fila_pivote
                ] = Fraction(0)

                continue

            multiplicador = (
                elemento_eliminado
                / valor_pivote
            )

            # L guarda el multiplicador antes de modificar la fila de U.
            matriz_l[
                fila
            ][
                fila_pivote
            ] = multiplicador

            matriz_antes = _copiar_matriz(
                matriz_u
            )

            for j in range(
                columna,
                columnas
            ):
                matriz_u[fila][j] -= (
                    multiplicador
                    * matriz_u[fila_pivote][j]
                )

            matriz_despues = _copiar_matriz(
                matriz_u
            )

            multiplicadores.append(
                {
                    "fila": fila,
                    "fila_pivote": fila_pivote,
                    "columna_pivote": columna,
                    "elemento_eliminado": elemento_eliminado,
                    "pivote": valor_pivote,
                    "multiplicador": multiplicador,
                }
            )

            pasos.append(
                {
                    "fila_pivote": fila_pivote,
                    "columna_pivote": columna,
                    "fila": fila,
                    "operacion": _texto_operacion_reemplazo(
                        fila,
                        fila_pivote,
                        multiplicador
                    ),
                    "multiplicador": multiplicador,
                    "matriz_antes": matriz_antes,
                    "matriz_despues": matriz_despues,
                }
            )

        fila_pivote += 1

    producto_lu = producto_matricial(
        matriz_l,
        matriz_u
    )

    cumple_lu = (
        producto_lu
        == matriz_a
    )

    return {
        "matriz_a": matriz_a,
        "matriz_l": matriz_l,
        "matriz_u": matriz_u,
        "multiplicadores": multiplicadores,
        "pasos": pasos,
        "posiciones_pivote": posiciones_pivote,
        "num_pivotes": len(
            posiciones_pivote
        ),
        "producto_lu": producto_lu,
        "cumple_lu": cumple_lu,
        "filas": filas,
        "columnas": columnas,
    }


def sustitucion_hacia_adelante(
    matriz_l,
    vector_b,
):
    """Resuelve Ly=b reduciendo la matriz aumentada [L|b] con Gauss-Jordan."""
    _validar_matriz_cuadrada_vector(
        matriz_l,
        vector_b,
        "L",
        "b",
    )

    matriz_aumentada = _crear_matriz_aumentada(
        matriz_l,
        vector_b
    )

    reduccion = reducir_por_gauss_jordan(
        matriz_aumentada
    )

    vector_y = _extraer_vector_reducido(
        reduccion,
        len(matriz_l),
        "y",
    )

    return {
        "vector_y": vector_y,
        "matriz_aumentada": matriz_aumentada,
        "matriz_reducida": reduccion[
            "matriz_reducida"
        ],
        "historial": reduccion[
            "historial"
        ],
        "posiciones_pivote": reduccion[
            "posiciones_pivote"
        ],
        "pasos": _crear_pasos_adelante_compatibilidad(
            matriz_l,
            vector_b,
            vector_y,
        ),
    }


def sustitucion_hacia_atras(
    matriz_u,
    vector_y,
):
    """Resuelve Ux=y reduciendo la matriz aumentada [U|y] con Gauss-Jordan."""
    _validar_matriz_cuadrada_vector(
        matriz_u,
        vector_y,
        "U",
        "y",
    )

    matriz_aumentada = _crear_matriz_aumentada(
        matriz_u,
        vector_y
    )

    reduccion = reducir_por_gauss_jordan(
        matriz_aumentada
    )

    vector_x = _extraer_vector_reducido(
        reduccion,
        len(matriz_u),
        "x",
    )

    return {
        "vector_x": vector_x,
        "matriz_aumentada": matriz_aumentada,
        "matriz_reducida": reduccion[
            "matriz_reducida"
        ],
        "historial": reduccion[
            "historial"
        ],
        "posiciones_pivote": reduccion[
            "posiciones_pivote"
        ],
        "pasos": _crear_pasos_atras_compatibilidad(
            matriz_u,
            vector_y,
            vector_x,
        ),
    }


def resolver_sistema_lu(
    matriz_a,
    vector_b,
):
    """Factoriza A, resuelve [L|b] y [U|y], y verifica LU=A y Ax=b."""
    _validar_sistema_cuadrado(
        matriz_a,
        vector_b
    )

    factorizacion = factorizar_lu(
        matriz_a
    )

    orden = len(
        matriz_a
    )

    if factorizacion[
        "num_pivotes"
    ] != orden:
        raise ValueError(
            "El sistema no tiene solución única mediante esta factorización: "
            "A no posee una posición pivote en cada fila y columna."
        )

    adelante = sustitucion_hacia_adelante(
        factorizacion[
            "matriz_l"
        ],
        vector_b
    )

    atras = sustitucion_hacia_atras(
        factorizacion[
            "matriz_u"
        ],
        adelante[
            "vector_y"
        ]
    )

    vector_x = atras[
        "vector_x"
    ]

    vector_x_columna = [
        [valor]
        for valor in vector_x
    ]

    producto_ax_matriz = producto_matricial(
        matriz_a,
        vector_x_columna
    )

    producto_ax = [
        fila[0]
        for fila in producto_ax_matriz
    ]

    cumple_ax_b = (
        producto_ax
        == vector_b
    )

    return {
        "matriz_a": matriz_a,
        "vector_b": vector_b,
        "factorizacion": factorizacion,
        "sustitucion_adelante": adelante,
        "sustitucion_atras": atras,
        "vector_y": adelante[
            "vector_y"
        ],
        "vector_x": vector_x,
        "producto_ax": producto_ax,
        "cumple_ax_b": cumple_ax_b,
        "cumple_lu": factorizacion[
            "cumple_lu"
        ],
    }