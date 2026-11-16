"""Expone el Programa 8 y contrasta sus resultados con Gauss-Jordan.

Tema: métodos iterativos de Jacobi y Gauss-Seidel.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from fractions import Fraction

from modulos.modulo_sistemas import reducir_por_gauss_jordan
from programas.programa_8.metodos_iterativos import resolver_metodos
from teoremas.resumen_teoremas_iterativos import obtener_teoremas_iterativos


def obtener_logo_modulo():
    """Devuelve el encabezado textual del Módulo 7."""
    return ("\n============================================================\n"
            " MÓDULO 7 - MÉTODOS ITERATIVOS · PROGRAMA 8\n"
            " Jacobi y Gauss-Seidel\n"
            "============================================================\n")


def obtener_teoremas_clave():
    """Expone el resumen teórico del módulo."""
    return obtener_teoremas_iterativos()


def _norma_diferencia(primero, segundo):
    """Mide la diferencia máxima entre dos soluciones aproximadas."""
    return max(abs(a - b) for a, b in zip(primero, segundo))


def _comparar_metodos(jacobi, gauss_seidel):
    """Resume convergencia, iteraciones y diferencia entre aproximaciones."""
    solucion_j = jacobi["solucion"]
    solucion_gs = gauss_seidel["solucion"]
    diferencia = (_norma_diferencia(solucion_j, solucion_gs)
                  if solucion_j is not None and solucion_gs is not None else None)
    if jacobi["convergio"] and gauss_seidel["convergio"]:
        pasos_j = jacobi["numero_iteraciones"]
        pasos_gs = gauss_seidel["numero_iteraciones"]
        if pasos_j < pasos_gs:
            menor = "Jacobi"
        elif pasos_gs < pasos_j:
            menor = "Gauss-Seidel"
        else:
            menor = "Empate"
    elif jacobi["convergio"]:
        menor = "Solo Jacobi alcanzó la tolerancia"
    elif gauss_seidel["convergio"]:
        menor = "Solo Gauss-Seidel alcanzó la tolerancia"
    else:
        menor = "Ninguno alcanzó la tolerancia"
    return {"metodo_menos_iteraciones": menor, "diferencia": diferencia}


def _solucion_gauss_jordan(matriz, vector):
    """Obtiene la referencia exacta solo si [A|b] reduce a [I|x]."""
    orden = len(matriz)
    aumentada = [fila.copy() + [vector[i]]
                 for i, fila in enumerate(matriz)]
    reducida = reducir_por_gauss_jordan(aumentada)["matriz_reducida"]
    identidad = all(
        reducida[i][j] == (Fraction(1) if i == j else Fraction(0))
        for i in range(orden) for j in range(orden)
    )
    if not identidad:
        return None
    try:
        return [float(reducida[i][-1]) for i in range(orden)]
    except OverflowError:
        return None


def _validar_referencia(matriz, vector, jacobi, gauss_seidel):
    """Compara cada método convergido con el Gauss-Jordan existente."""
    referencia = {
        "solucion": None,
        "estado": "La referencia se calcula cuando al menos un método converge.",
        "diferencia_jacobi": None,
        "diferencia_gauss_seidel": None,
    }
    if not (jacobi["convergio"] or gauss_seidel["convergio"]):
        return referencia
    solucion = _solucion_gauss_jordan(matriz, vector)
    if solucion is None:
        referencia["estado"] = (
            "Gauss-Jordan no encontró una solución única representable."
        )
        return referencia
    referencia.update(
        solucion=solucion,
        estado="Solución única de referencia obtenida con Gauss-Jordan.",
        diferencia_jacobi=(
            _norma_diferencia(jacobi["solucion"], solucion)
            if jacobi["convergio"] else None
        ),
        diferencia_gauss_seidel=(
            _norma_diferencia(gauss_seidel["solucion"], solucion)
            if gauss_seidel["convergio"] else None
        ),
    )
    return referencia


def resolver_sistema_iterativo(matriz_exacta, b_exacto, x0_exacto,
                              tolerancia, maximo):
    """Ejecuta ambos métodos y adjunta comparación y solución de referencia."""
    matriz = [[float(valor) for valor in fila] for fila in matriz_exacta]
    vector = [float(valor) for valor in b_exacto]
    inicial = [float(valor) for valor in x0_exacto]
    resultado = resolver_metodos(matriz, vector, inicial, tolerancia, maximo)
    jacobi = resultado["jacobi"]
    gauss_seidel = resultado["gauss_seidel"]
    resultado["comparacion"] = _comparar_metodos(jacobi, gauss_seidel)
    resultado["referencia"] = _validar_referencia(
        matriz_exacta, b_exacto, jacobi, gauss_seidel
    )
    return resultado
