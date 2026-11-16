"""Valida entradas del Programa 8 antes de los métodos iterativos.

Tema: Jacobi y Gauss-Seidel para sistemas lineales.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import math

from modulos.modulo_iterativos import resolver_sistema_iterativo
from utilidades.estructuras_entrada import convertir_matriz, convertir_vector


def _convertir_flotante(valor, nombre):
    """Convierte un valor exacto sin admitir desbordamiento ni subdesbordamiento."""
    try:
        numero = float(valor)
    except (OverflowError, ValueError):
        raise ValueError(f"{nombre} excede el rango de punto flotante.") from None
    if not math.isfinite(numero) or (valor != 0 and numero == 0):
        raise ValueError(f"{nombre} no puede representarse con precisión numérica.")
    return numero


def _convertir_tolerancia(texto):
    """Exige una tolerancia decimal, finita y estrictamente positiva."""
    try:
        tolerancia = float(str(texto).strip().replace(",", "."))
    except ValueError:
        raise ValueError("La tolerancia ε debe ser un número decimal positivo.") from None
    if not math.isfinite(tolerancia) or tolerancia <= 0:
        raise ValueError("La tolerancia ε debe ser un número decimal positivo.")
    return tolerancia


def _convertir_maximo(texto):
    """Exige una cantidad entera positiva de iteraciones."""
    try:
        maximo = int(str(texto).strip())
    except ValueError:
        raise ValueError("El máximo de iteraciones debe ser un entero positivo.") from None
    if maximo <= 0:
        raise ValueError("El máximo de iteraciones debe ser un entero positivo.")
    return maximo


def procesar_metodos_iterativos(a_texto, b_texto, x0_texto,
                               tolerancia_texto, maximo_texto):
    """Convierte y valida A, b, x⁽⁰⁾ y los criterios de parada."""
    matriz_exacta = convertir_matriz(a_texto)
    orden = len(matriz_exacta)
    if any(len(fila) != orden for fila in matriz_exacta):
        raise ValueError("La matriz A debe ser cuadrada (n × n).")

    try:
        b_exacto = convertir_vector(b_texto)
    except ValueError as error:
        raise ValueError(f"Vector b: {error}") from None
    try:
        x0_exacto = convertir_vector(x0_texto)
    except ValueError as error:
        raise ValueError(f"Vector inicial x⁽⁰⁾: {error}") from None

    if len(b_exacto) != orden:
        raise ValueError(f"El vector b debe tener {orden} componentes.")
    if len(x0_exacto) != orden:
        raise ValueError(f"El vector inicial x⁽⁰⁾ debe tener {orden} componentes.")

    tolerancia = _convertir_tolerancia(tolerancia_texto)
    maximo = _convertir_maximo(maximo_texto)

    for i, fila in enumerate(matriz_exacta, start=1):
        for j, valor in enumerate(fila, start=1):
            _convertir_flotante(valor, f"A[{i},{j}]")
    for i, valor in enumerate(b_exacto, start=1):
        _convertir_flotante(valor, f"b[{i}]")
    for i, valor in enumerate(x0_exacto, start=1):
        _convertir_flotante(valor, f"x⁽⁰⁾[{i}]")

    return resolver_sistema_iterativo(
        matriz_exacta, b_exacto, x0_exacto, tolerancia, maximo
    )
