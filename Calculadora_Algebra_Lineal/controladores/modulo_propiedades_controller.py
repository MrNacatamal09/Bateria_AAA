"""
Conecta la interfaz de Propiedades con el motor consolidado oficial.
Convierte A, B, C y r antes de ejecutar cálculos o aplicar filtros.
Tema de clase: propiedades matriciales y reutilización de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import (
    convertir_matriz,
)

from utilidades.numeros import (
    convertir_a_fraccion,
)

from modulos.modulo_propiedades import (
    verificar_propiedades,
    obtener_categorias_propiedades,
    filtrar_resultados_propiedades,
)


def procesar_propiedades_consolidadas(
    matriz_a,
    matriz_b,
    matriz_c,
    escalar,
):
    """Convierte A, B, C y r y ejecuta el verificador consolidado."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    matriz_b = convertir_matriz(
        matriz_b
    )

    matriz_c = convertir_matriz(
        matriz_c
    )

    escalar = convertir_a_fraccion(
        escalar
    )

    return verificar_propiedades(
        matriz_a,
        matriz_b,
        matriz_c,
        escalar,
    )


def procesar_categorias_propiedades():
    """Devuelve las categorías disponibles para el filtro."""
    return obtener_categorias_propiedades()


def procesar_filtro_propiedades(
    resultado,
    texto_busqueda="",
    categoria="Todas",
):
    """Filtra resultados ya calculados sin repetir operaciones matemáticas."""
    if resultado is None:
        raise ValueError(
            "Primero debe verificar las propiedades consolidadas."
        )

    return filtrar_resultados_propiedades(
        resultado,
        texto_busqueda,
        categoria,
    )