"""
Da formato a las seis propiedades verificadas en el Programa 5.
Presenta ambos miembros de cada igualdad y la conclusión de la prueba.
Tema de clase: propiedades de matrices invertibles y determinantes.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

from utilidades.formato_determinantes import (
    formatear_matriz
)


def formatear_conclusion(cumple):
    """Devuelve la conclusión solicitada para una propiedad verificada."""
    if cumple:
        return "Se cumple"

    return "No se cumple"


def formatear_propiedad_1(resultado):
    """Presenta la comprobación de (A^-1)^-1 = A."""
    return (
        "PROPIEDAD 1\n"
        + "(A⁻¹)⁻¹ = A\n"
        + "=" * 60
        + "\n\n"
        + "Lado izquierdo:\n\n"
        + formatear_matriz(
            resultado["lado_izquierdo"]
        )
        + "\n\n"
        + "Lado derecho:\n\n"
        + formatear_matriz(
            resultado["lado_derecho"]
        )
        + "\n\n"
        + formatear_conclusion(
            resultado["cumple"]
        )
    )


def formatear_propiedad_2(resultado):
    """Presenta la comprobación de (AB)^-1 = B^-1 A^-1."""
    texto = (
        "PROPIEDAD 2\n"
        + "(AB)⁻¹ = B⁻¹A⁻¹\n"
        + "=" * 60
        + "\n\n"
        + "AB =\n\n"
        + formatear_matriz(
            resultado["producto_ab"]
        )
        + "\n\n"
        + "(AB)⁻¹ =\n\n"
        + formatear_matriz(
            resultado["lado_izquierdo"]
        )
        + "\n\n"
        + "B⁻¹A⁻¹ =\n\n"
        + formatear_matriz(
            resultado["lado_derecho"]
        )
        + "\n\n"
    )

    return (
        texto
        + formatear_conclusion(
            resultado["cumple"]
        )
    )


def formatear_propiedad_3(resultado):
    """Presenta la comprobación de (A^T)^-1 = (A^-1)^T."""
    texto = (
        "PROPIEDAD 3\n"
        + "(Aᵀ)⁻¹ = (A⁻¹)ᵀ\n"
        + "=" * 60
        + "\n\n"
        + "Aᵀ =\n\n"
        + formatear_matriz(
            resultado["transpuesta_a"]
        )
        + "\n\n"
        + "(Aᵀ)⁻¹ =\n\n"
        + formatear_matriz(
            resultado["lado_izquierdo"]
        )
        + "\n\n"
        + "(A⁻¹)ᵀ =\n\n"
        + formatear_matriz(
            resultado["lado_derecho"]
        )
        + "\n\n"
    )

    return (
        texto
        + formatear_conclusion(
            resultado["cumple"]
        )
    )


def formatear_propiedad_4(resultado):
    """Presenta la comprobación de det(A^-1) = 1/det(A)."""
    texto = (
        "PROPIEDAD 4\n"
        + "det(A⁻¹) = 1/det(A)\n"
        + "=" * 60
        + "\n\n"
        + "A⁻¹ =\n\n"
        + formatear_matriz(
            resultado["inversa_a"]
        )
        + "\n\n"
        + "det(A) = "
        + str(
            resultado["determinante_a"]
        )
        + "\n\n"
        + "Lado izquierdo:\n"
        + "det(A⁻¹) = "
        + str(
            resultado["lado_izquierdo"]
        )
        + "\n\n"
        + "Lado derecho:\n"
        + "1/det(A) = "
        + str(
            resultado["lado_derecho"]
        )
        + "\n\n"
    )

    return (
        texto
        + formatear_conclusion(
            resultado["cumple"]
        )
    )


def formatear_operacion_fila(nombre, resultado):
    """Presenta una operación elemental y su efecto sobre el determinante."""
    texto = (
        nombre
        + "\n"
        + "-" * 60
        + "\n\n"
        + "Operación:\n"
        + resultado["operacion"]
        + "\n\n"
        + "Matriz resultante:\n\n"
        + formatear_matriz(
            resultado["matriz_transformada"]
        )
        + "\n\n"
        + "det(A) original = "
        + str(
            resultado["determinante_original"]
        )
        + "\n"
        + "Determinante obtenido = "
        + str(
            resultado["determinante_transformado"]
        )
        + "\n"
        + "Valor esperado = "
        + str(
            resultado["valor_esperado"]
        )
        + "\n\n"
        + formatear_conclusion(
            resultado["cumple"]
        )
    )

    return texto


def formatear_propiedad_5(resultado):
    """Presenta las tres reglas del determinante ante operaciones de fila."""
    texto = (
        "PROPIEDAD 5\n"
        + "DETERMINANTE Y OPERACIONES DE FILA\n"
        + "=" * 60
        + "\n\n"
    )

    texto += formatear_operacion_fila(
        "A. Intercambio de dos filas",
        resultado["intercambio"]
    )

    texto += (
        "\n\n"
        + formatear_operacion_fila(
            "B. Reemplazo de una fila",
            resultado["reemplazo"]
        )
    )

    texto += (
        "\n\n"
        + formatear_operacion_fila(
            "C. Multiplicación de una fila por k",
            resultado["escalamiento"]
        )
    )

    texto += (
        "\n\n"
        + "=" * 60
        + "\n"
        + "Conclusión de la propiedad 5: "
        + formatear_conclusion(
            resultado["cumple"]
        )
    )

    return texto


def formatear_propiedad_6(resultado):
    """Presenta la comparación del determinante con la reducción triangular."""
    texto = (
        "PROPIEDAD 6\n"
        + "DETERMINANTE DE UNA MATRIZ TRIANGULAR\n"
        + "=" * 60
        + "\n\n"
        + "Matriz triangular obtenida:\n\n"
        + formatear_matriz(
            resultado["matriz_triangular"]
        )
        + "\n\n"
        + "Producto de la diagonal = "
        + str(
            resultado["producto_diagonal"]
        )
        + "\n"
        + "Intercambios de fila = "
        + str(
            resultado["intercambios"]
        )
        + "\n\n"
        + "Determinante por cofactores = "
        + str(
            resultado["determinante_cofactores"]
        )
        + "\n"
        + "Determinante triangular corregido = "
        + str(
            resultado["determinante_triangular"]
        )
        + "\n\n"
        + formatear_conclusion(
            resultado["cumple"]
        )
    )

    return texto


def formatear_propiedad(numero_propiedad, resultado):
    """Selecciona el formato correspondiente a una propiedad del 1 al 6."""
    formateadores = {
        1: formatear_propiedad_1,
        2: formatear_propiedad_2,
        3: formatear_propiedad_3,
        4: formatear_propiedad_4,
        5: formatear_propiedad_5,
        6: formatear_propiedad_6
    }

    if numero_propiedad not in formateadores:
        raise ValueError(
            "La propiedad debe estar entre 1 y 6."
        )

    return formateadores[
        numero_propiedad
    ](
        resultado
    )