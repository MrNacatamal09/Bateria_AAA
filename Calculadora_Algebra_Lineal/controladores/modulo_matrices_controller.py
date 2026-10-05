"""
Conecta la interfaz con las funciones oficiales del Programa 5.
Convierte los datos de entrada y coordina operaciones, determinantes e inversas.
Tema de clase: Módulo III de Álgebra de Matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import (
    convertir_matriz
)

from utilidades.numeros import (
    convertir_a_fraccion
)

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
    verificar_propiedad_6
)

from programas.programa_3.matrices import (
    multiplicar_matrices_con_procedimiento
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
    verificar_transpuesta_producto
)


def procesar_operacion_basica(
    operacion,
    matriz_a,
    matriz_b=None,
    escalar=None
):
    """Procesa suma, resta o multiplicación por escalar desde la interfaz."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    if operacion == "suma":
        return _procesar_suma(
            matriz_a,
            matriz_b
        )

    if operacion == "resta":
        return _procesar_resta(
            matriz_a,
            matriz_b
        )

    if operacion == "escalar":
        return _procesar_escalar(
            matriz_a,
            escalar
        )

    raise ValueError(
        "La operación básica seleccionada no es válida."
    )


def _procesar_suma(matriz_a, matriz_b):
    """Convierte B y devuelve los datos de la operación A + B."""
    if matriz_b is None:
        raise ValueError(
            "Debe ingresar la matriz B."
        )

    matriz_b = convertir_matriz(
        matriz_b
    )

    return {
        "operacion": "suma",
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "resultado": sumar(
            matriz_a,
            matriz_b
        )
    }


def _procesar_resta(matriz_a, matriz_b):
    """Convierte B y devuelve los datos de la operación A - B."""
    if matriz_b is None:
        raise ValueError(
            "Debe ingresar la matriz B."
        )

    matriz_b = convertir_matriz(
        matriz_b
    )

    return {
        "operacion": "resta",
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "resultado": restar(
            matriz_a,
            matriz_b
        )
    }


def _procesar_escalar(matriz_a, escalar):
    """Convierte el escalar y devuelve los datos de la operación cA."""
    if escalar is None:
        raise ValueError(
            "Debe ingresar un escalar."
        )

    escalar = convertir_a_fraccion(
        escalar
    )

    return {
        "operacion": "escalar",
        "matriz_a": matriz_a,
        "escalar": escalar,
        "resultado": multiplicar_por_escalar(
            matriz_a,
            escalar
        )
    }


def procesar_multiplicacion_matrices(
    matriz_a,
    matriz_b
):
    """Calcula AB y conserva el procedimiento de la regla fila-columna."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    matriz_b = convertir_matriz(
        matriz_b
    )

    columnas_a = len(
        matriz_a[0]
    )

    filas_b = len(
        matriz_b
    )

    if columnas_a != filas_b:
        raise ValueError(
            "No se puede multiplicar: "
            f"Columnas de A [{columnas_a}] ≠ "
            f"Filas de B [{filas_b}]"
        )

    procedimiento = multiplicar_matrices_con_procedimiento(
        matriz_a,
        matriz_b
    )

    return {
        "operacion": "multiplicacion",
        "matriz_a": matriz_a,
        "matriz_b": matriz_b,
        "resultado": producto_matricial(
            matriz_a,
            matriz_b
        ),
        "procedimiento": procedimiento[
            "procedimiento"
        ]
    }


def procesar_transpuesta(matriz_a):
    """Convierte A y devuelve su matriz transpuesta."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    return {
        "operacion": "transpuesta",
        "matriz_a": matriz_a,
        "resultado": transponer(
            matriz_a
        )
    }


def procesar_determinante_programa_5(matriz_a):
    """Ejecuta cofactores, Sarrus cuando aplica y reducción triangular."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    metodos = resolver_determinante(
        matriz_a
    )

    diagnostico = diagnosticar_invertibilidad(
        matriz_a
    )

    return {
        "operacion": "determinante",
        "matriz_a": matriz_a,
        "metodos": metodos,
        "diagnostico": diagnostico
    }


def procesar_inversa(matriz_a):
    """Mantiene compatibilidad con la interfaz anterior de Gauss-Jordan."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    return {
        "operacion": "inversa",
        "resultado": inversa_gauss_jordan(
            matriz_a
        )
    }


def procesar_inversa_gauss_jordan_programa_5(
    matriz_a
):
    """Calcula A^-1 por Gauss-Jordan y añade el diagnóstico de invertibilidad."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    resultado = inversa_gauss_jordan(
        matriz_a
    )

    diagnostico = diagnosticar_invertibilidad(
        matriz_a
    )

    return {
        "operacion": "inversa_gauss_jordan",
        "matriz_a": matriz_a,
        "resultado": resultado,
        "diagnostico": diagnostico
    }


def procesar_inversa_adjunta_programa_5(
    matriz_a
):
    """Calcula A^-1 por adjunta y compara el resultado con Gauss-Jordan."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    resultado = inversa_por_adjunta(
        matriz_a
    )

    comparacion = comparar_inversas(
        matriz_a
    )

    diagnostico = diagnosticar_invertibilidad(
        matriz_a
    )

    return {
        "operacion": "inversa_adjunta",
        "matriz_a": matriz_a,
        "resultado": resultado,
        "comparacion": comparacion,
        "diagnostico": diagnostico
    }


def _convertir_fila_usuario(
    fila,
    orden,
    nombre
):
    """Convierte una fila escrita desde 1 a su índice interno desde 0."""
    try:
        fila = int(
            fila
        )
    except (TypeError, ValueError):
        raise ValueError(
            f"{nombre} debe ser un número entero."
        )

    if fila < 1 or fila > orden:
        raise ValueError(
            f"{nombre} debe estar entre 1 y {orden}."
        )

    return fila - 1


def _procesar_propiedad_5(
    matriz_a,
    fila_1,
    fila_2,
    escalar_reemplazo,
    fila_escalar,
    escalar_fila
):
    """Convierte filas y escalares para verificar las operaciones elementales."""
    orden = len(
        matriz_a
    )

    fila_1 = _convertir_fila_usuario(
        fila_1,
        orden,
        "La primera fila"
    )

    fila_2 = _convertir_fila_usuario(
        fila_2,
        orden,
        "La segunda fila"
    )

    fila_escalar = _convertir_fila_usuario(
        fila_escalar,
        orden,
        "La fila a escalar"
    )

    return verificar_propiedad_5(
        matriz_a,
        fila_1,
        fila_2,
        convertir_a_fraccion(
            escalar_reemplazo
        ),
        fila_escalar,
        convertir_a_fraccion(
            escalar_fila
        )
    )


def procesar_propiedad_programa_5(
    numero_propiedad,
    matriz_a,
    matriz_b=None,
    fila_1=None,
    fila_2=None,
    escalar_reemplazo=None,
    fila_escalar=None,
    escalar_fila=None
):
    """Ejecuta una de las seis propiedades requeridas por la opción 9."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    if numero_propiedad == 1:
        return verificar_propiedad_1(
            matriz_a
        )

    if numero_propiedad == 2:
        return _procesar_propiedad_2(
            matriz_a,
            matriz_b
        )

    if numero_propiedad == 3:
        return verificar_propiedad_3(
            matriz_a
        )

    if numero_propiedad == 4:
        return verificar_propiedad_4(
            matriz_a
        )

    if numero_propiedad == 5:
        return _procesar_propiedad_5(
            matriz_a,
            fila_1,
            fila_2,
            escalar_reemplazo,
            fila_escalar,
            escalar_fila
        )

    if numero_propiedad == 6:
        return verificar_propiedad_6(
            matriz_a
        )

    raise ValueError(
        "La propiedad debe estar entre 1 y 6."
    )


def _procesar_propiedad_2(
    matriz_a,
    matriz_b
):
    """Convierte B y ejecuta la propiedad de la inversa del producto."""
    if matriz_b is None:
        raise ValueError(
            "La propiedad 2 requiere las matrices A y B."
        )

    matriz_b = convertir_matriz(
        matriz_b
    )

    return verificar_propiedad_2(
        matriz_a,
        matriz_b
    )


def procesar_propiedad_matrices(
    propiedad,
    matriz_a,
    matriz_b=None,
    matriz_c=None,
    escalar=None
):
    """Mantiene temporalmente las propiedades usadas por la interfaz anterior."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    if propiedad == "asociativa":
        return _propiedad_tres_matrices(
            verificar_asociativa_multiplicacion,
            matriz_a,
            matriz_b,
            matriz_c
        )

    if propiedad == "distributiva_izquierda":
        return _propiedad_tres_matrices(
            verificar_distributiva_izquierda,
            matriz_a,
            matriz_b,
            matriz_c
        )

    if propiedad == "distributiva_derecha":
        return _propiedad_tres_matrices(
            verificar_distributiva_derecha,
            matriz_a,
            matriz_b,
            matriz_c
        )

    if propiedad == "escalar_producto":
        return _propiedad_dos_matrices_escalar(
            verificar_escalar_producto,
            matriz_a,
            matriz_b,
            escalar
        )

    if propiedad == "identidad":
        return verificar_identidad_multiplicacion(
            matriz_a
        )

    if propiedad == "transpuesta_doble":
        return verificar_transpuesta_doble(
            matriz_a
        )

    if propiedad == "transpuesta_suma":
        return _propiedad_dos_matrices(
            verificar_transpuesta_suma,
            matriz_a,
            matriz_b
        )

    if propiedad == "transpuesta_escalar":
        return _propiedad_una_matriz_escalar(
            verificar_transpuesta_escalar,
            matriz_a,
            escalar
        )

    if propiedad == "transpuesta_producto":
        return _propiedad_dos_matrices(
            verificar_transpuesta_producto,
            matriz_a,
            matriz_b
        )

    raise ValueError(
        "La propiedad seleccionada no es válida."
    )


def _propiedad_tres_matrices(
    funcion,
    matriz_a,
    matriz_b,
    matriz_c
):
    """Convierte B y C antes de evaluar una propiedad con tres matrices."""
    if matriz_b is None or matriz_c is None:
        raise ValueError(
            "Esta propiedad requiere las matrices A, B y C."
        )

    return funcion(
        matriz_a,
        convertir_matriz(
            matriz_b
        ),
        convertir_matriz(
            matriz_c
        )
    )


def _propiedad_dos_matrices(
    funcion,
    matriz_a,
    matriz_b
):
    """Convierte B antes de evaluar una propiedad con dos matrices."""
    if matriz_b is None:
        raise ValueError(
            "Esta propiedad requiere las matrices A y B."
        )

    return funcion(
        matriz_a,
        convertir_matriz(
            matriz_b
        )
    )


def _propiedad_una_matriz_escalar(
    funcion,
    matriz_a,
    escalar
):
    """Convierte el escalar antes de evaluar una propiedad sobre A."""
    if escalar is None:
        raise ValueError(
            "Esta propiedad requiere un escalar."
        )

    return funcion(
        matriz_a,
        convertir_a_fraccion(
            escalar
        )
    )


def _propiedad_dos_matrices_escalar(
    funcion,
    matriz_a,
    matriz_b,
    escalar
):
    """Convierte B y el escalar para una propiedad que utiliza ambos."""
    if matriz_b is None:
        raise ValueError(
            "Esta propiedad requiere las matrices A y B."
        )

    if escalar is None:
        raise ValueError(
            "Esta propiedad requiere un escalar."
        )

    return funcion(
        matriz_a,
        convertir_matriz(
            matriz_b
        ),
        convertir_a_fraccion(
            escalar
        )
    )