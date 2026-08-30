from copy import deepcopy

from .gauss import gauss
from .gauss_jordan import gauss_jordan
from .solucion import obtener_solucion, formatear_solucion
from .verificacion import verificar_solucion


# Revisamos que la matriz tenga una estructura válida
def validar_matriz(matriz, numero_variables):

    if not matriz:
        raise ValueError("La matriz no puede estar vacía.")

    if numero_variables <= 0:
        raise ValueError(
            "Debe existir al menos una variable."
        )

    columnas_esperadas = numero_variables + 1

    for i in range(len(matriz)):

        if len(matriz[i]) != columnas_esperadas:
            raise ValueError(
                f"La fila {i + 1} debe tener "
                f"{columnas_esperadas} valores."
            )


# Resolvemos el sistema con el método elegido
def resolver_sistema(
    matriz_original,
    numero_variables,
    metodo="gauss"
):

    validar_matriz(
        matriz_original,
        numero_variables
    )

    # Conservamos una copia para verificar la solución
    matriz_original = deepcopy(matriz_original)

    metodo = str(metodo).lower().strip()

    # Aplicamos el método seleccionado
    if metodo == "gauss":

        resultado_metodo = gauss(
            matriz_original
        )

        matriz_resultado = resultado_metodo[
            "matriz_escalonada"
        ]

    elif metodo == "gauss_jordan":

        resultado_metodo = gauss_jordan(
            matriz_original
        )

        matriz_resultado = resultado_metodo[
            "matriz_reducida"
        ]

    else:
        raise ValueError(
            "El método debe ser 'gauss' "
            "o 'gauss_jordan'."
        )

    # Obtenemos la solución y clasificación
    solucion = obtener_solucion(
        matriz_resultado,
        numero_variables
    )

    clasificacion = solucion["clasificacion"]

    solucion_formateada = formatear_solucion(
        solucion,
        numero_variables
    )

    # Verificamos la solución en el sistema original
    verificacion = verificar_solucion(
        matriz_original,
        solucion,
        numero_variables
    )

    return {
        "metodo": metodo,
        "matriz_original": matriz_original,
        "matriz_resultado": matriz_resultado,
        "historial": resultado_metodo["historial"],
        "posiciones_pivote": resultado_metodo[
            "posiciones_pivote"
        ],
        "clasificacion": clasificacion,
        "solucion": solucion,
        "solucion_formateada": solucion_formateada,
        "verificacion": verificacion
    }