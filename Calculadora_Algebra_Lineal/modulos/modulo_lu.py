"""
Expone las funciones oficiales del módulo de Factorización LU.
Reutiliza motores matemáticos, propiedades y filtros sin mezclar interfaz y cálculo.
Tema de clase: descomposición A = LU y resolución de sistemas Ax = b.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from programas.programa_6.factorizacion_lu import (
    factorizar_lu,
    resolver_sistema_lu,
)

from programas.programa_6.propiedades_consolidadas import (
    verificar_propiedades_consolidadas,
    obtener_categorias_propiedades as obtener_categorias_propiedades_motor,
    filtrar_propiedades as filtrar_propiedades_motor,
)

from teoremas.resumen_teoremas_lu import (
    obtener_teoremas_lu,
)


NOMBRE_MODULO = "Factorización LU"
MODULO_DESARROLLADO = True

OPCIONES_MENU = {
    0: "Ver Teoremas Clave del Módulo",
    1: "Factorización A = LU",
    2: "Resolver Ax = b mediante LU",
    3: "Propiedades Consolidadas",
}


def obtener_factorizacion(matriz_a):
    """Obtiene L y U junto con el procedimiento de reducción."""
    return factorizar_lu(
        matriz_a
    )


def resolver_por_lu(matriz_a, vector_b):
    """Resuelve Ax=b mediante A=LU, Ly=b y Ux=y."""
    return resolver_sistema_lu(
        matriz_a,
        vector_b
    )


def verificar_propiedades(
    matriz_a,
    matriz_b,
    matriz_c,
    escalar,
):
    """Evalúa el conjunto consolidado de propiedades matriciales."""
    return verificar_propiedades_consolidadas(
        matriz_a,
        matriz_b,
        matriz_c,
        escalar,
    )


def obtener_categorias_propiedades():
    """Devuelve las categorías disponibles para filtrar propiedades."""
    return obtener_categorias_propiedades_motor()


def filtrar_resultados_propiedades(
    resultado,
    texto_busqueda="",
    categoria="Todas",
):
    """Filtra propiedades ya calculadas sin volver a ejecutar operaciones."""
    return filtrar_propiedades_motor(
        resultado,
        texto_busqueda,
        categoria,
    )


def obtener_teoremas_clave():
    """Devuelve el resumen teórico del módulo LU."""
    return obtener_teoremas_lu()


def obtener_logo_modulo():
    """Devuelve el logotipo textual del módulo de Factorización LU."""
    return """
============================================================
 MÓDULO V - FACTORIZACIÓN LU
 Descomposición A = LU y Resolución de Sistemas
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
        "Este módulo descompone A en L·U, conserva los multiplicadores "
        "de eliminación, resuelve Ax=b y consolida propiedades matriciales."
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