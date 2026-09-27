from teoremas.resumen_teoremas import (
    obtener_teoremas_determinantes
)


# ==========================================================
# MÓDULO 4
# DETERMINANTES
# ==========================================================


NOMBRE_MODULO = (
    "Determinantes"
)


MODULO_DESARROLLADO = True


# ==========================================================
# FUNCIONALIDADES DEL MÓDULO
# ==========================================================

FUNCIONALIDADES_ACTUALES = {
    1: {
        "nombre": "Determinante",
        "descripcion": (
            "Cálculo del determinante de una "
            "matriz cuadrada."
        )
    },

    2: {
        "nombre": "Menores y Cofactores",
        "descripcion": (
            "Obtención de menores Mᵢⱼ "
            "y cofactores Cᵢⱼ."
        )
    },

    3: {
        "nombre": "Desarrollo por Cofactores",
        "descripcion": (
            "Cálculo paso a paso seleccionando "
            "una fila o columna conveniente."
        )
    },

    4: {
        "nombre": "Análisis de Invertibilidad",
        "descripcion": (
            "Determinación de invertibilidad "
            "mediante el valor del determinante."
        )
    }
}


# ==========================================================
# LOGOTIPO ASCII
# ==========================================================

def obtener_logo_modulo():

    return """
======================================================
 MÓDULO: DETERMINANTES
 Menores, Cofactores y Desarrollo por Cofactores
 Análisis de Invertibilidad
======================================================
"""


def mostrar_logo_modulo():

    print(
        obtener_logo_modulo()
    )


# ==========================================================
# DESCRIPCIÓN DEL MÓDULO
# ==========================================================

def obtener_descripcion_modulo():

    return (
        "Este módulo permite calcular determinantes "
        "de matrices cuadradas, obtener menores y "
        "cofactores, realizar desarrollo por cofactores "
        "y analizar si una matriz es invertible."
    )


# ==========================================================
# MENÚ DEL MÓDULO
# ==========================================================

def obtener_menu_modulo():

    return """
0. Ver Teoremas Clave del Módulo
1. Calcular Determinante
2. Menores y Cofactores
3. Desarrollo por Cofactores
4. Analizar Invertibilidad
"""


def mostrar_menu_modulo():

    mostrar_logo_modulo()

    print(
        obtener_menu_modulo()
    )


# ==========================================================
# TEOREMAS CLAVE
# ==========================================================

def obtener_teoremas_clave():

    return obtener_teoremas_determinantes()


def mostrar_teoremas_clave():

    print(
        obtener_teoremas_clave()
    )


# ==========================================================
# FUNCIONALIDADES
# ==========================================================

def obtener_funcionalidades_actuales():

    return FUNCIONALIDADES_ACTUALES


def obtener_informacion_funcionalidad(
    numero_funcionalidad
):

    if (
        numero_funcionalidad
        not in FUNCIONALIDADES_ACTUALES
    ):

        raise ValueError(
            "La funcionalidad indicada no pertenece "
            "al Módulo de Determinantes."
        )

    return FUNCIONALIDADES_ACTUALES[
        numero_funcionalidad
    ]


# ==========================================================
# ESTADO DEL MÓDULO
# ==========================================================

def modulo_esta_desarrollado():

    return MODULO_DESARROLLADO


# ==========================================================
# VALIDAR OPCIÓN
# ==========================================================

def validar_opcion_modulo(
    opcion
):

    opciones_validas = [
        0,
        1,
        2,
        3,
        4
    ]

    return opcion in opciones_validas