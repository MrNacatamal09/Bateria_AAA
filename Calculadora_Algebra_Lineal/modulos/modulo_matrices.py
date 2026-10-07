"""
Integra las operaciones generales del Módulo III de matrices.
Reutiliza los motores de suma, resta, escalar, producto y transposición.
Tema de clase: operaciones y propiedades generales de matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from teoremas.resumen_teoremas import obtener_teoremas_matrices

from programas.programa_3.matrices import (
    sumar_matrices,
    restar_matrices,
    multiplicar_matriz_escalar,
    multiplicar_matrices,
    transponer_matriz,
)


NOMBRE_MODULO = "Álgebra de Matrices"
MODULO_DESARROLLADO = True

OPCIONES_MENU = {
    0: "Ver Teoremas Clave del Módulo",
    1: "Suma",
    2: "Resta",
    3: "Multiplicación por Escalar",
    4: "Producto Matricial",
    5: "Transposición",
}


def sumar(matriz_a, matriz_b):
    """Suma A y B cuando poseen las mismas dimensiones."""
    return sumar_matrices(matriz_a, matriz_b)


def restar(matriz_a, matriz_b):
    """Calcula A - B cuando ambas matrices tienen igual dimensión."""
    return restar_matrices(matriz_a, matriz_b)


def multiplicar_por_escalar(matriz_a, escalar):
    """Calcula rA multiplicando cada entrada de A por r."""
    return multiplicar_matriz_escalar(matriz_a, escalar)


def producto_matricial(matriz_a, matriz_b):
    """Calcula AB cuando columnas de A igualan filas de B."""
    return multiplicar_matrices(matriz_a, matriz_b)


def transponer(matriz_a):
    """Calcula Aᵀ intercambiando filas por columnas."""
    return transponer_matriz(matriz_a)


def obtener_logo_modulo():
    """Devuelve el logotipo textual del Módulo III."""
    return """
============================================================
 MÓDULO III - ÁLGEBRA DE MATRICES
 Operaciones y propiedades generales de matrices
============================================================
"""


def mostrar_logo_modulo():
    """Muestra en consola el logotipo textual del módulo."""
    print(obtener_logo_modulo())


def obtener_descripcion_modulo():
    """Devuelve una descripción breve del Módulo III."""
    return (
        "Este módulo reúne las operaciones fundamentales con matrices: "
        "suma, resta, producto por escalar, producto matricial, transposición "
        "y propiedades generales."
    )


def obtener_menu_modulo():
    """Construye el menú oficial de opciones 0 a 5 del Módulo III."""
    return "\n".join(
        f"{numero}. {OPCIONES_MENU[numero]}"
        for numero in range(6)
    )


def mostrar_menu_modulo():
    """Muestra el logotipo y el menú del Módulo III."""
    mostrar_logo_modulo()
    print(obtener_menu_modulo())


def obtener_teoremas_clave():
    """Devuelve los teoremas correspondientes a operaciones con matrices."""
    return obtener_teoremas_matrices()


def mostrar_teoremas_clave():
    """Muestra en consola los teoremas del Módulo III."""
    print(obtener_teoremas_clave())


def obtener_funcionalidades_actuales():
    """Devuelve una copia de las opciones oficiales del Módulo III."""
    return OPCIONES_MENU.copy()


def obtener_informacion_funcionalidad(numero_funcionalidad):
    """Devuelve el nombre de una opción válida del Módulo III."""
    if numero_funcionalidad not in OPCIONES_MENU:
        raise ValueError(
            "La funcionalidad indicada no pertenece al Módulo de Matrices."
        )

    return {
        "numero": numero_funcionalidad,
        "nombre": OPCIONES_MENU[numero_funcionalidad],
    }


def modulo_esta_desarrollado():
    """Indica si el módulo de matrices se encuentra habilitado."""
    return MODULO_DESARROLLADO


def validar_opcion_modulo(opcion):
    """Devuelve True cuando la opción recibida pertenece al menú 0–5."""
    return opcion in OPCIONES_MENU
