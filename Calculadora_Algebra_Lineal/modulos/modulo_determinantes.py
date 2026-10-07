"""
Integra determinantes, matriz inversa y sus propiedades en el Módulo IV.
Reutiliza los motores matemáticos ya desarrollados en el proyecto.
Tema de clase: determinantes, matriz inversa y teorema de invertibilidad.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from copy import deepcopy
from fractions import Fraction

from teoremas.resumen_teoremas import obtener_teoremas_determinantes

from programas.programa_1.operaciones_fila import (
    intercambiar_filas,
    multiplicar_fila,
    sumar_multiplo_fila,
)

from programas.programa_3.matrices import (
    multiplicar_matrices,
    transponer_matriz,
)

from programas.programa_3.propiedades_matrices_generales import (
    matrices_iguales,
)

from programas.determinantes.determinante import (
    calcular_determinante,
    triangularizar_para_determinante,
)

from programas.determinantes.procedimiento_determinante import (
    comparar_procedimientos_determinante,
)

from programas.matrices.inversa import calcular_inversa

from programas.matrices.inversa_adjunta import (
    calcular_inversa_adjunta,
    comparar_metodos_inversa,
)


NOMBRE_MODULO = "Determinantes e Inversa"
MODULO_DESARROLLADO = True

OPCIONES_MENU = {
    6: "Determinante",
    7: "Inversa por Gauss-Jordan",
    8: "Inversa por Matriz Adjunta",
    9: "Verificador de propiedades",
}


def determinante(matriz_a):
    """Calcula det(A) mediante el motor general de determinantes."""
    return calcular_determinante(matriz_a)


def resolver_determinante(matriz_a):
    """Compara cofactores, Sarrus y reducción triangular cuando aplican."""
    return comparar_procedimientos_determinante(matriz_a)


def inversa_gauss_jordan(matriz_a):
    """Calcula A⁻¹ mediante Gauss-Jordan sobre [A|I]."""
    return calcular_inversa(matriz_a)


def inversa_por_adjunta(matriz_a):
    """Calcula A⁻¹ mediante det(A), cofactores y adj(A)."""
    return calcular_inversa_adjunta(matriz_a)


def comparar_inversas(matriz_a):
    """Compara la inversa por Gauss-Jordan y por matriz adjunta."""
    return comparar_metodos_inversa(matriz_a)


def diagnosticar_invertibilidad(matriz_a):
    """Relaciona det(A), pivotes, L.I., generación de ℝⁿ e invertibilidad."""
    det_a = calcular_determinante(matriz_a)
    triangular = triangularizar_para_determinante(matriz_a)
    orden = len(matriz_a)
    num_pivotes = triangular["num_pivotes"]
    es_invertible = det_a != 0 and num_pivotes == orden

    if es_invertible:
        texto = (
            "La matriz es invertible: det(A) ≠ 0, tiene n posiciones pivote, "
            "sus columnas son L.I. y generan ℝⁿ"
        )
    else:
        texto = "La matriz es singular (no tiene inversa): det(A) = 0"

    return {
        "determinante": det_a,
        "num_pivotes": num_pivotes,
        "es_invertible": es_invertible,
        "columnas_li": es_invertible,
        "genera_rn": es_invertible,
        "diagnostico": texto,
    }


def _obtener_inversa_valida(matriz_a, nombre="A"):
    """Obtiene la inversa y genera un error claro si la matriz es singular."""
    resultado = calcular_inversa(matriz_a)

    if not resultado["es_invertible"]:
        raise ValueError(
            f"La matriz {nombre} debe ser invertible para verificar esta propiedad."
        )

    return resultado["inversa"]


def _validar_mismo_orden(matriz_a, matriz_b):
    """Valida que A y B sean cuadradas y tengan el mismo orden."""
    if len(matriz_a) != len(matriz_a[0]):
        raise ValueError("La matriz A debe ser cuadrada.")

    if len(matriz_b) != len(matriz_b[0]):
        raise ValueError("La matriz B debe ser cuadrada.")

    if len(matriz_a) != len(matriz_b):
        raise ValueError("Las matrices A y B deben tener el mismo orden.")


def verificar_propiedad_1(matriz_a):
    """Verifica (A⁻¹)⁻¹ = A mostrando ambos lados."""
    inversa_a = _obtener_inversa_valida(matriz_a)
    inversa_inversa = _obtener_inversa_valida(inversa_a, "A⁻¹")

    return {
        "propiedad": "(A⁻¹)⁻¹ = A",
        "lado_izquierdo": inversa_inversa,
        "lado_derecho": matriz_a,
        "cumple": matrices_iguales(inversa_inversa, matriz_a),
    }


def verificar_propiedad_2(matriz_a, matriz_b):
    """Verifica (AB)⁻¹ = B⁻¹A⁻¹ mostrando ambos lados."""
    _validar_mismo_orden(matriz_a, matriz_b)
    inversa_a = _obtener_inversa_valida(matriz_a, "A")
    inversa_b = _obtener_inversa_valida(matriz_b, "B")
    producto_ab = multiplicar_matrices(matriz_a, matriz_b)
    inversa_producto = _obtener_inversa_valida(producto_ab, "AB")
    lado_derecho = multiplicar_matrices(inversa_b, inversa_a)

    return {
        "propiedad": "(AB)⁻¹ = B⁻¹A⁻¹",
        "producto_ab": producto_ab,
        "lado_izquierdo": inversa_producto,
        "lado_derecho": lado_derecho,
        "cumple": matrices_iguales(inversa_producto, lado_derecho),
    }


def verificar_propiedad_3(matriz_a):
    """Verifica (Aᵀ)⁻¹ = (A⁻¹)ᵀ mostrando ambos lados."""
    inversa_a = _obtener_inversa_valida(matriz_a)
    transpuesta_a = transponer_matriz(matriz_a)
    lado_izquierdo = _obtener_inversa_valida(transpuesta_a, "Aᵀ")
    lado_derecho = transponer_matriz(inversa_a)

    return {
        "propiedad": "(Aᵀ)⁻¹ = (A⁻¹)ᵀ",
        "transpuesta_a": transpuesta_a,
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "cumple": matrices_iguales(lado_izquierdo, lado_derecho),
    }


def verificar_propiedad_4(matriz_a):
    """Verifica det(A⁻¹) = 1/det(A)."""
    inversa_a = _obtener_inversa_valida(matriz_a)
    det_a = calcular_determinante(matriz_a)
    det_inversa = calcular_determinante(inversa_a)
    valor_esperado = Fraction(1, 1) / det_a

    return {
        "propiedad": "det(A⁻¹) = 1/det(A)",
        "inversa_a": inversa_a,
        "determinante_a": det_a,
        "lado_izquierdo": det_inversa,
        "lado_derecho": valor_esperado,
        "cumple": det_inversa == valor_esperado,
    }


def _validar_indice_fila(indice, orden, nombre):
    """Valida que un índice de fila pertenezca a la matriz."""
    if indice < 0 or indice >= orden:
        raise ValueError(f"{nombre} debe estar entre 1 y {orden}.")


def _texto_reemplazo(fila_destino, fila_origen, escalar):
    """Construye una operación Fi -> Fi + kFj con signo natural."""
    if escalar < 0:
        return (
            f"F{fila_destino + 1} -> F{fila_destino + 1} "
            f"- ({-escalar})F{fila_origen + 1}"
        )

    return (
        f"F{fila_destino + 1} -> F{fila_destino + 1} "
        f"+ ({escalar})F{fila_origen + 1}"
    )


def verificar_propiedad_5(
    matriz_a,
    fila_1,
    fila_2,
    escalar_reemplazo,
    fila_escalar,
    escalar_fila,
):
    """Verifica el efecto de tres operaciones de fila sobre det(A)."""
    orden = len(matriz_a)
    _validar_indice_fila(fila_1, orden, "Fila 1")
    _validar_indice_fila(fila_2, orden, "Fila 2")
    _validar_indice_fila(fila_escalar, orden, "Fila a escalar")

    if fila_1 == fila_2:
        raise ValueError("Para el intercambio debe seleccionar dos filas diferentes.")

    if escalar_fila == 0:
        raise ValueError("El escalar usado para multiplicar una fila no puede ser cero.")

    det_original = calcular_determinante(matriz_a)

    matriz_intercambio = deepcopy(matriz_a)
    intercambiar_filas(matriz_intercambio, fila_1, fila_2)
    det_intercambio = calcular_determinante(matriz_intercambio)

    matriz_reemplazo = deepcopy(matriz_a)
    sumar_multiplo_fila(
        matriz_reemplazo,
        fila_2,
        fila_1,
        escalar_reemplazo,
    )
    det_reemplazo = calcular_determinante(matriz_reemplazo)

    matriz_escalamiento = deepcopy(matriz_a)
    multiplicar_fila(matriz_escalamiento, fila_escalar, escalar_fila)
    det_escalamiento = calcular_determinante(matriz_escalamiento)

    intercambio = {
        "operacion": f"F{fila_1 + 1} <-> F{fila_2 + 1}",
        "matriz": matriz_intercambio,
        "determinante_obtenido": det_intercambio,
        "valor_esperado": -det_original,
        "cumple": det_intercambio == -det_original,
    }

    reemplazo = {
        "operacion": _texto_reemplazo(fila_2, fila_1, escalar_reemplazo),
        "matriz": matriz_reemplazo,
        "determinante_obtenido": det_reemplazo,
        "valor_esperado": det_original,
        "cumple": det_reemplazo == det_original,
    }

    escalamiento = {
        "operacion": f"F{fila_escalar + 1} -> ({escalar_fila})F{fila_escalar + 1}",
        "matriz": matriz_escalamiento,
        "determinante_obtenido": det_escalamiento,
        "valor_esperado": escalar_fila * det_original,
        "cumple": det_escalamiento == escalar_fila * det_original,
    }

    return {
        "propiedad": "Determinante y operaciones de fila",
        "determinante_original": det_original,
        "intercambio": intercambio,
        "reemplazo": reemplazo,
        "escalamiento": escalamiento,
        "cumple": (
            intercambio["cumple"]
            and reemplazo["cumple"]
            and escalamiento["cumple"]
        ),
    }


def verificar_propiedad_6(matriz_a):
    """Compara el determinante triangular corregido con cofactores."""
    triangular = triangularizar_para_determinante(matriz_a)
    det_cofactores = calcular_determinante(matriz_a)
    det_triangular = triangular["determinante"]

    return {
        "propiedad": "Determinante de una matriz triangular",
        "matriz_triangular": triangular["matriz_triangular"],
        "producto_diagonal": triangular["producto_diagonal"],
        "intercambios": triangular["intercambios"],
        "determinante_cofactores": det_cofactores,
        "determinante_triangular": det_triangular,
        "cumple": det_cofactores == det_triangular,
    }


def obtener_logo_modulo():
    """Devuelve el logotipo textual del Módulo IV."""
    return """
============================================================
 MÓDULO IV - DETERMINANTES E INVERSA
 Determinantes, Matriz Inversa y Propiedades
============================================================
"""


def mostrar_logo_modulo():
    """Muestra en consola el logotipo textual del módulo."""
    print(obtener_logo_modulo())


def obtener_descripcion_modulo():
    """Devuelve una descripción breve del Módulo IV."""
    return (
        "Este módulo reúne determinantes, matriz inversa por Gauss-Jordan, "
        "matriz inversa por adjunta y propiedades asociadas."
    )


def obtener_menu_modulo():
    """Construye el menú de las opciones 6 a 9 del Módulo IV."""
    return "\n".join(
        f"{numero}. {OPCIONES_MENU[numero]}"
        for numero in range(6, 10)
    )


def mostrar_menu_modulo():
    """Muestra el logotipo y el menú del Módulo IV."""
    mostrar_logo_modulo()
    print(obtener_menu_modulo())


def obtener_teoremas_clave():
    """Devuelve los teoremas correspondientes al Módulo IV."""
    return obtener_teoremas_determinantes()


def mostrar_teoremas_clave():
    """Muestra en consola los teoremas del Módulo IV."""
    print(obtener_teoremas_clave())


def obtener_funcionalidades_actuales():
    """Devuelve una copia de las opciones 6 a 9."""
    return OPCIONES_MENU.copy()


def obtener_informacion_funcionalidad(numero_funcionalidad):
    """Devuelve nombre y número de una opción válida del Módulo IV."""
    if numero_funcionalidad not in OPCIONES_MENU:
        raise ValueError(
            "La funcionalidad indicada no pertenece al Módulo de Determinantes."
        )

    return {
        "numero": numero_funcionalidad,
        "nombre": OPCIONES_MENU[numero_funcionalidad],
    }


def modulo_esta_desarrollado():
    """Indica si el módulo de determinantes se encuentra habilitado."""
    return MODULO_DESARROLLADO


def validar_opcion_modulo(opcion):
    """Devuelve True si la opción pertenece al rango 6 a 9."""
    return opcion in OPCIONES_MENU
