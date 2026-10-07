"""
Conecta la interfaz con las operaciones generales del Módulo III.
Convierte las entradas y coordina operaciones y propiedades de matrices.
Tema de clase: operaciones y propiedades generales de matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import convertir_matriz
from utilidades.numeros import convertir_a_fraccion

from modulos.modulo_matrices import (
    sumar,
    restar,
    multiplicar_por_escalar,
    producto_matricial,
    transponer,
)

from programas.programa_3.matrices import (
    multiplicar_matrices_con_procedimiento,
)

from programas.programa_3.propiedades_matrices_generales import (
    verificar_asociativa_multiplicacion,
    verificar_distributiva_izquierda,
    verificar_distributiva_derecha,
    verificar_escalar_producto,
    verificar_identidad_multiplicacion,
    verificar_transpuesta_doble,
    verificar_transpuesta_suma,
    verificar_transpuesta_escalar,
    verificar_transpuesta_producto,
)


def procesar_operacion_basica(
    operacion,
    matriz_a,
    matriz_b=None,
    escalar=None,
):
    """Procesa suma, resta o multiplicación por escalar desde la interfaz."""
    matriz_a = convertir_matriz(matriz_a)

    if operacion == "suma":
        if matriz_b is None:
            raise ValueError("Debe ingresar la matriz B.")

        matriz_b = convertir_matriz(matriz_b)
        return {
            "operacion": "suma",
            "matriz_a": matriz_a,
            "matriz_b": matriz_b,
            "resultado": sumar(matriz_a, matriz_b),
        }

    if operacion == "resta":
        if matriz_b is None:
            raise ValueError("Debe ingresar la matriz B.")

        matriz_b = convertir_matriz(matriz_b)
        return {
            "operacion": "resta",
            "matriz_a": matriz_a,
            "matriz_b": matriz_b,
            "resultado": restar(matriz_a, matriz_b),
        }

    if operacion == "escalar":
        if escalar is None:
            raise ValueError("Debe ingresar el escalar r.")

        valor_escalar = convertir_a_fraccion(escalar)
        return {
            "operacion": "escalar",
            "matriz_a": matriz_a,
            "escalar": valor_escalar,
            "resultado": multiplicar_por_escalar(
                matriz_a,
                valor_escalar,
            ),
        }

    raise ValueError("La operación seleccionada no es válida.")


def procesar_multiplicacion_matrices(matriz_a, matriz_b):
    """Valida dimensiones y calcula AB junto con su procedimiento."""
    matriz_a = convertir_matriz(matriz_a)
    matriz_b = convertir_matriz(matriz_b)

    columnas_a = len(matriz_a[0])
    filas_b = len(matriz_b)

    if columnas_a != filas_b:
        raise ValueError(
            "No se puede multiplicar: "
            f"Columnas de A [{columnas_a}] ≠ Filas de B [{filas_b}]"
        )

    procedimiento = multiplicar_matrices_con_procedimiento(
        matriz_a,
        matriz_b,
    )

    return {
        "operacion": "producto",
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "resultado": producto_matricial(matriz_a, matriz_b),
        "procedimiento": procedimiento,
    }


def procesar_transpuesta(matriz_a):
    """Convierte la entrada y calcula Aᵀ."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "operacion": "transpuesta",
        "matriz_a": matriz_a,
        "resultado": transponer(matriz_a),
    }


def procesar_propiedad_matrices(
    propiedad,
    matriz_a,
    matriz_b=None,
    matriz_c=None,
    escalar=None,
):
    """Ejecuta una de las nueve propiedades generales del Módulo III."""
    matriz_a = convertir_matriz(matriz_a)

    if propiedad == "asociativa":
        if matriz_b is None or matriz_c is None:
            raise ValueError("Esta propiedad necesita las matrices A, B y C.")

        return verificar_asociativa_multiplicacion(
            matriz_a,
            convertir_matriz(matriz_b),
            convertir_matriz(matriz_c),
        )

    if propiedad == "distributiva_izquierda":
        if matriz_b is None or matriz_c is None:
            raise ValueError("Esta propiedad necesita las matrices A, B y C.")

        return verificar_distributiva_izquierda(
            matriz_a,
            convertir_matriz(matriz_b),
            convertir_matriz(matriz_c),
        )

    if propiedad == "distributiva_derecha":
        if matriz_b is None or matriz_c is None:
            raise ValueError("Esta propiedad necesita las matrices A, B y C.")

        return verificar_distributiva_derecha(
            matriz_a,
            convertir_matriz(matriz_b),
            convertir_matriz(matriz_c),
        )

    if propiedad == "escalar_producto":
        if matriz_b is None:
            raise ValueError("Esta propiedad necesita las matrices A y B.")

        if escalar is None:
            raise ValueError("Debe ingresar el escalar r.")

        return verificar_escalar_producto(
            matriz_a,
            convertir_matriz(matriz_b),
            convertir_a_fraccion(escalar),
        )

    if propiedad == "identidad":
        return verificar_identidad_multiplicacion(matriz_a)

    if propiedad == "transpuesta_doble":
        return verificar_transpuesta_doble(matriz_a)

    if propiedad == "transpuesta_suma":
        if matriz_b is None:
            raise ValueError("Esta propiedad necesita las matrices A y B.")

        return verificar_transpuesta_suma(
            matriz_a,
            convertir_matriz(matriz_b),
        )

    if propiedad == "transpuesta_escalar":
        if escalar is None:
            raise ValueError("Debe ingresar el escalar r.")

        return verificar_transpuesta_escalar(
            matriz_a,
            convertir_a_fraccion(escalar),
        )

    if propiedad == "transpuesta_producto":
        if matriz_b is None:
            raise ValueError("Esta propiedad necesita las matrices A y B.")

        return verificar_transpuesta_producto(
            matriz_a,
            convertir_matriz(matriz_b),
        )

    raise ValueError("La propiedad general seleccionada no es válida.")
