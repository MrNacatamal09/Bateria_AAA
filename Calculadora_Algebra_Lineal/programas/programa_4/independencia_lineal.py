from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)

from programas.programa_4.construir_matriz_vectores import (
    validar_vectores,
    construir_matriz_columnas,
    construir_matriz_homogenea
)


# ==========================================================
# PROGRAMA 4
# INDEPENDENCIA LINEAL
# ==========================================================


def obtener_columnas_pivote_variables(
    columnas_pivote,
    numero_variables
):

    columnas_variables = []

    for columna in columnas_pivote:

        # Ignoramos la columna aumentada.
        if columna < numero_variables:

            columnas_variables.append(
                columna
            )

    return columnas_variables


# ==========================================================
# ANALIZAR PIVOTES
# ==========================================================

def contar_pivotes(
    columnas_pivote,
    numero_variables
):

    columnas_variables = (
        obtener_columnas_pivote_variables(
            columnas_pivote,
            numero_variables
        )
    )

    return len(
        columnas_variables
    )


# ==========================================================
# DETERMINAR L.I. O L.D.
# ==========================================================

def determinar_independencia(
    numero_vectores,
    numero_pivotes,
    variables_libres
):

    # Un conjunto es linealmente independiente
    # cuando Ax = 0 solamente tiene
    # la solución trivial.
    #
    # Esto ocurre cuando no existen
    # variables libres.

    if (
        numero_pivotes == numero_vectores
        and not variables_libres
    ):

        return {
            "tipo": "LI",
            "es_independiente": True,
            "es_dependiente": False,
            "veredicto": (
                "Los vectores son "
                "LINEALMENTE INDEPENDIENTES."
            ),
            "razon": (
                "No existen variables libres. "
                "Por tanto, el sistema homogéneo "
                "Ax = 0 solamente posee la solución "
                "trivial."
            )
        }

    return {
        "tipo": "LD",
        "es_independiente": False,
        "es_dependiente": True,
        "veredicto": (
            "Los vectores son "
            "LINEALMENTE DEPENDIENTES."
        ),
        "razon": (
            "Existe al menos una variable libre. "
            "Por tanto, el sistema homogéneo "
            "Ax = 0 posee soluciones no triviales."
        )
    }


# ==========================================================
# OBTENER UNA SOLUCIÓN NO TRIVIAL
# ==========================================================

def obtener_solucion_no_trivial(
    resultado_sistema,
    numero_variables
):

    variables_libres = resultado_sistema[
        "variables_libres"
    ]

    if not variables_libres:

        return None

    solucion = resultado_sistema[
        "solucion"
    ]

    expresiones = solucion[
        "expresiones"
    ]

    # Elegimos la primera variable libre.
    variable_libre_elegida = (
        variables_libres[0]
    )

    valores = []

    for _ in range(
        numero_variables
    ):

        valores.append(
            0
        )

    # Asignamos 1 a la variable libre elegida.
    valores[
        variable_libre_elegida
    ] = 1

    # Las demás variables libres permanecen en 0.
    #
    # Ahora calculamos las variables básicas.
    for (
        variable_basica,
        expresion
    ) in expresiones.items():

        valor = expresion[
            "constante"
        ]

        coeficiente = (
            expresion[
                "parametros"
            ].get(
                variable_libre_elegida,
                0
            )
        )

        valor += coeficiente

        valores[
            variable_basica
        ] = valor

    return valores


# ==========================================================
# ANALIZAR INDEPENDENCIA LINEAL
# ==========================================================

def analizar_independencia_lineal(
    vectores
):

    # ======================================================
    # VALIDACIÓN
    # ======================================================

    validar_vectores(
        vectores
    )

    cantidad_vectores = len(
        vectores
    )

    dimension = len(
        vectores[0]
    )

    # ======================================================
    # MATRIZ DE COLUMNAS A
    # ======================================================

    matriz_a = construir_matriz_columnas(
        vectores
    )

    # ======================================================
    # SISTEMA HOMOGÉNEO [A | 0]
    # ======================================================

    matriz_homogenea = (
        construir_matriz_homogenea(
            vectores
        )
    )

    # Hay una variable por cada vector.
    numero_variables = (
        cantidad_vectores
    )

    # ======================================================
    # REUTILIZAMOS PROGRAMA 2
    # ======================================================

    resultado_sistema = (
        resolver_programa_2(
            matriz_homogenea,
            numero_variables
        )
    )

    # ======================================================
    # PIVOTES
    # ======================================================

    columnas_pivote = (
        resultado_sistema[
            "columnas_pivote"
        ]
    )

    columnas_pivote_variables = (
        obtener_columnas_pivote_variables(
            columnas_pivote,
            numero_variables
        )
    )

    numero_pivotes = contar_pivotes(
        columnas_pivote,
        numero_variables
    )

    # ======================================================
    # VARIABLES
    # ======================================================

    variables_basicas = (
        resultado_sistema[
            "variables_basicas"
        ]
    )

    variables_libres = (
        resultado_sistema[
            "variables_libres"
        ]
    )

    # ======================================================
    # VEREDICTO L.I. / L.D.
    # ======================================================

    analisis = determinar_independencia(
        cantidad_vectores,
        numero_pivotes,
        variables_libres
    )

    # ======================================================
    # SOLUCIÓN NO TRIVIAL
    # ======================================================

    solucion_no_trivial = None

    if analisis[
        "es_dependiente"
    ]:

        solucion_no_trivial = (
            obtener_solucion_no_trivial(
                resultado_sistema,
                numero_variables
            )
        )

    # ======================================================
    # RESULTADO
    # ======================================================

    return {
        # Datos originales
        "vectores":
            vectores,

        "cantidad_vectores":
            cantidad_vectores,

        "dimension":
            dimension,

        # Matrices
        "matriz_a":
            matriz_a,

        "matriz_homogenea":
            matriz_homogenea,

        "matriz_reducida":
            resultado_sistema[
                "matriz_reducida"
            ],

        # Pivotes
        "numero_pivotes":
            numero_pivotes,

        "columnas_pivote":
            columnas_pivote_variables,

        "posiciones_pivote":
            resultado_sistema[
                "posiciones_pivote"
            ],

        # Variables
        "variables_basicas":
            variables_basicas,

        "variables_libres":
            variables_libres,

        # Solución de Ax = 0
        "solucion":
            resultado_sistema[
                "solucion"
            ],

        "solucion_formateada":
            resultado_sistema[
                "solucion_formateada"
            ],

        "solucion_no_trivial":
            solucion_no_trivial,

        # Procedimiento
        "historial":
            resultado_sistema[
                "historial"
            ],

        # Clasificación
        "tipo":
            analisis[
                "tipo"
            ],

        "es_independiente":
            analisis[
                "es_independiente"
            ],

        "es_dependiente":
            analisis[
                "es_dependiente"
            ],

        "veredicto":
            analisis[
                "veredicto"
            ],

        "razon":
            analisis[
                "razon"
            ]
    }