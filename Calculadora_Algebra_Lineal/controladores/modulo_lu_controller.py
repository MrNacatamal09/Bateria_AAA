"""
Conecta la interfaz de LU con los motores matemáticos oficiales.
Convierte matrices, vectores y escalares antes de ejecutar cada operación.
Tema de clase: factorización LU y consolidación de propiedades.
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
)


def procesar_factorizacion_lu(matriz_a):
    """Convierte A y devuelve su factorización LU completa."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    return obtener_factorizacion(
        matriz_a
    )


def procesar_sistema_lu(matriz_a, vector_b):
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
