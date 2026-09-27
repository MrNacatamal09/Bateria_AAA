from teoremas.resumen_teoremas import (
    obtener_teoremas_matrices
)


# ==========================================================
# MÓDULO 3
# ÁLGEBRA DE MATRICES
# ==========================================================


NOMBRE_MODULO = (
    "Álgebra de Matrices"
)


MODULO_DESARROLLADO = True


# ==========================================================
# FUNCIONALIDADES DEL MÓDULO
# ==========================================================

FUNCIONALIDADES_ACTUALES = {
    1: {
        "nombre": "Operaciones básicas",
        "descripcion": (
            "Suma, resta y multiplicación "
            "de una matriz por un escalar."
        )
    },

    2: {
        "nombre": "Multiplicación de matrices",
        "descripcion": (
            "Producto AB mediante la regla "
            "fila-columna, con procedimiento."
        )
    },

    3: {
        "nombre": "Transpuesta",
        "descripcion": (
            "Obtención de Aᵀ intercambiando "
            "filas por columnas."
        )
    },

    4: {
        "nombre": "Matriz inversa",
        "descripcion": (
            "Cálculo de A⁻¹ mediante "
            "Gauss-Jordan sobre [A | I]."
        )
    },

    5: {
        "nombre": "Propiedades de matrices",
        "descripcion": (
            "Verificación de propiedades de suma, "
            "multiplicación, transpuesta e inversa."
        )
    }
}


# ==========================================================
# LOGOTIPO ASCII
# ==========================================================

def obtener_logo_modulo():

    return """
======================================================
 MÓDULO: ÁLGEBRA DE MATRICES
 Operaciones, Multiplicación, Transpuesta e Inversa
 Propiedades de las Matrices
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
        "Este módulo reúne las operaciones fundamentales "
        "con matrices, incluyendo suma, resta, producto "
        "por escalar, multiplicación matricial, transpuesta, "
        "matriz inversa y verificación de propiedades."
    )


# ==========================================================
# MENÚ DEL MÓDULO
# ==========================================================

def obtener_menu_modulo():

    return """
0. Ver Teoremas Clave del Módulo
1. Operaciones Básicas
2. Multiplicación de Matrices
3. Transpuesta
4. Matriz Inversa
5. Propiedades de Matrices
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

    return obtener_teoremas_matrices()


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
            "al Módulo de Álgebra de Matrices."
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
        4,
        5
    ]

    return opcion in opciones_validas