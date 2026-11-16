"""
Expone las funciones oficiales del módulo de Factorización LU.
Reutiliza los motores matemáticos sin mezclar interfaz y cálculo.
Tema de clase: descomposición A = LU o PA = LU y resolución de Ax = b.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from programas.programa_6.factorizacion_lu import (
    factorizar_lu,
    reconstruir_a_desde_lu as reconstruir_a_desde_lu_motor,
    resolver_sistema_lu,
)

from teoremas.resumen_teoremas_lu import (
    obtener_teoremas_lu,
)


NOMBRE_MODULO = "Factorización LU"
MODULO_DESARROLLADO = True

OPCIONES_MENU = {
    0: "Ver Teoremas Clave del Módulo",
    1: "Factorización LU (A = LU o PA = LU)",
    2: "Resolver Ax = b mediante LU",
    3: "Reconstruir A desde L y U",
}


def obtener_factorizacion(matriz_a):
    """Obtiene P, L y U junto con el procedimiento de reducción."""
    return factorizar_lu(
        matriz_a
    )


def resolver_por_lu(
    matriz_a,
    vector_b,
):
    """Resuelve Ax=b mediante PA=LU, Ly=Pb y Ux=y."""
    return resolver_sistema_lu(
        matriz_a,
        vector_b,
    )


def reconstruir_a_desde_lu(matriz_l, matriz_u, matriz_p=None):
    """Reconstruye A desde L y U, con P opcional."""
    return reconstruir_a_desde_lu_motor(matriz_l, matriz_u, matriz_p)


def obtener_teoremas_clave():
    """Devuelve el resumen teórico del módulo LU."""
    return obtener_teoremas_lu()


def obtener_logo_modulo():
    """Devuelve el logotipo textual del módulo de Factorización LU."""
    return """
============================================================
 MÓDULO V - FACTORIZACIÓN LU
 Descomposición A = LU o PA = LU y Resolución de Sistemas
============================================================
"""


def mostrar_logo_modulo():
    """Muestra en consola el logotipo textual del módulo."""
    print(
        obtener_logo_modulo()
    )


def obtener_descripcion_modulo():
    """Devuelve una descripción breve del módulo."""
    return (
        "Este módulo descompone A mediante LU con pivoteo parcial, "
        "resuelve Ax=b y reconstruye A desde L y U."
    )


def obtener_menu_modulo():
    """Construye el menú actual del Módulo V."""
    return "\n".join(
        f"{numero}. {OPCIONES_MENU[numero]}"
        for numero in sorted(
            OPCIONES_MENU
        )
    )


def modulo_esta_desarrollado():
    """Indica si el módulo de LU se encuentra habilitado."""
    return MODULO_DESARROLLADO
