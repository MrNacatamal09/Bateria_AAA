from teoremas.resumen_teoremas import (
    obtener_teoremas_sistemas
)


# ==========================================================
# MÓDULO 1
# SISTEMAS DE ECUACIONES LINEALES
# ==========================================================


NOMBRE_MODULO = (
    "Sistemas de Ecuaciones Lineales"
)


# ==========================================================
# PROGRAMAS QUE PERTENECEN AL MÓDULO
# ==========================================================

PROGRAMAS_MODULO = {
    1: {
        "nombre": "Programa 1",
        "descripcion": (
            "Resolución de sistemas lineales mediante "
            "Gauss y Gauss-Jordan."
        )
    },

    2: {
        "nombre": "Programa 2",
        "descripcion": (
            "Análisis mediante Gauss-Jordan, pivotes, "
            "variables básicas y variables libres."
        )
    }
}


# ==========================================================
# LOGOTIPO ASCII
# ==========================================================

def obtener_logo_modulo():

    return """
======================================================
 MÓDULO: SISTEMAS DE ECUACIONES LINEALES
 Métodos de Gauss y Gauss-Jordan
 Resolución y análisis de sistemas
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
        "con la resolución y análisis de sistemas de "
        "ecuaciones lineales mediante operaciones "
        "elementales por filas."
    )


# ==========================================================
# MENÚ DEL MÓDULO
# ==========================================================

def obtener_menu_modulo():

    return """
0. Ver Teoremas Clave del Módulo
1. Programa 1 - Gauss y Gauss-Jordan
2. Programa 2 - Análisis de Pivotes y Variables
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

    return obtener_teoremas_sistemas()


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
            "al Módulo de Sistemas de Ecuaciones Lineales."
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
        1,
        2
    ]

    return opcion in opciones_validas