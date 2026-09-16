from .vectores import (
    sumar_vectores,
    restar_vectores,
    multiplicar_vector_escalar
)

from .matrices import (
    sumar_matrices,
    restar_matrices,
    multiplicar_matriz_escalar,
    multiplicar_matrices
)

from .combinacion_lineal import evaluar_combinacion_lineal
from .ecuacion_matricial import resolver_ecuacion_matricial


# Ejecutamos una operación con vectores
def resolver_vectores(
    operacion,
    vector_1,
    vector_2=None,
    escalar=None
):

    if operacion == "suma":

        if vector_2 is None:
            raise ValueError(
                "Debe ingresar el segundo vector."
            )

        return {
            "operacion": "suma_vectores",
            "resultado": sumar_vectores(
                vector_1,
                vector_2
            )
        }

    if operacion == "resta":

        if vector_2 is None:
            raise ValueError(
                "Debe ingresar el segundo vector."
            )

        return {
            "operacion": "resta_vectores",
            "resultado": restar_vectores(
                vector_1,
                vector_2
            )
        }

    if operacion == "escalar":

        if escalar is None:
            raise ValueError(
                "Debe ingresar un escalar."
            )

        return {
            "operacion": "vector_por_escalar",
            "resultado": multiplicar_vector_escalar(
                vector_1,
                escalar
            )
        }

    raise ValueError(
        "La operación vectorial no es válida."
    )


# Ejecutamos una operación con matrices
def resolver_matrices(
    operacion,
    matriz_1,
    matriz_2=None,
    escalar=None
):

    if operacion == "suma":

        if matriz_2 is None:
            raise ValueError(
                "Debe ingresar la segunda matriz."
            )

        return {
            "operacion": "suma_matrices",
            "resultado": sumar_matrices(
                matriz_1,
                matriz_2
            )
        }

    if operacion == "resta":

        if matriz_2 is None:
            raise ValueError(
                "Debe ingresar la segunda matriz."
            )

        return {
            "operacion": "resta_matrices",
            "resultado": restar_matrices(
                matriz_1,
                matriz_2
            )
        }

    if operacion == "escalar":

        if escalar is None:
            raise ValueError(
                "Debe ingresar un escalar."
            )

        return {
            "operacion": "matriz_por_escalar",
            "resultado": multiplicar_matriz_escalar(
                matriz_1,
                escalar
            )
        }

    if operacion == "multiplicacion":

        if matriz_2 is None:
            raise ValueError(
                "Debe ingresar la segunda matriz."
            )

        return {
            "operacion": "multiplicacion_matrices",
            "resultado": multiplicar_matrices(
                matriz_1,
                matriz_2
            )
        }

    raise ValueError(
        "La operación matricial no es válida."
    )


# Evaluamos una combinación lineal
def resolver_combinacion_lineal(vectores, vector_b):

    resultado = evaluar_combinacion_lineal(
        vectores,
        vector_b
    )

    return {
        "operacion": "combinacion_lineal",
        "resultado": resultado
    }


# Resolvemos una ecuación matricial Ax = b
def resolver_ax_b(matriz_a, vector_b):

    resultado = resolver_ecuacion_matricial(
        matriz_a,
        vector_b
    )

    return {
        "operacion": "ecuacion_matricial",
        "resultado": resultado
    }