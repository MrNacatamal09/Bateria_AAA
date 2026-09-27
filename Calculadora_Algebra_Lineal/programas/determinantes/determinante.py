from fractions import Fraction


# ==========================================================
# DETERMINANTES
# MOTOR MATEMÁTICO
# ==========================================================


# ==========================================================
# VALIDAR MATRIZ
# ==========================================================

def validar_matriz(
    matriz
):

    if not matriz:

        raise ValueError(
            "La matriz no puede estar vacía."
        )

    columnas = len(
        matriz[0]
    )

    if columnas == 0:

        raise ValueError(
            "La matriz debe tener al menos "
            "una columna."
        )

    for fila in matriz:

        if len(fila) != columnas:

            raise ValueError(
                "Todas las filas deben tener "
                "la misma cantidad de columnas."
            )


# ==========================================================
# VALIDAR MATRIZ CUADRADA
# ==========================================================

def validar_matriz_cuadrada(
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

    if filas != columnas:

        raise ValueError(
            "El determinante solamente puede "
            "calcularse para matrices cuadradas."
        )


# ==========================================================
# OBTENER MENOR
#
# Mij se obtiene eliminando la fila i
# y la columna j de la matriz.
# ==========================================================

def obtener_menor(
    matriz,
    fila_eliminar,
    columna_eliminar
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    if (
        fila_eliminar < 0
        or fila_eliminar >= orden
    ):

        raise ValueError(
            "La fila indicada no es válida."
        )

    if (
        columna_eliminar < 0
        or columna_eliminar >= orden
    ):

        raise ValueError(
            "La columna indicada no es válida."
        )

    menor = []

    for i in range(
        orden
    ):

        if i == fila_eliminar:

            continue

        nueva_fila = []

        for j in range(
            orden
        ):

            if j == columna_eliminar:

                continue

            nueva_fila.append(
                matriz[i][j]
            )

        menor.append(
            nueva_fila
        )

    return menor


# ==========================================================
# SIGNO DEL COFACTOR
#
# (-1)^(i+j)
# ==========================================================

def obtener_signo_cofactor(
    fila,
    columna
):

    # Python comienza los índices en 0.
    # La paridad del signo se conserva.

    if (
        (fila + columna) % 2
        == 0
    ):

        return Fraction(
            1
        )

    return Fraction(
        -1
    )


# ==========================================================
# CONTAR CEROS DE UNA FILA
# ==========================================================

def contar_ceros_fila(
    matriz,
    fila
):

    validar_matriz(
        matriz
    )

    if (
        fila < 0
        or fila >= len(matriz)
    ):

        raise ValueError(
            "La fila indicada no es válida."
        )

    cantidad = 0

    for valor in matriz[
        fila
    ]:

        if valor == 0:

            cantidad += 1

    return cantidad


# ==========================================================
# CONTAR CEROS DE UNA COLUMNA
# ==========================================================

def contar_ceros_columna(
    matriz,
    columna
):

    validar_matriz(
        matriz
    )

    if (
        columna < 0
        or columna >= len(matriz[0])
    ):

        raise ValueError(
            "La columna indicada no es válida."
        )

    cantidad = 0

    for fila in range(
        len(matriz)
    ):

        if (
            matriz[fila][columna]
            == 0
        ):

            cantidad += 1

    return cantidad


# ==========================================================
# SELECCIONAR FILA O COLUMNA
#
# Se busca la fila o columna que tenga
# la mayor cantidad de ceros.
# ==========================================================

def seleccionar_fila_o_columna(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    mejor_tipo = "fila"

    mejor_indice = 0

    mayor_cantidad_ceros = (
        contar_ceros_fila(
            matriz,
            0
        )
    )

    # ======================================================
    # REVISAMOS LAS FILAS
    # ======================================================

    for i in range(
        orden
    ):

        cantidad = contar_ceros_fila(
            matriz,
            i
        )

        if (
            cantidad
            > mayor_cantidad_ceros
        ):

            mayor_cantidad_ceros = (
                cantidad
            )

            mejor_tipo = "fila"

            mejor_indice = i

    # ======================================================
    # REVISAMOS LAS COLUMNAS
    # ======================================================

    for j in range(
        orden
    ):

        cantidad = contar_ceros_columna(
            matriz,
            j
        )

        if (
            cantidad
            > mayor_cantidad_ceros
        ):

            mayor_cantidad_ceros = (
                cantidad
            )

            mejor_tipo = "columna"

            mejor_indice = j

    return (
        mejor_tipo,
        mejor_indice
    )


# ==========================================================
# DETERMINANTE 2 x 2
#
# |a b|
# |c d|
#
# det(A) = ad - bc
# ==========================================================

def calcular_determinante_2x2(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    if len(matriz) != 2:

        raise ValueError(
            "Esta función solamente acepta "
            "matrices de orden 2."
        )

    a = matriz[0][0]

    b = matriz[0][1]

    c = matriz[1][0]

    d = matriz[1][1]

    determinante = (
        a * d
        - b * c
    )

    return determinante


# ==========================================================
# DETERMINANTE GENERAL
#
# Desarrollo por cofactores.
# ==========================================================

def calcular_determinante(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    # ======================================================
    # MATRIZ 1 x 1
    # ======================================================

    if orden == 1:

        return matriz[0][0]

    # ======================================================
    # MATRIZ 2 x 2
    # ======================================================

    if orden == 2:

        return calcular_determinante_2x2(
            matriz
        )

    # ======================================================
    # MATRICES DE ORDEN 3 O MAYOR
    #
    # Elegimos la fila o columna con más ceros.
    # ======================================================

    tipo, indice = seleccionar_fila_o_columna(
        matriz
    )

    determinante = Fraction(
        0
    )

    # ======================================================
    # DESARROLLO POR FILA
    # ======================================================

    if tipo == "fila":

        fila = indice

        for columna in range(
            orden
        ):

            elemento = matriz[
                fila
            ][
                columna
            ]

            # Un elemento cero no aporta
            # nada al desarrollo.
            if elemento == 0:

                continue

            menor = obtener_menor(
                matriz,
                fila,
                columna
            )

            determinante_menor = (
                calcular_determinante(
                    menor
                )
            )

            signo = obtener_signo_cofactor(
                fila,
                columna
            )

            termino = (
                elemento
                * signo
                * determinante_menor
            )

            determinante += termino

    # ======================================================
    # DESARROLLO POR COLUMNA
    # ======================================================

    elif tipo == "columna":

        columna = indice

        for fila in range(
            orden
        ):

            elemento = matriz[
                fila
            ][
                columna
            ]

            if elemento == 0:

                continue

            menor = obtener_menor(
                matriz,
                fila,
                columna
            )

            determinante_menor = (
                calcular_determinante(
                    menor
                )
            )

            signo = obtener_signo_cofactor(
                fila,
                columna
            )

            termino = (
                elemento
                * signo
                * determinante_menor
            )

            determinante += termino

    return determinante


# ==========================================================
# CALCULAR COFACTOR
#
# Cij = (-1)^(i+j) det(Mij)
# ==========================================================

def calcular_cofactor(
    matriz,
    fila,
    columna
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    if (
        fila < 0
        or fila >= orden
    ):

        raise ValueError(
            "La fila indicada no es válida."
        )

    if (
        columna < 0
        or columna >= orden
    ):

        raise ValueError(
            "La columna indicada no es válida."
        )

    # ======================================================
    # MATRIZ 1 x 1
    # ======================================================

    if orden == 1:

        return Fraction(
            1
        )

    # ======================================================
    # OBTENEMOS EL MENOR
    # ======================================================

    menor = obtener_menor(
        matriz,
        fila,
        columna
    )

    # ======================================================
    # DETERMINANTE DEL MENOR
    # ======================================================

    determinante_menor = (
        calcular_determinante(
            menor
        )
    )

    # ======================================================
    # SIGNO
    # ======================================================

    signo = obtener_signo_cofactor(
        fila,
        columna
    )

    # ======================================================
    # COFACTOR
    # ======================================================

    cofactor = (
        signo
        * determinante_menor
    )

    return cofactor


# ==========================================================
# DETERMINAR SI UNA MATRIZ ES INVERTIBLE
#
# A es invertible si det(A) != 0.
# ==========================================================

def es_matriz_invertible(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    determinante = calcular_determinante(
        matriz
    )

    return (
        determinante != 0
    )