from fractions import Fraction


# ==========================================================
# VALIDACIÓN DE MATRICES
# ==========================================================

# Revisamos que una matriz tenga filas y columnas válidas.
def validar_matriz(matriz):

    if not matriz:
        raise ValueError(
            "La matriz no puede estar vacía."
        )

    columnas = len(
        matriz[0]
    )

    if columnas == 0:
        raise ValueError(
            "La matriz debe tener al menos una columna."
        )

    for i in range(
        len(matriz)
    ):

        if len(matriz[i]) != columnas:
            raise ValueError(
                "Todas las filas deben tener "
                "la misma cantidad de columnas."
            )


# ==========================================================
# DIMENSIONES
# ==========================================================

def obtener_dimensiones(matriz):

    validar_matriz(
        matriz
    )

    filas = len(
        matriz
    )

    columnas = len(
        matriz[0]
    )

    return filas, columnas


# ==========================================================
# VALIDAR MISMAS DIMENSIONES
# ==========================================================

# Revisamos que dos matrices tengan las mismas dimensiones.
def validar_mismas_dimensiones(
    matriz_1,
    matriz_2
):

    validar_matriz(
        matriz_1
    )

    validar_matriz(
        matriz_2
    )

    mismas_filas = (
        len(matriz_1)
        == len(matriz_2)
    )

    mismas_columnas = (
        len(matriz_1[0])
        == len(matriz_2[0])
    )

    if not (
        mismas_filas
        and mismas_columnas
    ):

        raise ValueError(
            "Las matrices deben tener "
            "las mismas dimensiones."
        )


# ==========================================================
# SUMA DE MATRICES
# ==========================================================

# Sumamos dos matrices elemento a elemento.
def sumar_matrices(
    matriz_1,
    matriz_2
):

    validar_mismas_dimensiones(
        matriz_1,
        matriz_2
    )

    resultado = []

    for i in range(
        len(matriz_1)
    ):

        fila = []

        for j in range(
            len(matriz_1[i])
        ):

            fila.append(
                matriz_1[i][j]
                + matriz_2[i][j]
            )

        resultado.append(
            fila
        )

    return resultado


# ==========================================================
# RESTA DE MATRICES
# ==========================================================

# Restamos dos matrices elemento a elemento.
def restar_matrices(
    matriz_1,
    matriz_2
):

    validar_mismas_dimensiones(
        matriz_1,
        matriz_2
    )

    resultado = []

    for i in range(
        len(matriz_1)
    ):

        fila = []

        for j in range(
            len(matriz_1[i])
        ):

            fila.append(
                matriz_1[i][j]
                - matriz_2[i][j]
            )

        resultado.append(
            fila
        )

    return resultado


# ==========================================================
# MULTIPLICACIÓN POR ESCALAR
# ==========================================================

# Multiplicamos una matriz por un escalar.
def multiplicar_matriz_escalar(
    matriz,
    escalar
):

    validar_matriz(
        matriz
    )

    escalar = Fraction(
        escalar
    )

    resultado = []

    for i in range(
        len(matriz)
    ):

        fila = []

        for j in range(
            len(matriz[i])
        ):

            fila.append(
                matriz[i][j]
                * escalar
            )

        resultado.append(
            fila
        )

    return resultado


# ==========================================================
# VALIDAR MULTIPLICACIÓN DE MATRICES
# ==========================================================

# Para que AB exista, el número de columnas de A
# debe ser igual al número de filas de B.
def validar_multiplicacion(
    matriz_1,
    matriz_2
):

    validar_matriz(
        matriz_1
    )

    validar_matriz(
        matriz_2
    )

    columnas_matriz_1 = len(
        matriz_1[0]
    )

    filas_matriz_2 = len(
        matriz_2
    )

    if (
        columnas_matriz_1
        != filas_matriz_2
    ):

        raise ValueError(
            "Las columnas de la primera matriz "
            "deben ser iguales a las filas "
            "de la segunda matriz."
        )


# ==========================================================
# MULTIPLICACIÓN DE MATRICES
# ==========================================================

# Multiplicamos dos matrices utilizando
# la regla fila-columna.
def multiplicar_matrices(
    matriz_1,
    matriz_2
):

    validar_multiplicacion(
        matriz_1,
        matriz_2
    )

    filas_resultado = len(
        matriz_1
    )

    columnas_resultado = len(
        matriz_2[0]
    )

    dimension_comun = len(
        matriz_1[0]
    )

    resultado = []

    # i recorre las filas de la primera matriz.
    for i in range(
        filas_resultado
    ):

        fila = []

        # j recorre las columnas de la segunda matriz.
        for j in range(
            columnas_resultado
        ):

            valor = Fraction(
                0
            )

            # k recorre la dimensión compartida.
            for k in range(
                dimension_comun
            ):

                valor += (
                    matriz_1[i][k]
                    * matriz_2[k][j]
                )

            fila.append(
                valor
            )

        resultado.append(
            fila
        )

    return resultado


# ==========================================================
# MULTIPLICACIÓN CON PROCEDIMIENTO
# ==========================================================

# Esta función realiza la misma multiplicación,
# pero además guarda el procedimiento utilizado
# para calcular cada entrada de AB.
def multiplicar_matrices_con_procedimiento(
    matriz_1,
    matriz_2
):

    validar_multiplicacion(
        matriz_1,
        matriz_2
    )

    filas_resultado = len(
        matriz_1
    )

    columnas_resultado = len(
        matriz_2[0]
    )

    dimension_comun = len(
        matriz_1[0]
    )

    resultado = []

    procedimiento = []

    for i in range(
        filas_resultado
    ):

        fila_resultado = []

        for j in range(
            columnas_resultado
        ):

            productos = []

            valor = Fraction(
                0
            )

            # Obtenemos la fila de A.
            fila_a = []

            for k in range(
                dimension_comun
            ):

                fila_a.append(
                    matriz_1[i][k]
                )

            # Obtenemos la columna de B.
            columna_b = []

            for k in range(
                dimension_comun
            ):

                columna_b.append(
                    matriz_2[k][j]
                )

            # Aplicamos la regla fila-columna.
            for k in range(
                dimension_comun
            ):

                producto = (
                    matriz_1[i][k]
                    * matriz_2[k][j]
                )

                productos.append(
                    {
                        "valor_a":
                            matriz_1[i][k],

                        "valor_b":
                            matriz_2[k][j],

                        "producto":
                            producto
                    }
                )

                valor += producto

            fila_resultado.append(
                valor
            )

            procedimiento.append(
                {
                    "fila_resultado":
                        i,

                    "columna_resultado":
                        j,

                    "fila_a":
                        fila_a,

                    "columna_b":
                        columna_b,

                    "productos":
                        productos,

                    "resultado":
                        valor
                }
            )

        resultado.append(
            fila_resultado
        )

    return {
        "resultado":
            resultado,

        "procedimiento":
            procedimiento
    }


# ==========================================================
# TRANSPUESTA DE UNA MATRIZ
# ==========================================================

# La transpuesta intercambia filas por columnas.
#
# Si A tiene dimensión m x n,
# entonces Aᵀ tiene dimensión n x m.
def transponer_matriz(
    matriz
):

    validar_matriz(
        matriz
    )

    filas = len(
        matriz
    )

    columnas = len(
        matriz[0]
    )

    transpuesta = []

    # Cada columna de A se convierte
    # en una fila de Aᵀ.
    for j in range(
        columnas
    ):

        fila = []

        for i in range(
            filas
        ):

            fila.append(
                matriz[i][j]
            )

        transpuesta.append(
            fila
        )

    return transpuesta