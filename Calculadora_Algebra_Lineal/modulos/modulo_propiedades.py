"""
Expone las funciones oficiales de la sección Propiedades.
Reutiliza el motor consolidado sin mezclar interfaz, validación y cálculo.
Tema de clase: propiedades matriciales y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from programas.programa_6.propiedades_consolidadas import (
    verificar_propiedades_consolidadas,
    obtener_categorias_propiedades as obtener_categorias_propiedades_motor,
    filtrar_propiedades as filtrar_propiedades_motor,
)

from teoremas.resumen_teoremas_propiedades import (
    obtener_teoremas_propiedades,
    obtener_descripcion_propiedades,
)


NOMBRE_MODULO = "Propiedades"
MODULO_DESARROLLADO = True


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
    """Devuelve el resumen teórico de la sección Propiedades."""
    return obtener_teoremas_propiedades()


def obtener_descripcion_modulo():
    """Devuelve una descripción breve de la sección Propiedades."""
    return obtener_descripcion_propiedades()


def obtener_logo_modulo():
    """Devuelve el logotipo textual de la sección Propiedades."""
    return """
============================================================
 PROPIEDADES
 Matrices, Transpuesta, Inversa y Determinantes
============================================================
"""


def mostrar_logo_modulo():
    """Muestra en consola el logotipo textual de la sección."""
    print(
        obtener_logo_modulo()
    )


def modulo_esta_desarrollado():
    """Indica si la sección Propiedades se encuentra habilitada."""
    return MODULO_DESARROLLADO