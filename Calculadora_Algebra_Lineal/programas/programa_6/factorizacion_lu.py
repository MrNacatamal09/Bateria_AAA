"""
Implementa la factorización LU y la resolución de sistemas Ax = b.
Construye L y U sin intercambios de filas y conserva cada multiplicador.
Tema de clase: factorización LU y sustituciones hacia adelante y atrás.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from programas.programa_3.matrices import (
    multiplicar_matrices,
)

from programas.programa_3.propiedades_matriz import (
    multiplicar_matriz_vector,
)


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


def _requiere_intercambio(matriz_u, fila_pivote, columna):
    """Indica si una entrada inferior obligaría a intercambiar filas."""
    for fila in range(
        fila_pivote + 1,
        len(matriz_u)
    ):
        if matriz_u[fila][columna] != 0:
            return True

    return False


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

    for columna in range(columnas):
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
                    "No se puede obtener A = LU sin intercambio de filas: "
                    f"en la columna {columna + 1} la entrada pivote de "
                    f"F{fila_pivote + 1} es 0 y existe una entrada no nula "
                    "debajo. Se requiere una permutación; corresponde PA = LU."
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

    producto_lu = multiplicar_matrices(
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
        "num_pivotes": len(posiciones_pivote),
        "producto_lu": producto_lu,
        "cumple_lu": cumple_lu,
        "filas": filas,
        "columnas": columnas,
    }


def sustitucion_hacia_adelante(matriz_l, vector_b):
    """Resuelve Ly = b y guarda el despeje de cada componente yᵢ."""
    orden = len(
        matriz_l
    )

    if len(vector_b) != orden:
        raise ValueError(
            "El vector b no es compatible con la matriz L."
        )

    vector_y = [
        Fraction(0)
        for _ in range(orden)
    ]

    pasos = []

    for i in range(orden):
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

        if diagonal == 0:
            raise ValueError(
                "No se puede realizar sustitución hacia adelante: "
                f"l{i + 1}{i + 1} = 0."
            )

        numerador = (
            vector_b[i]
            - suma
        )

        vector_y[i] = (
            numerador
            / diagonal
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

    return {
        "vector_y": vector_y,
        "pasos": pasos,
    }


def sustitucion_hacia_atras(matriz_u, vector_y):
    """Resuelve Ux = y y guarda el despeje de cada componente xᵢ."""
    orden = len(
        matriz_u
    )

    if len(vector_y) != orden:
        raise ValueError(
            "El vector y no es compatible con la matriz U."
        )

    if len(matriz_u[0]) != orden:
        raise ValueError(
            "Para resolver Ux = y, la matriz U debe ser cuadrada."
        )

    vector_x = [
        Fraction(0)
        for _ in range(orden)
    ]

    pasos = []

    for i in range(
        orden - 1,
        -1,
        -1
    ):
        diagonal = matriz_u[i][i]

        if diagonal == 0:
            raise ValueError(
                "El sistema no tiene solución única: "
                f"u{i + 1}{i + 1} = 0."
            )

        suma = Fraction(0)
        terminos = []

        for j in range(
            i + 1,
            orden
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

        numerador = (
            vector_y[i]
            - suma
        )

        vector_x[i] = (
            numerador
            / diagonal
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

    return {
        "vector_x": vector_x,
        "pasos": pasos,
    }


def resolver_sistema_lu(matriz_a, vector_b):
    """Factoriza A, resuelve Ly=b y Ux=y, y comprueba LU=A y Ax=b."""
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

    if factorizacion["num_pivotes"] != orden:
        raise ValueError(
            "El sistema no tiene solución única mediante esta factorización: "
            "A no posee una posición pivote en cada fila y columna."
        )

    adelante = sustitucion_hacia_adelante(
        factorizacion["matriz_l"],
        vector_b
    )

    atras = sustitucion_hacia_atras(
        factorizacion["matriz_u"],
        adelante["vector_y"]
    )

    vector_x = atras[
        "vector_x"
    ]

    producto_ax = multiplicar_matriz_vector(
        matriz_a,
        vector_x
    )

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
        "vector_y": adelante["vector_y"],
        "vector_x": vector_x,
        "producto_ax": producto_ax,
        "cumple_ax_b": cumple_ax_b,
        "cumple_lu": factorizacion["cumple_lu"],
    }
