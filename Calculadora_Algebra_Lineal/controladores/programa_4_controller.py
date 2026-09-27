from utilidades.estructuras_entrada import (
    convertir_vector
)

from programas.programa_4.resolver_programa_4 import (
    resolver_programa_4
)


# ==========================================================
# PROGRAMA 4
# CONTROLADOR DE INDEPENDENCIA LINEAL
# ==========================================================

def procesar_independencia_lineal(
    vectores
):

    # ======================================================
    # VALIDACIÓN BÁSICA
    # ======================================================

    if not vectores:

        raise ValueError(
            "Debe ingresar al menos un vector."
        )

    # ======================================================
    # CONVERSIÓN DE LOS VECTORES
    #
    # Todos los valores ingresados desde la interfaz
    # se convierten mediante las utilidades existentes.
    # Esto permite trabajar con enteros, decimales
    # y fracciones exactas.
    # ======================================================

    vectores_convertidos = []

    for vector in vectores:

        vector_convertido = convertir_vector(
            vector
        )

        vectores_convertidos.append(
            vector_convertido
        )

    # ======================================================
    # MOTOR DEL PROGRAMA 4
    # ======================================================

    return resolver_programa_4(
        vectores_convertidos
    )