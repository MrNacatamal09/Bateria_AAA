"""
Conecta la interfaz de LU con los motores matemáticos oficiales.
Convierte entradas y gestiona el filtrado de propiedades ya calculadas.
Tema de clase: factorización LU, propiedades y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import (
    convertir_matriz,
    convertir_vector,
)

from utilidades.numeros import (
    convertir_a_fraccion,
)

from modulos.modulo_lu import (
    obtener_factorizacion,
    resolver_por_lu,
    verificar_propiedades,
    obtener_categorias_propiedades,
    filtrar_resultados_propiedades,
)


def procesar_factorizacion_lu(matriz_a):
    """Convierte A y devuelve su factorización LU completa."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    return obtener_factorizacion(
        matriz_a
    )


def procesar_sistema_lu(
    matriz_a,
    vector_b,
):
    """Convierte A y b y resuelve Ax=b mediante LU."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    vector_b = convertir_vector(
        vector_b
    )

    return resolver_por_lu(
        matriz_a,
        vector_b
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
    """Devuelve las categorías disponibles para el filtro de propiedades."""
    return obtener_categorias_propiedades()


def procesar_filtro_propiedades(
    resultado,
    texto_busqueda="",
    categoria="Todas",
):
    """Filtra un resultado ya calculado sin repetir operaciones matemáticas."""
    if resultado is None:
        raise ValueError(
            "Primero debe verificar las propiedades consolidadas."
        )

    return filtrar_resultados_propiedades(
        resultado,
        texto_busqueda,
        categoria,
    )