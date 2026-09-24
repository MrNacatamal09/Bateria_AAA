from fractions import Fraction

from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)


# ==========================================================
# VALIDACIÓN DE Ax = b
# ==========================================================

def validar_ecuacion_matricial(
    matriz_a,
    vector_b
):

    if not matriz_a:
        raise ValueError(
            "La matriz A no puede estar vacía."
        )

    numero_columnas = len(
        matriz_a[0]
    )

    if numero_columnas == 0:
        raise ValueError(
            "La matriz A debe tener al menos una columna."
        )

    for fila in matriz_a:

        if len(fila) != numero_columnas:
            raise ValueError(
                "Todas las filas de A deben tener "
                "la misma cantidad de columnas."
            )

    if len(matriz_a) != len(vector_b):
        raise ValueError(
            "La cantidad de componentes del vector b "
            "debe coincidir con la cantidad de filas de A."
        )


# ==========================================================
# MATRIZ AUMENTADA
# ==========================================================

def construir_matriz_aumentada(
    matriz_a,
    vector_b
):

    matriz_aumentada = []

    for i in range(
        len(matriz_a)
    ):

        fila = list(
            matriz_a[i]
        )

        fila.append(
            vector_b[i]
        )

        matriz_aumentada.append(
            fila
        )

    return matriz_aumentada


# ==========================================================
# SISTEMA HOMOGÉNEO / NO HOMOGÉNEO
# ==========================================================

def es_sistema_homogeneo(
    vector_b
):

    for valor in vector_b:

        if valor != 0:
            return False

    return True


def analizar_soluciones_homogeneas(
    es_homogeneo,
    tipo_sistema,
    variables_libres,
    numero_variables
):

    if not es_homogeneo:

        return {
            "aplica": False,
            "solucion_trivial": "no_aplica",
            "soluciones_no_triviales": "no_aplica",
            "vector_trivial": []
        }

    vector_trivial = []

    for _ in range(
        numero_variables
    ):

        vector_trivial.append(
            Fraction(0)
        )

    if (
        tipo_sistema == "indeterminado"
        and variables_libres
    ):

        soluciones_no_triviales = (
            "existen"
        )

    else:

        soluciones_no_triviales = (
            "no_existen"
        )

    return {
        "aplica": True,
        "solucion_trivial": "existe",
        "soluciones_no_triviales":
            soluciones_no_triviales,
        "vector_trivial":
            vector_trivial
    }


# ==========================================================
# FORMA VECTORIAL DE LA SOLUCIÓN
# ==========================================================

def construir_forma_vectorial(
    resultado_solucion,
    numero_variables
):

    tipo = resultado_solucion[
        "tipo"
    ]

    if tipo == "inconsistente":

        return {
            "tipo": "sin_solucion",
            "vector_particular": [],
            "terminos_parametricos": []
        }

    expresiones = resultado_solucion[
        "expresiones"
    ]

    parametros = resultado_solucion[
        "parametros"
    ]

    vector_particular = []

    for _ in range(
        numero_variables
    ):

        vector_particular.append(
            Fraction(0)
        )

    # Construimos la parte constante
    for j in range(
        numero_variables
    ):

        if j in expresiones:

            vector_particular[j] = (
                expresiones[j][
                    "constante"
                ]
            )

    # Si existe una única solución
    if tipo == "determinado":

        return {
            "tipo": "unica",
            "vector_particular":
                vector_particular,
            "terminos_parametricos": []
        }

    # Si existen variables libres,
    # construimos los vectores dirección.
    terminos_parametricos = []

    for (
        variable_libre,
        parametro
    ) in parametros.items():

        vector_direccion = []

        for _ in range(
            numero_variables
        ):

            vector_direccion.append(
                Fraction(0)
            )

        # La variable libre asociada
        # recibe coeficiente 1.
        vector_direccion[
            variable_libre
        ] = Fraction(1)

        # Obtenemos el efecto del parámetro
        # sobre cada variable básica.
        for (
            variable_basica,
            expresion
        ) in expresiones.items():

            coeficiente = (
                expresion[
                    "parametros"
                ].get(
                    variable_libre,
                    Fraction(0)
                )
            )

            vector_direccion[
                variable_basica
            ] = coeficiente

        terminos_parametricos.append(
            {
                "parametro":
                    parametro,

                "variable_libre":
                    variable_libre,

                "vector":
                    vector_direccion
            }
        )

    return {
        "tipo": "parametrica",
        "vector_particular":
            vector_particular,
        "terminos_parametricos":
            terminos_parametricos
    }


# ==========================================================
# OBTENER LAS COLUMNAS DE A COMO VECTORES
# ==========================================================

def obtener_vectores_columna(
    matriz_a
):

    numero_filas = len(
        matriz_a
    )

    numero_columnas = len(
        matriz_a[0]
    )

    columnas = []

    # j representa las columnas
    for j in range(
        numero_columnas
    ):

        vector = []

        # i representa las filas
        for i in range(
            numero_filas
        ):

            vector.append(
                matriz_a[i][j]
            )

        columnas.append(
            vector
        )

    return columnas


# ==========================================================
# CONSTRUIR SISTEMA HOMOGÉNEO ASOCIADO Ax = 0
# ==========================================================

def construir_sistema_homogeneo(
    matriz_a
):

    matriz_homogenea = []

    for fila in matriz_a:

        nueva_fila = list(
            fila
        )

        nueva_fila.append(
            Fraction(0)
        )

        matriz_homogenea.append(
            nueva_fila
        )

    return matriz_homogenea


# ==========================================================
# OBTENER UNA SOLUCIÓN NO TRIVIAL DE Ax = 0
# ==========================================================

def obtener_solucion_no_trivial(
    resultado_homogeneo,
    numero_variables
):

    variables_libres = (
        resultado_homogeneo[
            "variables_libres"
        ]
    )

    if not variables_libres:
        return None

    resultado_solucion = (
        resultado_homogeneo[
            "solucion"
        ]
    )

    expresiones = resultado_solucion[
        "expresiones"
    ]

    # Elegimos la primera variable libre.
    variable_libre_elegida = (
        variables_libres[0]
    )

    solucion = []

    for _ in range(
        numero_variables
    ):

        solucion.append(
            Fraction(0)
        )

    # Asignamos 1 a la variable libre elegida.
    solucion[
        variable_libre_elegida
    ] = Fraction(1)

    # Las demás variables libres permanecen
    # en cero.
    #
    # Calculamos las variables básicas.
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
                Fraction(0)
            )
        )

        valor += coeficiente

        solucion[
            variable_basica
        ] = valor

    return solucion


# ==========================================================
# MCD SIN UTILIZAR math
# ==========================================================

def calcular_mcd(
    a,
    b
):

    a = abs(
        a
    )

    b = abs(
        b
    )

    # Algoritmo de Euclides
    while b != 0:

        residuo = a % b

        a = b
        b = residuo

    return a


# ==========================================================
# MCM SIN UTILIZAR math
# ==========================================================

def calcular_mcm(
    a,
    b
):

    if (
        a == 0
        or b == 0
    ):

        return 0

    return (
        abs(
            a * b
        )
        //
        calcular_mcd(
            a,
            b
        )
    )


def calcular_mcm_lista(
    numeros
):

    resultado = 1

    for numero in numeros:

        resultado = calcular_mcm(
            resultado,
            numero
        )

    return resultado


def calcular_mcd_lista(
    numeros
):

    if not numeros:
        return 1

    resultado = numeros[0]

    for numero in numeros[1:]:

        resultado = calcular_mcd(
            resultado,
            numero
        )

    return resultado


# ==========================================================
# NORMALIZAR UNA SOLUCIÓN A COEFICIENTES ENTEROS
# ==========================================================

def normalizar_relacion_entera(
    solucion
):

    if solucion is None:
        return None

    denominadores = []

    # Obtenemos todos los denominadores.
    for valor in solucion:

        denominadores.append(
            valor.denominator
        )

    # Calculamos el mínimo común múltiplo
    # sin utilizar la librería math.
    mcm = calcular_mcm_lista(
        denominadores
    )

    enteros = []

    # Eliminamos los denominadores.
    for valor in solucion:

        enteros.append(
            int(
                valor * mcm
            )
        )

    # Obtenemos los valores no nulos
    # para buscar un divisor común.
    valores_no_cero = []

    for valor in enteros:

        if valor != 0:

            valores_no_cero.append(
                abs(valor)
            )

    # Simplificamos la relación.
    if valores_no_cero:

        divisor_comun = (
            calcular_mcd_lista(
                valores_no_cero
            )
        )

        if divisor_comun > 1:

            nuevos_enteros = []

            for valor in enteros:

                nuevos_enteros.append(
                    valor
                    //
                    divisor_comun
                )

            enteros = (
                nuevos_enteros
            )

    # Dejamos positivo el primer
    # coeficiente diferente de cero.
    for valor in enteros:

        if valor != 0:

            if valor < 0:

                nuevos_enteros = []

                for numero in enteros:

                    nuevos_enteros.append(
                        -numero
                    )

                enteros = (
                    nuevos_enteros
                )

            break

    return enteros


# ==========================================================
# ANÁLISIS DE DEPENDENCIA LINEAL
# ==========================================================

def analizar_dependencia_lineal(
    matriz_a
):

    numero_variables = len(
        matriz_a[0]
    )

    # Cada columna de A representa un vector.
    columnas = obtener_vectores_columna(
        matriz_a
    )

    # Construimos [A | 0].
    matriz_homogenea = (
        construir_sistema_homogeneo(
            matriz_a
        )
    )

    # Resolvemos Ax = 0 reutilizando
    # el Programa 2.
    resultado_homogeneo = (
        resolver_programa_2(
            matriz_homogenea,
            numero_variables
        )
    )

    variables_libres = (
        resultado_homogeneo[
            "variables_libres"
        ]
    )

    # Si existe al menos una variable libre,
    # existe una solución no trivial.
    son_dependientes = (
        len(
            variables_libres
        ) > 0
    )

    solucion_no_trivial = None
    relacion_entera = None

    if son_dependientes:

        solucion_no_trivial = (
            obtener_solucion_no_trivial(
                resultado_homogeneo,
                numero_variables
            )
        )

        # Convertimos, cuando es posible,
        # una solución con fracciones en
        # coeficientes enteros equivalentes.
        relacion_entera = (
            normalizar_relacion_entera(
                solucion_no_trivial
            )
        )

    if son_dependientes:

        tipo = "dependientes"

        razon = (
            "El sistema homogéneo asociado Ax = 0 "
            "posee al menos una variable libre. "
            "Por tanto, existe una solución no trivial "
            "y los vectores columna de A son "
            "linealmente dependientes."
        )

    else:

        tipo = "independientes"

        razon = (
            "El sistema homogéneo asociado Ax = 0 "
            "no posee variables libres. "
            "Por tanto, únicamente existe la solución "
            "trivial y los vectores columna de A son "
            "linealmente independientes."
        )

    return {
        "tipo":
            tipo,

        "son_dependientes":
            son_dependientes,

        "son_independientes":
            not son_dependientes,

        "columnas":
            columnas,

        "matriz_homogenea":
            matriz_homogenea,

        "resultado_homogeneo":
            resultado_homogeneo,

        "variables_basicas":
            resultado_homogeneo[
                "variables_basicas"
            ],

        "variables_libres":
            variables_libres,

        "solucion_formateada":
            resultado_homogeneo[
                "solucion_formateada"
            ],

        "solucion_no_trivial":
            solucion_no_trivial,

        # Relación exacta obtenida
        # directamente de Ax = 0.
        "coeficientes_relacion":
            solucion_no_trivial,

        # Relación equivalente usando,
        # cuando es posible, enteros mínimos.
        "relacion_entera":
            relacion_entera,

        "razon":
            razon
    }


# ==========================================================
# RESOLVER ECUACIÓN MATRICIAL Ax = b
# ==========================================================

def resolver_ecuacion_matricial(
    matriz_a,
    vector_b
):

    validar_ecuacion_matricial(
        matriz_a,
        vector_b
    )

    matriz_aumentada = (
        construir_matriz_aumentada(
            matriz_a,
            vector_b
        )
    )

    numero_variables = len(
        matriz_a[0]
    )

    # ======================================================
    # RESOLVEMOS EL SISTEMA ORIGINAL Ax = b
    # ======================================================

    resultado = resolver_programa_2(
        matriz_aumentada,
        numero_variables
    )

    # ======================================================
    # HOMOGÉNEO / NO HOMOGÉNEO
    # ======================================================

    sistema_homogeneo = (
        es_sistema_homogeneo(
            vector_b
        )
    )

    analisis_homogeneo = (
        analizar_soluciones_homogeneas(
            sistema_homogeneo,
            resultado[
                "tipo"
            ],
            resultado[
                "variables_libres"
            ],
            numero_variables
        )
    )

    # ======================================================
    # FORMA VECTORIAL
    # ======================================================

    forma_vectorial = (
        construir_forma_vectorial(
            resultado[
                "solucion"
            ],
            numero_variables
        )
    )

    # ======================================================
    # DEPENDENCIA LINEAL DE LAS COLUMNAS DE A
    # ======================================================

    dependencia_lineal = (
        analizar_dependencia_lineal(
            matriz_a
        )
    )

    # ======================================================
    # RESULTADO COMPLETO
    # ======================================================

    return {
        "matriz_a":
            matriz_a,

        "vector_b":
            vector_b,

        "matriz_aumentada":
            matriz_aumentada,

        "tipo":
            resultado[
                "tipo"
            ],

        "solucion":
            resultado[
                "solucion"
            ],

        "solucion_formateada":
            resultado[
                "solucion_formateada"
            ],

        "matriz_reducida":
            resultado[
                "matriz_reducida"
            ],

        "posiciones_pivote":
            resultado[
                "posiciones_pivote"
            ],

        "columnas_pivote":
            resultado[
                "columnas_pivote"
            ],

        "variables_basicas":
            resultado[
                "variables_basicas"
            ],

        "variables_libres":
            resultado[
                "variables_libres"
            ],

        "historial":
            resultado[
                "historial"
            ],

        "verificacion":
            resultado[
                "verificacion"
            ],

        # Información sobre Ax = b
        "es_homogeneo":
            sistema_homogeneo,

        "tipo_respecto_b": (
            "homogeneo"
            if sistema_homogeneo
            else "no_homogeneo"
        ),

        "analisis_homogeneo":
            analisis_homogeneo,

        # Forma vectorial
        "forma_vectorial":
            forma_vectorial,

        # Dependencia lineal de
        # las columnas de A.
        "dependencia_lineal":
            dependencia_lineal
    }