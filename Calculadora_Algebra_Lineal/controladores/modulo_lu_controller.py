"""
Conecta la interfaz de LU con los motores matemáticos oficiales.
Convierte matrices y vectores antes de ejecutar cada operación.
Tema de clase: factorización LU y resolución de sistemas Ax = b.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import (
    convertir_matriz,
    convertir_vector,
)

from modulos.modulo_lu import (
    obtener_factorizacion,
    resolver_por_lu,
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
        vector_b,
    )