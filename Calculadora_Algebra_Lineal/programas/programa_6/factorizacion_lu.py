"""
Implementa la factorización LU y la resolución de sistemas Ax = b.
Construye PA = LU con pivoteo parcial y reutiliza Gauss-Jordan.
Tema de clase: factorización LU, reducción y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from modulos.modulo_matrices import (
    crear_identidad,
    matrices_son_iguales,
    producto_matricial,
    transponer,
)
from modulos.modulo_sistemas import reducir_por_gauss_jordan
from programas.programa_3.matrices import validar_matriz


def _copiar_matriz(matriz):
    """Devuelve una copia independiente de una matriz."""
    return [
        fila.copy()
        for fila in matriz
    ]


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


def _validar_permutacion(matriz_p, orden):
    """Exige una matriz P cuadrada con un único 1 por fila y columna."""
    try:
        validar_matriz(matriz_p)
    except ValueError as error:
        raise ValueError(f"La matriz P no es válida: {error}") from None

    if len(matriz_p) != orden or len(matriz_p[0]) != orden:
        raise ValueError(
            f"La matriz P debe ser cuadrada de orden {orden}."
        )

    if any(
        any(valor not in (0, 1) for valor in fila) or sum(fila) != 1
        for fila in matriz_p
    ) or any(
        sum(matriz_p[fila][columna] for fila in range(orden)) != 1
        for columna in range(orden)
    ):
        raise ValueError(
            "La matriz P debe contener solo 0 y 1, con un único 1 "
            "en cada fila y cada columna."
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
    """Construye PA = LU con pivoteo parcial y registra la reducción."""
    _validar_matriz(
        matriz_a
    )

    filas = len(
        matriz_a
    )

    columnas = len(
        matriz_a[0]
    )

    matriz_a_exacta = [
        [Fraction(valor) for valor in fila]
        for fila in matriz_a
    ]

    matriz_u = _copiar_matriz(
        matriz_a_exacta
    )

    matriz_l = crear_identidad(
        filas
    )

    matriz_p = crear_identidad(
        filas
    )

    pasos = []
    historial_operaciones = []
    multiplicadores = []
    posiciones_pivote = []
    permutaciones = []

    fila_pivote = 0

    for columna in range(
        columnas
    ):
        if fila_pivote >= filas:
            break

        fila_elegida = max(
            range(fila_pivote, filas),
            key=lambda fila: abs(matriz_u[fila][columna]),
        )

        if matriz_u[fila_elegida][columna] == 0:
            continue

        if fila_elegida != fila_pivote:
            matriz_antes = _copiar_matriz(matriz_u)
            matriz_u[fila_pivote], matriz_u[fila_elegida] = (
                matriz_u[fila_elegida], matriz_u[fila_pivote]
            )
            matriz_p[fila_pivote], matriz_p[fila_elegida] = (
                matriz_p[fila_elegida], matriz_p[fila_pivote]
            )

            # Las columnas anteriores de L ya guardan multiplicadores.
            # Sus filas deben seguir la misma permutación que U y P.
            for columna_anterior in range(fila_pivote):
                matriz_l[fila_pivote][columna_anterior], matriz_l[fila_elegida][columna_anterior] = (
                    matriz_l[fila_elegida][columna_anterior],
                    matriz_l[fila_pivote][columna_anterior],
                )

            permutaciones.append((fila_pivote, fila_elegida))
            historial_operaciones.append(
                {
                    "tipo": "permutacion",
                    "fila_pivote": fila_pivote,
                    "fila_intercambiada": fila_elegida,
                    "columna_pivote": columna,
                    "operacion": f"F{fila_pivote + 1} ↔ F{fila_elegida + 1}",
                    "matriz_antes": matriz_antes,
                    "matriz_despues": _copiar_matriz(matriz_u),
                }
            )

        valor_pivote = matriz_u[fila_pivote][columna]

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

            paso = {
                    "tipo": "eliminacion",
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
            pasos.append(paso)
            historial_operaciones.append(paso)

        fila_pivote += 1

    producto_lu = producto_matricial(
        matriz_l,
        matriz_u
    )

    producto_pa = producto_matricial(
        matriz_p,
        matriz_a_exacta,
    )

    cumple_lu = matrices_son_iguales(
        producto_lu,
        producto_pa,
    )

    return {
        "matriz_a": matriz_a_exacta,
        "matriz_p": matriz_p,
        "matriz_l": matriz_l,
        "matriz_u": matriz_u,
        "permutaciones": permutaciones,
        "hubo_permutaciones": bool(permutaciones),
        "multiplicadores": multiplicadores,
        "pasos": pasos,
        "historial_operaciones": historial_operaciones,
        "posiciones_pivote": posiciones_pivote,
        "num_pivotes": len(
            posiciones_pivote
        ),
        "producto_lu": producto_lu,
        "producto_pa": producto_pa,
        "cumple_lu": cumple_lu,
        "filas": filas,
        "columnas": columnas,
    }


def reconstruir_a_desde_lu(matriz_l, matriz_u, matriz_p=None):
    """Reconstruye A=LU o A=PᵀLU si se proporciona una P válida."""
    for nombre, matriz in (("L", matriz_l), ("U", matriz_u)):
        try:
            validar_matriz(matriz)
        except ValueError as error:
            raise ValueError(
                f"La matriz {nombre} no es válida: {error}"
            ) from None

    if len(matriz_l[0]) != len(matriz_u):
        raise ValueError(
            "No se puede calcular L·U: el número de columnas de L "
            "debe ser igual al número de filas de U."
        )

    matriz_l_exacta = [
        [Fraction(valor) for valor in fila]
        for fila in matriz_l
    ]
    matriz_u_exacta = [
        [Fraction(valor) for valor in fila]
        for fila in matriz_u
    ]
    producto_lu = producto_matricial(matriz_l_exacta, matriz_u_exacta)

    if matriz_p is None:
        matriz_p_exacta = None
        matriz_p_transpuesta = None
        matriz_a = _copiar_matriz(producto_lu)
        producto_pa = _copiar_matriz(matriz_a)
        hubo_permutaciones = False
    else:
        _validar_permutacion(matriz_p, len(matriz_l_exacta))
        matriz_p_exacta = [
            [Fraction(valor) for valor in fila]
            for fila in matriz_p
        ]
        matriz_p_transpuesta = transponer(matriz_p_exacta)
        matriz_a = producto_matricial(matriz_p_transpuesta, producto_lu)
        producto_pa = producto_matricial(matriz_p_exacta, matriz_a)
        hubo_permutaciones = not matrices_son_iguales(
            matriz_p_exacta,
            crear_identidad(len(matriz_l_exacta)),
        )

    return {
        "matriz_l": matriz_l_exacta,
        "matriz_u": matriz_u_exacta,
        "matriz_p": matriz_p_exacta,
        "matriz_p_transpuesta": matriz_p_transpuesta,
        "producto_lu": producto_lu,
        "matriz_a": matriz_a,
        "producto_pa": producto_pa,
        "cumple_lu": matrices_son_iguales(producto_pa, producto_lu),
        "hubo_permutaciones": hubo_permutaciones,
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
    """Factoriza PA, resuelve Ly=Pb y Ux=y, y verifica Ax=b."""
    _validar_sistema_cuadrado(
        matriz_a,
        vector_b
    )

    factorizacion = factorizar_lu(
        matriz_a
    )

    matriz_a_exacta = factorizacion["matriz_a"]
    vector_b_exacto = [Fraction(valor) for valor in vector_b]

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

    producto_pb_matriz = producto_matricial(
        factorizacion["matriz_p"],
        [[valor] for valor in vector_b_exacto],
    )
    vector_pb = [fila[0] for fila in producto_pb_matriz]

    adelante = sustitucion_hacia_adelante(
        factorizacion[
            "matriz_l"
        ],
        vector_pb
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
        matriz_a_exacta,
        vector_x_columna
    )

    producto_ax = [
        fila[0]
        for fila in producto_ax_matriz
    ]

    cumple_ax_b = matrices_son_iguales(
        producto_ax_matriz,
        [[valor] for valor in vector_b_exacto],
    )

    return {
        "matriz_a": matriz_a_exacta,
        "vector_b": vector_b_exacto,
        "vector_pb": vector_pb,
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
