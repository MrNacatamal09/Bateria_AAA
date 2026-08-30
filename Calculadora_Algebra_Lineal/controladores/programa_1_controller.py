from utilidades.matriz_entrada import construir_matriz_aumentada
from programas.programa_1.resolver_sistema import resolver_sistema


# Preparamos los datos y enviamos el sistema al motor
def procesar_sistema(
    datos,
    numero_ecuaciones,
    numero_variables,
    metodo
):

    # Convertimos los datos ingresados a una matriz válida
    matriz = construir_matriz_aumentada(
        datos,
        numero_ecuaciones,
        numero_variables
    )

    # Enviamos la matriz al método seleccionado
    resultado = resolver_sistema(
        matriz,
        numero_variables,
        metodo
    )

    return resultado