"""Presentación textual del procedimiento del Programa 7.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

def _numero(valor):
    """Muestra un real con precisión suficiente y marca valores ausentes."""
    return "—" if valor is None else f"{valor:.10g}"


def formatear_biseccion(resultado):
    """Incluye criterio de parada, comparación y tabla iterativa."""
    lineas = [f"f(x) = {resultado['expresion']}",
              f"Intervalo inicial: {resultado['intervalo_inicial']}",
              "Los extremos de la tabla corresponden al intervalo ANTES de actualizarlo.",
              "xᵣ = a + (b − a)/2; Eᵦ = (b − a)/2; εₐ = |(xᵣ,k − xᵣ,k−1)/xᵣ,k|.",
              f"Iteraciones teóricas según ⌈log₂((b−a)/E)⌉: {resultado['iteraciones_teoricas']}",
              f"Iteraciones ejecutadas: {len(resultado['tabla'])}",
              f"Raíz aproximada: {_numero(resultado['raiz'])}",
              f"f(raíz): {_numero(resultado['valor_funcion'])}",
              f"Cota final Eᵦ: {_numero(resultado['cota'])}",
              resultado['motivo'], "",
              "k | a | b | xᵣ | f(a) | f(b) | f(xᵣ) | Eᵦ | Eₐ | εₐ"]
    for fila in resultado["tabla"]:
        lineas.append(" | ".join(_numero(fila[clave]) for clave in
                                  ("k", "a", "b", "xr", "fa", "fb", "fr", "eb", "ea", "er")))
    if resultado["referencia"]:
        referencia, diferencia = resultado["referencia"]
        lineas += ["", f"Contraste opcional con SciPy: {_numero(referencia)}",
                   f"Diferencia absoluta: {_numero(diferencia)}"]
    else:
        lineas += ["", "Contraste SciPy: no disponible o no aplicable."]
    lineas += ["La continuidad general debe comprobarse para el intervalo elegido; "
               "el muestreo solo detecta algunas discontinuidades."]
    return "\n".join(lineas)


def formatear_posicional(resultado):
    """Muestra todos los dígitos, incluidos los ceros, y sus potencias."""
    def expansion(terminos):
        return " + ".join(f"{d}·{base}^{potencia}" for d, base, potencia, _ in terminos)
    def valores(terminos):
        return " + ".join(str(valor) for _, _, _, valor in terminos)
    signo = "−" if resultado["valor"] < 0 else ""
    return "\n".join([
        f"Base de origen: {resultado['base_origen']}",
        f"Entrada: ({resultado['entrada']})_{resultado['base_origen']}",
        f"Valor decimal: ({resultado['valor']})₁₀",
        f"Valor binario: ({signo}{resultado['binario']})₂",
        "", "Descomposición en base 10:",
        f"({resultado['decimal']})₁₀ = {expansion(resultado['terminos_10'])}",
        f"             = {valores(resultado['terminos_10'])} = {resultado['decimal']}",
        "", "Descomposición en base 2:",
        f"({resultado['binario']})₂ = {expansion(resultado['terminos_2'])}",
        f"             = {valores(resultado['terminos_2'])} = {resultado['decimal']}₁₀",
        "En valores negativos se conserva el signo y se descompone el valor absoluto."
    ])


def formatear_errores(errores, propagacion, ejemplos):
    """Explica errores y los experimentos de punto flotante."""
    relativo = ("No definido (xᵥ = 0)" if errores["relativo"] is None
                else _numero(errores["relativo"]))
    porcentual = ("No definido (xᵥ = 0)" if errores["porcentual"] is None
                  else _numero(errores["porcentual"]) + " %")
    return "\n".join([
        "ERRORES DE LA APROXIMACIÓN", "Eₐ = |xᵥ − xₐ| = " + _numero(errores["absoluto"]),
        "Eᵣ = Eₐ/|xᵥ| = " + relativo,
        "Eᵣ(%) = 100·Eᵣ = " + porcentual, "",
        "PROPAGACIÓN: f(x)=sin(x)+x²",
        f"x = {_numero(propagacion['x'])}; Δx = {_numero(propagacion['delta'])}",
        "f′(x)=cos(x)+2x = " + _numero(propagacion["derivada"]),
        "Δy aproximado = f′(x)·Δx = " + _numero(propagacion["lineal"]),
        "Δy real = f(x+Δx)−f(x) = " + _numero(propagacion["real"]),
        "Diferencia absoluta = " + _numero(propagacion["diferencia"]),
        "La derivada da una aproximación de primer orden, mejor para Δx pequeño.", "",
        "REPRESENTACIÓN EN FLOAT (equipo actual)",
        f"0.1 + 0.2 = {ejemplos['suma']!r}; == 0.3 → {ejemplos['igual']}",
        "0.1 y 0.2 no tienen representación binaria finita; se redondean.",
        f"Épsilon de máquina = {_numero(ejemplos['epsilon'])}: separación entre 1.0 y el float siguiente.",
        f"Overflow controlado: 1e308·1e308 → {ejemplos['overflow']}; magnitud fuera del rango.",
        f"Underflow controlado: min_normal·epsilon/4 → {ejemplos['underflow']}; valor demasiado pequeño.",
        "El resultado de overflow/underflow depende del tipo y operación.", "",
        "TIPOS DE ERROR Y EJEMPLOS", "Inherente: una medida de 2.1 cm ya contiene incertidumbre.",
        "Redondeo: representar 0.1 en float aproxima el valor decimal.",
        "Truncamiento numérico: sustituir sin(x) por x omite términos de Taylor.",
        "Overflow: superar el mayor valor representable.",
        "Underflow: perder precisión o llegar a cero cerca del menor valor representable.",
        "Modelo matemático: ignorar resistencia del aire al estimar una trayectoria."
    ])
