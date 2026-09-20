from fractions import Fraction

from programas.programa_2.resolver_programa_2 import (
    resolver_programa_2
)


# Revisamos que A y b tengan dimensiones válidas
def validar_ecuacion_matricial(
    matriz_a,
    vector_b
):

    if not matriz_a:

        raise ValueError(
            "La matriz A no puede estar vacía."
        )

    if not vector_b:

        raise ValueError(
            "El vector b no puede estar vacío."
        )

    numero_columnas = len(
        matriz_a[0]
    )

    if numero_columnas == 0:

        raise ValueError(
            "La matriz A debe tener al menos una columna."
        )

    # Revisamos que A sea una matriz rectangular
    for i in range(
        len(matriz_a)
    ):

        if len(matriz_a[i]) != numero_columnas:

            raise ValueError(
                "Todas las filas de A deben tener "
                "la misma cantidad de columnas."
            )

    # b debe tener una entrada por cada fila de A
    if len(vector_b) != len(matriz_a):

        raise ValueError(
            "El vector b debe tener la misma cantidad "
            "de elementos que filas tiene A."
        )


# Construimos la matriz aumentada [A|b]
def construir_matriz_aumentada(
    matriz_a,
    vector_b
):

    validar_ecuacion_matricial(
        matriz_a,
        vector_b
    )

    matriz_aumentada = []

    # i representa las filas
    for i in range(
        len(matriz_a)
    ):

        fila = []

        # j representa las columnas de A
        for j in range(
            len(matriz_a[i])
        ):

            fila.append(
                matriz_a[i][j]
            )

        fila.append(
            vector_b[i]
        )

        matriz_aumentada.append(
            fila
        )

    return matriz_aumentada


# Determinamos si Ax = b es un sistema homogéneo
def es_sistema_homogeneo(
    vector_b
):

    for valor in vector_b:

        if valor != 0:

            return False

    return True


# Analizamos solución trivial y soluciones no triviales
def analizar_soluciones_homogeneas(
    es_homogeneo,
    tipo_sistema,
    variables_libres,
    numero_variables
):

    # La clasificación trivial/no trivial se utiliza
    # principalmente para sistemas homogéneos
    if not es_homogeneo:

        return {
            "aplica": False,
            "solucion_trivial": "no_aplica",
            "soluciones_no_triviales": "no_aplica",
            "vector_trivial": []
        }

    vector_trivial = [
        Fraction(0)
        for _ in range(
            numero_variables
        )
    ]

    # Todo sistema homogéneo posee la solución x = 0
    solucion_trivial = "existe"

    # Si existen variables libres,
    # también existen soluciones distintas de cero
    if (
        tipo_sistema == "indeterminado"
        and variables_libres
    ):

        soluciones_no_triviales = "existen"

    else:

        soluciones_no_triviales = "no_existen"

    return {
        "aplica": True,
        "solucion_trivial": solucion_trivial,
        "soluciones_no_triviales": soluciones_no_triviales,
        "vector_trivial": vector_trivial
    }


# Construimos la forma vectorial de la solución
def construir_forma_vectorial(
    resultado_solucion,
    numero_variables
):

    tipo = resultado_solucion[
        "tipo"
    ]

    # Un sistema inconsistente no posee solución
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

    vector_particular = [
        Fraction(0)
        for _ in range(
            numero_variables
        )
    ]

    # Obtenemos la parte constante de cada variable
    for j in range(
        numero_variables
    ):

        if j in expresiones:

            vector_particular[j] = (
                expresiones[j][
                    "constante"
                ]
            )

        else:

            # Una variable libre no tiene
            # término constante propio
            vector_particular[j] = (
                Fraction(0)
            )

    # Solución única
    if tipo == "determinado":

        return {
            "tipo": "unica",
            "vector_particular": vector_particular,
            "terminos_parametricos": []
        }

    # Solución paramétrica
    terminos_parametricos = []

    # Cada variable libre genera un vector dirección
    for variable_libre, parametro in (
        parametros.items()
    ):

        vector_direccion = [
            Fraction(0)
            for _ in range(
                numero_variables
            )
        ]

        # La variable libre tiene coeficiente 1
        # con respecto a su propio parámetro
        vector_direccion[
            variable_libre
        ] = Fraction(1)

        # Revisamos cómo aparece este parámetro
        # en cada variable básica
        for variable_basica, expresion in (
            expresiones.items()
        ):

            coeficiente = expresion[
                "parametros"
            ].get(
                variable_libre,
                Fraction(0)
            )

            vector_direccion[
                variable_basica
            ] = coeficiente

        terminos_parametricos.append({
            "parametro": parametro,
            "variable_libre": variable_libre,
            "vector": vector_direccion
        })

    return {
        "tipo": "parametrica",
        "vector_particular": vector_particular,
        "terminos_parametricos": terminos_parametricos
    }


# Resolvemos la ecuación matricial Ax = b
def resolver_ecuacion_matricial(
    matriz_a,
    vector_b
):

    matriz_aumentada = (
        construir_matriz_aumentada(
            matriz_a,
            vector_b
        )
    )

    numero_variables = len(
        matriz_a[0]
    )

    resultado = resolver_programa_2(
        matriz_aumentada,
        numero_variables
    )

    tipo = resultado[
        "tipo"
    ]

    solucion = resultado[
        "solucion"
    ]

    variables_libres = resultado[
        "variables_libres"
    ]

    # Revisamos si b es el vector cero
    sistema_homogeneo = (
        es_sistema_homogeneo(
            vector_b
        )
    )

    tipo_respecto_b = (
        "homogeneo"
        if sistema_homogeneo
        else "no_homogeneo"
    )

    # Analizamos solución trivial y no trivial
    analisis_homogeneo = (
        analizar_soluciones_homogeneas(
            sistema_homogeneo,
            tipo,
            variables_libres,
            numero_variables
        )
    )

    # Construimos la representación vectorial
    forma_vectorial = (
        construir_forma_vectorial(
            solucion,
            numero_variables
        )
    )

    return {
        "matriz_a": matriz_a,
        "vector_b": vector_b,
        "matriz_aumentada": matriz_aumentada,

        "tipo": tipo,

        "es_homogeneo": sistema_homogeneo,
        "tipo_respecto_b": tipo_respecto_b,

        "analisis_homogeneo": analisis_homogeneo,

        "solucion": solucion,

        "solucion_formateada": resultado[
            "solucion_formateada"
        ],

        "forma_vectorial": forma_vectorial,

        "matriz_reducida": resultado[
            "matriz_reducida"
        ],

        "columnas_pivote": resultado[
            "columnas_pivote"
        ],

        "variables_basicas": resultado[
            "variables_basicas"
        ],

        "variables_libres": resultado[
            "variables_libres"
        ],

        "historial": resultado[
            "historial"
        ],

        "verificacion": resultado[
            "verificacion"
        ]
    }