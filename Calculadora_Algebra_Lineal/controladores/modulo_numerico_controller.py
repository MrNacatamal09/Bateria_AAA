"""Conecta los formularios numéricos con el motor del Programa 7.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from modulos.modulo_numerico import (
    biseccion, puntos_grafica, notacion_posicional,
    calcular_errores, propagacion_error, ejemplos_punto_flotante,
)


def procesar_biseccion(expresion, a, b, tolerancia, maximo):
    """Devuelve tabla, aproximación y criterio de parada."""
    return biseccion(expresion, a, b, tolerancia, maximo)


def procesar_grafica(expresion, minimo, maximo):
    """Devuelve puntos evaluados de forma controlada."""
    return puntos_grafica(expresion, minimo, maximo)


def procesar_posicional(texto, base):
    """Devuelve las dos descomposiciones del entero."""
    return notacion_posicional(texto, base)


def procesar_errores(verdadero, aproximado, x, delta):
    """Devuelve errores de medición y propagación por derivada."""
    return calcular_errores(verdadero, aproximado), propagacion_error(x, delta)
