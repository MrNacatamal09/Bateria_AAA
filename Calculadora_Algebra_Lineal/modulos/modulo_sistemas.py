"""
Integra las herramientas del Módulo I de sistemas de ecuaciones lineales.
Expone Gauss-Jordan para que otros módulos reutilicen la reducción existente.
Tema de clase: sistemas lineales, Gauss, Gauss-Jordan y matrices aumentadas.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from teoremas.resumen_teoremas import obtener_teoremas_sistemas

from programas.programa_1.gauss_jordan import gauss_jordan


NOMBRE_MODULO = "Sistemas de Ecuaciones Lineales"

PROGRAMAS_MODULO = {
    1: {
        "nombre": "Programa 1",
        "descripcion": (
            "Resolución de sistemas lineales mediante "
            "Gauss y Gauss-Jordan."
        ),
    },
    2: {
        "nombre": "Programa 2",
        "descripcion": (
            "Análisis mediante Gauss-Jordan, pivotes, "
            "variables básicas y variables libres."
        ),
    },
}


def reducir_por_gauss_jordan(matriz_aumentada):
    """Reduce una matriz aumentada a RREF usando el motor del Programa 1."""
    return gauss_jordan(
        matriz_aumentada
    )


def obtener_logo_modulo():
    """Devuelve el logotipo textual del Módulo I."""
    return """
======================================================
 MÓDULO: SISTEMAS DE ECUACIONES LINEALES
 Métodos de Gauss y Gauss-Jordan
 Resolución y análisis de sistemas
======================================================
"""


def mostrar_logo_modulo():
    """Muestra en consola el logotipo textual del Módulo I."""
    print(
        obtener_logo_modulo()
    )


def obtener_descripcion_modulo():
    """Devuelve una descripción breve del Módulo I."""
    return (
        "Este módulo reúne las herramientas relacionadas "
        "con la resolución y análisis de sistemas de "
        "ecuaciones lineales mediante operaciones "
        "elementales por filas."
    )


def obtener_menu_modulo():
    """Devuelve el menú textual del Módulo I."""
    return """
0. Ver Teoremas Clave del Módulo
1. Programa 1 - Gauss y Gauss-Jordan
2. Programa 2 - Análisis de Pivotes y Variables
"""


def mostrar_menu_modulo():
    """Muestra en consola el logotipo y el menú del Módulo I."""
    mostrar_logo_modulo()

    print(
        obtener_menu_modulo()
    )


def obtener_teoremas_clave():
    """Devuelve los teoremas correspondientes al Módulo I."""
    return obtener_teoremas_sistemas()


def mostrar_teoremas_clave():
    """Muestra en consola los teoremas del Módulo I."""
    print(
        obtener_teoremas_clave()
    )


def obtener_programas_modulo():
    """Devuelve los programas que pertenecen al Módulo I."""
    return PROGRAMAS_MODULO


def obtener_informacion_programa(numero_programa):
    """Devuelve la información de un programa válido del Módulo I."""
    if numero_programa not in PROGRAMAS_MODULO:
        raise ValueError(
            "El programa indicado no pertenece "
            "al Módulo de Sistemas de Ecuaciones Lineales."
        )

    return PROGRAMAS_MODULO[
        numero_programa
    ]


def validar_opcion_modulo(opcion):
    """Indica si la opción recibida pertenece al menú del Módulo I."""
    return opcion in (
        0,
        1,
        2,
    )