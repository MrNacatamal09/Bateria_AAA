from teoremas.resumen_teoremas import (
    obtener_teoremas_vectores
)


# ==========================================================
# MÓDULO 2
# VECTORES E INDEPENDENCIA LINEAL
# ==========================================================


NOMBRE_MODULO = (
    "Vectores e Independencia Lineal"
)


# ==========================================================
# PROGRAMAS QUE PERTENECEN AL MÓDULO
# ==========================================================

PROGRAMAS_MODULO = {
    3: {
        "nombre": "Programa 3",
        "descripcion": (
            "Vectores, matrices, combinación lineal, "
            "ecuación Ax = b y propiedades."
        )
    },

    4: {
        "nombre": "Programa 4",
        "descripcion": (
            "Independencia y dependencia lineal "
            "de un conjunto de vectores."
        )
    }
}


# ==========================================================
# LOGOTIPO ASCII
# ==========================================================

def obtener_logo_modulo():

    return """
======================================================
 MÓDULO: VECTORES E INDEPENDENCIA LINEAL
 Combinaciones Lineales, L.I. y L.D.
 A x = 0
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
        "Este módulo reúne las herramientas relacionadas "
        "con vectores, combinaciones lineales, ecuaciones "
        "matriciales e independencia lineal."
    )


# ==========================================================
# MENÚ DEL MÓDULO
# ==========================================================

def obtener_menu_modulo():

    return """
0. Ver Teoremas Clave del Módulo
3. Programa 3 - Vectores y Matrices
4. Programa 4 - Independencia Lineal
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

    return obtener_teoremas_vectores()


def mostrar_teoremas_clave():

    print(
        obtener_teoremas_clave()
    )


# ==========================================================
# INFORMACIÓN DE LOS PROGRAMAS
# ==========================================================

def obtener_programas_modulo():

    return PROGRAMAS_MODULO


def obtener_informacion_programa(
    numero_programa
):

    if numero_programa not in PROGRAMAS_MODULO:

        raise ValueError(
            "El programa indicado no pertenece "
            "al Módulo de Vectores e Independencia Lineal."
        )

    return PROGRAMAS_MODULO[
        numero_programa
    ]


# ==========================================================
# VALIDAR OPCIÓN DEL MENÚ
# ==========================================================

def validar_opcion_modulo(
    opcion
):

    opciones_validas = [
        0,
        3,
        4
    ]

    return opcion in opciones_validas