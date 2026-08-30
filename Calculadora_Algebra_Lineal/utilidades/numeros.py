from fractions import Fraction


# Convertimos el valor ingresado a una fracción
def convertir_a_fraccion(valor):

    # Si ya es Fraction, no necesitamos convertirlo
    if isinstance(valor, Fraction):
        return valor

    # Convertimos otros valores a texto
    texto = str(valor).strip()

    # No permitimos campos vacíos
    if texto == "":
        raise ValueError("El valor no puede estar vacío.")

    # Permitimos coma como separador decimal
    texto = texto.replace(",", ".")

    try:
        return Fraction(texto)

    except (ValueError, ZeroDivisionError):
        raise ValueError(
            f"'{valor}' no es un número válido."
        )