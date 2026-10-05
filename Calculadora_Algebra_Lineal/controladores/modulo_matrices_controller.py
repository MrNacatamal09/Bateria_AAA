"""
Conecta la interfaz con las funciones oficiales del Programa 5.
Convierte los datos de entrada y coordina operaciones, determinantes e inversas.
Tema de clase: Módulo III de Álgebra de Matrices.
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
    resolver_determinante,
    inversa_gauss_jordan,
    inversa_por_adjunta,
    comparar_inversas,
    diagnosticar_invertibilidad,
    verificar_propiedad_1,
    verificar_propiedad_2,
    verificar_propiedad_3,
    verificar_propiedad_4,
    verificar_propiedad_5,
    verificar_propiedad_6,
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
            raise ValueError("Debe ingresar un escalar.")

        escalar = convertir_a_fraccion(escalar)
        return {
            "operacion": "escalar",
            "matriz_a": matriz_a,
            "escalar": escalar,
            "resultado": multiplicar_por_escalar(matriz_a, escalar),
        }

    raise ValueError("La operación básica seleccionada no es válida.")


def procesar_multiplicacion_matrices(matriz_a, matriz_b):
    """Calcula AB y conserva el procedimiento de la regla fila-columna."""
    matriz_a = convertir_matriz(matriz_a)
    matriz_b = convertir_matriz(matriz_b)

    columnas_a = len(matriz_a[0])
    filas_b = len(matriz_b)

    if columnas_a != filas_b:
        raise ValueError(
            f"No se puede multiplicar: Columnas de A [{columnas_a}] "
            f"≠ Filas de B [{filas_b}]"
        )

    procedimiento = multiplicar_matrices_con_procedimiento(
        matriz_a,
        matriz_b,
    )

    return {
        "operacion": "multiplicacion",
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "resultado": procedimiento["resultado"],
        "procedimiento": procedimiento["procedimiento"],
    }


def procesar_transpuesta(matriz_a):
    """Convierte la entrada y calcula Aᵀ."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "operacion": "transpuesta",
        "matriz_a": matriz_a,
        "resultado": transponer(matriz_a),
    }


def procesar_determinante_programa_5(matriz_a):
    """Calcula los métodos de det(A) y su diagnóstico de invertibilidad."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "matriz_a": matriz_a,
        "metodos": resolver_determinante(matriz_a),
        "diagnostico": diagnosticar_invertibilidad(matriz_a),
    }


def procesar_inversa(matriz_a):
    """Mantiene compatibilidad con la inversa usada antes del Programa 5."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "matriz_a": matriz_a,
        "resultado": inversa_gauss_jordan(matriz_a),
    }


def procesar_inversa_gauss_jordan_programa_5(matriz_a):
    """Calcula A⁻¹ por Gauss-Jordan y agrega el diagnóstico."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "matriz_a": matriz_a,
        "resultado": inversa_gauss_jordan(matriz_a),
        "diagnostico": diagnosticar_invertibilidad(matriz_a),
    }


def procesar_inversa_adjunta_programa_5(matriz_a):
    """Calcula A⁻¹ por adjunta, compara métodos y agrega diagnóstico."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "matriz_a": matriz_a,
        "resultado": inversa_por_adjunta(matriz_a),
        "comparacion": comparar_inversas(matriz_a),
        "diagnostico": diagnosticar_invertibilidad(matriz_a),
    }


def _convertir_fila_usuario(valor, nombre):
    """Convierte una fila escrita desde 1 a un índice interno desde 0."""
    try:
        fila = int(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nombre} debe ser un número entero.")

    if fila <= 0:
        raise ValueError(f"{nombre} debe ser mayor que cero.")

    return fila - 1


def _procesar_propiedad_5(
    matriz_a,
    fila_1,
    fila_2,
    escalar_reemplazo,
    fila_escalar,
    escalar_fila,
):
    """Convierte los datos elegidos por el usuario para la propiedad 5."""
    fila_1 = _convertir_fila_usuario(fila_1, "Fila 1")
    fila_2 = _convertir_fila_usuario(fila_2, "Fila 2")
    fila_escalar = _convertir_fila_usuario(
        fila_escalar,
        "Fila a escalar",
    )

    escalar_reemplazo = convertir_a_fraccion(escalar_reemplazo)
    escalar_fila = convertir_a_fraccion(escalar_fila)

    return verificar_propiedad_5(
        matriz_a,
        fila_1,
        fila_2,
        escalar_reemplazo,
        fila_escalar,
        escalar_fila,
    )


def procesar_propiedad_programa_5(
    numero,
    matriz_a,
    matriz_b=None,
    fila_1="1",
    fila_2="2",
    escalar_reemplazo="-3",
    fila_escalar="1",
    escalar_fila="3",
):
    """Ejecuta una de las seis propiedades oficiales del Programa 5."""
    matriz_a = convertir_matriz(matriz_a)

    if numero == 1:
        return verificar_propiedad_1(matriz_a)

    if numero == 2:
        if matriz_b is None:
            raise ValueError("La propiedad 2 necesita las matrices A y B.")

        matriz_b = convertir_matriz(matriz_b)
        return verificar_propiedad_2(matriz_a, matriz_b)

    if numero == 3:
        return verificar_propiedad_3(matriz_a)

    if numero == 4:
        return verificar_propiedad_4(matriz_a)

    if numero == 5:
        return _procesar_propiedad_5(
            matriz_a,
            fila_1,
            fila_2,
            escalar_reemplazo,
            fila_escalar,
            escalar_fila,
        )

    if numero == 6:
        return verificar_propiedad_6(matriz_a)

    raise ValueError("La propiedad seleccionada debe estar entre 1 y 6.")


def procesar_propiedad_matrices(
    propiedad,
    matriz_a,
    matriz_b=None,
    matriz_c=None,
    escalar=None,
):
    """Ejecuta una de las nueve propiedades generales heredadas del Módulo 3."""
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
