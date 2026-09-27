from copy import deepcopy

from programas.programa_2.gauss_jordan import (
    gauss_jordan
)

from programas.programa_3.matrices import (
    validar_matriz,
    multiplicar_matrices
)

from programas.programa_3.propiedades_matrices_generales import (
    crear_matriz_identidad,
    matrices_iguales
)

from programas.determinantes.determinante import (
    calcular_determinante
)


# ==========================================================
# INVERSA DE UNA MATRIZ
# MÉTODO DE GAUSS-JORDAN
# ==========================================================


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
            "La matriz debe ser cuadrada para "
            "poder calcular su inversa."
        )


# ==========================================================
# CONSTRUIR MATRIZ AUMENTADA [A | I]
# ==========================================================

def construir_matriz_aumentada_inversa(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    identidad = crear_matriz_identidad(
        orden
    )

    matriz_aumentada = []

    for i in range(
        orden
    ):

        fila = []

        # Parte izquierda: A
        for valor in matriz[i]:

            fila.append(
                valor
            )

        # Parte derecha: I
        for valor in identidad[i]:

            fila.append(
                valor
            )

        matriz_aumentada.append(
            fila
        )

    return matriz_aumentada


# ==========================================================
# EXTRAER LADO IZQUIERDO
# ==========================================================

def extraer_lado_izquierdo(
    matriz_aumentada,
    orden
):

    lado_izquierdo = []

    for i in range(
        orden
    ):

        fila = []

        for j in range(
            orden
        ):

            fila.append(
                matriz_aumentada[i][j]
            )

        lado_izquierdo.append(
            fila
        )

    return lado_izquierdo


# ==========================================================
# EXTRAER LADO DERECHO
# ==========================================================

def extraer_lado_derecho(
    matriz_aumentada,
    orden
):

    lado_derecho = []

    for i in range(
        orden
    ):

        fila = []

        for j in range(
            orden,
            orden * 2
        ):

            fila.append(
                matriz_aumentada[i][j]
            )

        lado_derecho.append(
            fila
        )

    return lado_derecho


# ==========================================================
# VERIFICAR INVERSA
#
# A A⁻¹ = I
# A⁻¹ A = I
# ==========================================================

def verificar_inversa(
    matriz,
    inversa
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    identidad = crear_matriz_identidad(
        orden
    )

    producto_izquierdo = multiplicar_matrices(
        matriz,
        inversa
    )

    producto_derecho = multiplicar_matrices(
        inversa,
        matriz
    )

    verifica_izquierda = matrices_iguales(
        producto_izquierdo,
        identidad
    )

    verifica_derecha = matrices_iguales(
        producto_derecho,
        identidad
    )

    return {
        "identidad":
            identidad,

        "producto_a_inversa":
            producto_izquierdo,

        "producto_inversa_a":
            producto_derecho,

        "verifica_a_inversa":
            verifica_izquierda,

        "verifica_inversa_a":
            verifica_derecha,

        "verificada":
            (
                verifica_izquierda
                and verifica_derecha
            )
    }


# ==========================================================
# CALCULAR INVERSA
# ==========================================================

def calcular_inversa(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    matriz_original = deepcopy(
        matriz
    )

    orden = len(
        matriz_original
    )

    # ======================================================
    # DETERMINANTE
    # ======================================================

    determinante = calcular_determinante(
        matriz_original
    )

    # Si el determinante es cero,
    # la matriz no es invertible.
    if determinante == 0:

        return {
            "matriz_original":
                matriz_original,

            "orden":
                orden,

            "determinante":
                determinante,

            "es_invertible":
                False,

            "matriz_aumentada":
                None,

            "matriz_reducida":
                None,

            "inversa":
                None,

            "historial":
                [],

            "posiciones_pivote":
                [],

            "verificacion":
                None,

            "mensaje":
                (
                    "La matriz no es invertible porque "
                    "su determinante es igual a 0."
                )
        }

    # ======================================================
    # CONSTRUIMOS [A | I]
    # ======================================================

    matriz_aumentada = (
        construir_matriz_aumentada_inversa(
            matriz_original
        )
    )

    # ======================================================
    # GAUSS-JORDAN
    #
    # Reutilizamos el motor del Programa 2.
    # Las operaciones se aplican sobre toda la fila,
    # por lo que transforman simultáneamente A e I.
    # ======================================================

    resultado_gauss_jordan = gauss_jordan(
        matriz_aumentada,
        orden
    )

    matriz_reducida = (
        resultado_gauss_jordan[
            "matriz_reducida"
        ]
    )

    # ======================================================
    # EXTRAEMOS LA PARTE IZQUIERDA
    # ======================================================

    lado_izquierdo = extraer_lado_izquierdo(
        matriz_reducida,
        orden
    )

    # ======================================================
    # COMPROBAMOS QUE SE OBTUVO I
    # ======================================================

    identidad = crear_matriz_identidad(
        orden
    )

    izquierda_es_identidad = matrices_iguales(
        lado_izquierdo,
        identidad
    )

    if not izquierda_es_identidad:

        return {
            "matriz_original":
                matriz_original,

            "orden":
                orden,

            "determinante":
                determinante,

            "es_invertible":
                False,

            "matriz_aumentada":
                matriz_aumentada,

            "matriz_reducida":
                matriz_reducida,

            "inversa":
                None,

            "historial":
                resultado_gauss_jordan[
                    "historial"
                ],

            "posiciones_pivote":
                resultado_gauss_jordan[
                    "posiciones_pivote"
                ],

            "verificacion":
                None,

            "mensaje":
                (
                    "No fue posible transformar la parte "
                    "izquierda de la matriz aumentada "
                    "en la matriz identidad."
                )
        }

    # ======================================================
    # EXTRAEMOS A⁻¹
    # ======================================================

    inversa = extraer_lado_derecho(
        matriz_reducida,
        orden
    )

    # ======================================================
    # VERIFICACIÓN
    # ======================================================

    verificacion = verificar_inversa(
        matriz_original,
        inversa
    )

    # ======================================================
    # RESULTADO
    # ======================================================

    return {
        "matriz_original":
            matriz_original,

        "orden":
            orden,

        "determinante":
            determinante,

        "es_invertible":
            True,

        "matriz_aumentada":
            matriz_aumentada,

        "matriz_reducida":
            matriz_reducida,

        "inversa":
            inversa,

        "historial":
            resultado_gauss_jordan[
                "historial"
            ],

        "posiciones_pivote":
            resultado_gauss_jordan[
                "posiciones_pivote"
            ],

        "verificacion":
            verificacion,

        "mensaje":
            (
                "La matriz es invertible y su inversa "
                "fue obtenida mediante Gauss-Jordan."
            )
    }