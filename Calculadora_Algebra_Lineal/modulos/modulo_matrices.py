"""
Integra las funciones del Programa 5 para el Módulo III de la calculadora.
Reúne operaciones, determinantes, inversas y verificación de propiedades.
Tema de clase: Álgebra de Matrices, Determinantes y Matriz Inversa.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from teoremas.resumen_teoremas import (
    obtener_teoremas_matrices
)

from programas.programa_3.matrices import (
    sumar_matrices as _sumar_matrices,
    restar_matrices as _restar_matrices,
    multiplicar_matriz_escalar as _multiplicar_matriz_escalar,
    multiplicar_matrices as _multiplicar_matrices,
    transponer_matriz as _transponer_matriz
)

from programas.determinantes.determinante import (
    calcular_determinante as _calcular_determinante
)

from programas.determinantes.procedimiento_determinante import (
    comparar_procedimientos_determinante
)

from programas.matrices.inversa import (
    calcular_inversa
)

from programas.matrices.inversa_adjunta import (
    calcular_inversa_adjunta,
    comparar_metodos_inversa
)

from programas.matrices.diagnostico_invertibilidad import (
    analizar_invertibilidad,
    construir_diagnostico
)

from programas.matrices.verificador_propiedades import (
    verificar_inversa_de_inversa,
    verificar_inversa_producto,
    verificar_inversa_transpuesta,
    verificar_determinante_inversa,
    verificar_propiedad_operaciones_fila,
    verificar_determinante_triangular
)


NOMBRE_MODULO = "Álgebra de Matrices"

MODULO_DESARROLLADO = True


OPCIONES_MENU = {
    0: "Ver Teoremas Clave del Módulo",
    1: "Suma",
    2: "Resta",
    3: "Multiplicación por Escalar",
    4: "Producto Matricial",
    5: "Transposición",
    6: "Determinante",
    7: "Inversa por Gauss-Jordan",
    8: "Inversa por Matriz Adjunta",
    9: "Verificador de propiedades"
}


def sumar(matriz_a, matriz_b):
    """Devuelve A + B.
    Requiere matrices con las mismas dimensiones."""
    return _sumar_matrices(
        matriz_a,
        matriz_b
    )


def restar(matriz_a, matriz_b):
    """Devuelve A - B.
    Requiere matrices con las mismas dimensiones."""
    return _restar_matrices(
        matriz_a,
        matriz_b
    )


def multiplicar_por_escalar(matriz, escalar):
    """Multiplica cada entrada de una matriz por un escalar."""
    return _multiplicar_matriz_escalar(
        matriz,
        escalar
    )


def producto_matricial(matriz_a, matriz_b):
    """Devuelve A·B mediante la regla fila-columna."""
    return _multiplicar_matrices(
        matriz_a,
        matriz_b
    )


def transponer(matriz):
    """Devuelve la transpuesta de una matriz."""
    return _transponer_matriz(
        matriz
    )


def determinante(matriz):
    """Calcula el determinante mediante expansión por cofactores."""
    return _calcular_determinante(
        matriz
    )


def resolver_determinante(matriz):
    """Calcula y compara los métodos de determinante exigidos en el Programa 5."""
    return comparar_procedimientos_determinante(
        matriz
    )


def inversa_gauss_jordan(matriz):
    """Calcula la inversa mediante la reducción [A|I] hasta [I|A^-1]."""
    return calcular_inversa(
        matriz
    )


def inversa_por_adjunta(matriz):
    """Calcula la inversa mediante A^-1 = (1/det(A)) adj(A)."""
    return calcular_inversa_adjunta(
        matriz
    )


def comparar_inversas(matriz):
    """Compara las inversas obtenidas por Gauss-Jordan y matriz adjunta."""
    return comparar_metodos_inversa(
        matriz
    )


def diagnosticar_invertibilidad(matriz):
    """Analiza determinante, pivotes, independencia lineal e invertibilidad."""
    resultado = analizar_invertibilidad(
        matriz
    )

    resultado["diagnostico"] = construir_diagnostico(
        resultado
    )

    return resultado


def verificar_propiedad_1(matriz_a):
    """Verifica la igualdad (A^-1)^-1 = A."""
    return verificar_inversa_de_inversa(
        matriz_a
    )


def verificar_propiedad_2(matriz_a, matriz_b):
    """Verifica la igualdad (AB)^-1 = B^-1 A^-1."""
    return verificar_inversa_producto(
        matriz_a,
        matriz_b
    )


def verificar_propiedad_3(matriz_a):
    """Verifica la igualdad (A^T)^-1 = (A^-1)^T."""
    return verificar_inversa_transpuesta(
        matriz_a
    )


def verificar_propiedad_4(matriz_a):
    """Verifica la igualdad det(A^-1) = 1/det(A)."""
    return verificar_determinante_inversa(
        matriz_a
    )


def verificar_propiedad_5(
    matriz_a,
    fila_1,
    fila_2,
    escalar_reemplazo,
    fila_escalar,
    escalar_fila
):
    """Verifica el efecto de tres operaciones elementales sobre det(A)."""
    return verificar_propiedad_operaciones_fila(
        matriz_a,
        fila_1,
        fila_2,
        escalar_reemplazo,
        fila_escalar,
        escalar_fila
    )


def verificar_propiedad_6(matriz_a):
    """Compara el determinante por cofactores con la reducción triangular."""
    return verificar_determinante_triangular(
        matriz_a
    )


def obtener_logo_modulo():
    """Devuelve el logotipo ASCII correspondiente al Módulo III."""
    return """
======================================================
 MÓDULO: ÁLGEBRA DE MATRICES
 Operaciones, Determinantes e Inversa
 Programa 5 - Calculadora de Álgebra Lineal
======================================================
"""


def mostrar_logo_modulo():
    """Imprime el logotipo ASCII del Módulo III."""
    print(
        obtener_logo_modulo()
    )


def obtener_descripcion_modulo():
    """Devuelve una descripción breve del contenido del Programa 5."""
    return (
        "Este módulo reúne operaciones matriciales, "
        "cálculo de determinantes, métodos para obtener "
        "la matriz inversa y verificación de propiedades."
    )


def obtener_menu_modulo():
    """Devuelve como texto las opciones 0 a 9 del Programa 5."""
    lineas = []

    for numero, nombre in OPCIONES_MENU.items():
        lineas.append(
            f"{numero}. {nombre}"
        )

    return "\n".join(
        lineas
    )


def mostrar_menu_modulo():
    """Imprime el logotipo y las opciones del Programa 5."""
    mostrar_logo_modulo()

    print(
        obtener_menu_modulo()
    )


def obtener_teoremas_clave():
    """Devuelve los teoremas asociados al Módulo III."""
    return obtener_teoremas_matrices()


def mostrar_teoremas_clave():
    """Imprime los teoremas clave del Módulo III."""
    print(
        obtener_teoremas_clave()
    )


def obtener_funcionalidades_actuales():
    """Devuelve una copia de las opciones disponibles en el Programa 5."""
    return OPCIONES_MENU.copy()


def obtener_informacion_funcionalidad(numero_funcionalidad):
    """Devuelve el nombre asociado a una opción del Programa 5."""
    if numero_funcionalidad not in OPCIONES_MENU:
        raise ValueError(
            "La opción indicada no pertenece al Módulo III."
        )

    return OPCIONES_MENU[
        numero_funcionalidad
    ]


def modulo_esta_desarrollado():
    """Indica si el Módulo III está disponible en la calculadora."""
    return MODULO_DESARROLLADO


def validar_opcion_modulo(opcion):
    """Devuelve True si la opción pertenece al menú del Programa 5."""
    return opcion in OPCIONES_MENU