"""
Conecta la interfaz del Módulo IV con determinantes, inversas y propiedades.
Convierte los datos de entrada antes de enviarlos a los motores matemáticos.
Tema de clase: determinantes, matriz inversa y propiedades asociadas.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.estructuras_entrada import convertir_matriz
from utilidades.numeros import convertir_a_fraccion

from modulos.modulo_determinantes import (
    resolver_determinante,
    resolver_cramer,
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


def procesar_determinante_programa_5(matriz_a):
    """Calcula los métodos de det(A) y su diagnóstico de invertibilidad."""
    matriz_a = convertir_matriz(matriz_a)

    return {
        "matriz_a": matriz_a,
        "metodos": resolver_determinante(matriz_a),
        "diagnostico": diagnosticar_invertibilidad(matriz_a),
    }


def procesar_cramer(matriz_a, vector_b):
    """Convierte A y b y resuelve el sistema mediante Cramer."""
    matriz_a = convertir_matriz(
        matriz_a
    )

    vector_b = [
        convertir_a_fraccion(
            valor
        )
        for valor in vector_b
    ]

    return resolver_cramer(
        matriz_a,
        vector_b,
    )


def procesar_inversa(matriz_a):
    """Mantiene compatibilidad con llamadas anteriores a la inversa."""
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
    """Ejecuta una de las seis propiedades del verificador."""
    matriz_a = convertir_matriz(matriz_a)

    if numero == 1:
        return verificar_propiedad_1(matriz_a)

    if numero == 2:
        if matriz_b is None:
            raise ValueError("La propiedad 2 necesita las matrices A y B.")

        return verificar_propiedad_2(
            matriz_a,
            convertir_matriz(matriz_b),
        )

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
