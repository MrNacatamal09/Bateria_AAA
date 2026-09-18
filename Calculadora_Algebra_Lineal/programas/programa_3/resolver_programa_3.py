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

from .combinacion_lineal import (
    evaluar_combinacion_lineal
)

from .ecuacion_matricial import (
    resolver_ecuacion_matricial
)


# Sumamos una cantidad variable de vectores
def sumar_varios_vectores(
    vectores
):

    if not vectores:

        raise ValueError(
            "Debe ingresar vectores para realizar la suma."
        )

    if len(vectores) < 2:

        raise ValueError(
            "La suma debe contener al menos dos vectores."
        )

    resultado = list(
        vectores[0]
    )

    for i in range(
        1,
        len(vectores)
    ):

        resultado = sumar_vectores(
            resultado,
            vectores[i]
        )

    return resultado


# Restamos una cantidad variable de vectores
def restar_varios_vectores(
    vectores
):

    if not vectores:

        raise ValueError(
            "Debe ingresar vectores para realizar la resta."
        )

    if len(vectores) < 2:

        raise ValueError(
            "La resta debe contener al menos dos vectores."
        )

    # La resta se realiza de izquierda a derecha
    resultado = list(
        vectores[0]
    )

    for i in range(
        1,
        len(vectores)
    ):

        resultado = restar_vectores(
            resultado,
            vectores[i]
        )

    return resultado


# Ejecutamos una operación con vectores
def resolver_vectores(
    operacion,
    vector_1=None,
    vector_2=None,
    escalar=None,
    vectores=None
):

    # Suma
    if operacion == "suma":

        # Suma de una cantidad variable
        if vectores is not None:

            return {
                "operacion": "suma_vectores",
                "cantidad_vectores": len(vectores),
                "resultado": sumar_varios_vectores(
                    vectores
                )
            }

        # Compatibilidad con dos vectores
        if vector_1 is None:

            raise ValueError(
                "Debe ingresar el primer vector."
            )

        if vector_2 is None:

            raise ValueError(
                "Debe ingresar el segundo vector."
            )

        return {
            "operacion": "suma_vectores",
            "cantidad_vectores": 2,
            "resultado": sumar_vectores(
                vector_1,
                vector_2
            )
        }

    # Resta
    if operacion == "resta":

        # Resta de una cantidad variable
        if vectores is not None:

            return {
                "operacion": "resta_vectores",
                "cantidad_vectores": len(vectores),
                "resultado": restar_varios_vectores(
                    vectores
                )
            }

        # Compatibilidad con dos vectores
        if vector_1 is None:

            raise ValueError(
                "Debe ingresar el primer vector."
            )

        if vector_2 is None:

            raise ValueError(
                "Debe ingresar el segundo vector."
            )

        return {
            "operacion": "resta_vectores",
            "cantidad_vectores": 2,
            "resultado": restar_vectores(
                vector_1,
                vector_2
            )
        }

    # Multiplicación por escalar
    if operacion == "escalar":

        if vector_1 is None:

            raise ValueError(
                "Debe ingresar el vector."
            )

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
def resolver_combinacion_lineal(
    vectores,
    vector_b
):

    resultado = evaluar_combinacion_lineal(
        vectores,
        vector_b
    )

    return {
        "operacion": "combinacion_lineal",
        "resultado": resultado
    }


# Resolvemos una ecuación matricial Ax = b
def resolver_ax_b(
    matriz_a,
    vector_b
):

    resultado = resolver_ecuacion_matricial(
        matriz_a,
        vector_b
    )

    return {
        "operacion": "ecuacion_matricial",
        "resultado": resultado
    }