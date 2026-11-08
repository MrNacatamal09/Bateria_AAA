"""Algoritmos del Programa 7, sin dependencias externas obligatorias.

Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import ast
import math
import sys


FUNCIONES = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
    "abs": abs,
}
CONSTANTES = {"pi": math.pi, "e": math.e}
OPERACIONES = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.Pow: lambda a, b: a ** b,
}


def numero_finito(valor, nombre):
    """Convierte una entrada escalar y exige un número real finito."""
    try:
        numero = float(str(valor).strip().replace(",", "."))
    except (ValueError, TypeError, OverflowError):
        raise ValueError(f"{nombre} debe ser un número real válido.") from None
    if not math.isfinite(numero):
        raise ValueError(f"{nombre} debe ser finito.")
    return numero


def entero_positivo(valor, nombre):
    """Valida un entero positivo sin aceptar decimales."""
    try:
        numero = int(str(valor).strip())
    except (ValueError, TypeError):
        raise ValueError(f"{nombre} debe ser un entero positivo.") from None
    if numero < 1:
        raise ValueError(f"{nombre} debe ser un entero positivo.")
    return numero


def _validar_nodo(nodo):
    """Comprueba la lista blanca antes de evaluar cualquier entrada."""
    if isinstance(nodo, ast.Expression):
        _validar_nodo(nodo.body)
    elif isinstance(nodo, ast.Constant) and type(nodo.value) in (int, float):
        try:
            finito = math.isfinite(float(nodo.value))
        except OverflowError:
            finito = False
        if not finito:
            raise ValueError("Las constantes deben ser finitas.")
    elif isinstance(nodo, ast.Name) and nodo.id in {"x", *CONSTANTES}:
        pass
    elif isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, (ast.UAdd, ast.USub)):
        _validar_nodo(nodo.operand)
    elif isinstance(nodo, ast.BinOp) and type(nodo.op) in OPERACIONES:
        _validar_nodo(nodo.left)
        _validar_nodo(nodo.right)
    elif (isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name)
          and nodo.func.id in FUNCIONES and len(nodo.args) == 1
          and not nodo.keywords):
        _validar_nodo(nodo.args[0])
    else:
        raise ValueError("Expresión no permitida. Use x, números, +, -, *, /, ** y funciones autorizadas.")


def _evaluar_nodo(nodo, x):
    """Evalúa exclusivamente nodos aceptados por el validador."""
    if isinstance(nodo, ast.Constant):
        return float(nodo.value)
    if isinstance(nodo, ast.Name):
        return x if nodo.id == "x" else CONSTANTES[nodo.id]
    if isinstance(nodo, ast.UnaryOp):
        valor = _evaluar_nodo(nodo.operand, x)
        return valor if isinstance(nodo.op, ast.UAdd) else -valor
    if isinstance(nodo, ast.BinOp):
        izquierdo = _evaluar_nodo(nodo.left, x)
        derecho = _evaluar_nodo(nodo.right, x)
        if isinstance(nodo.op, ast.Pow) and abs(derecho) > 1000:
            raise ValueError("El exponente es demasiado grande.")
        return OPERACIONES[type(nodo.op)](izquierdo, derecho)
    return FUNCIONES[nodo.func.id](_evaluar_nodo(nodo.args[0], x))


def compilar_funcion(expresion):
    """Crea una función segura a partir de una expresión matemática permitida."""
    texto = str(expresion).strip()
    if not texto or len(texto) > 250:
        raise ValueError("Escriba una función de hasta 250 caracteres.")
    try:
        arbol = ast.parse(texto, mode="eval")
        if sum(1 for _ in ast.walk(arbol)) > 100:
            raise ValueError("La función es demasiado compleja.")
        _validar_nodo(arbol)
    except (SyntaxError, RecursionError):
        raise ValueError("La función está mal escrita; use ** para potencias.") from None

    def funcion(x):
        try:
            valor = _evaluar_nodo(arbol.body, float(x))
            if isinstance(valor, complex) or not math.isfinite(valor):
                raise ValueError("El resultado no es real y finito.")
            return float(valor)
        except (ArithmeticError, OverflowError, ValueError, TypeError) as error:
            raise ValueError(f"f({x:g}) no está definida como número real finito: {error}") from None

    # Se conserva el árbol para examinar denominadores sin interpretar texto libre.
    funcion.arbol = arbol
    return funcion


def _revisar_continuidad(funcion, a, b):
    """Busca dominios inválidos y polos explícitos; no prueba continuidad general."""
    denominadores = [n.right for n in ast.walk(funcion.arbol)
                    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)]
    anterior = None
    for i in range(1025):
        x = a + (b - a) * i / 1024
        try:
            funcion(x)
            actuales = [_evaluar_nodo(nodo, x) for nodo in denominadores]
            if any(not math.isfinite(v) or v == 0 for v in actuales):
                raise ValueError("Hay una división por cero dentro del intervalo.")
            if anterior is not None and any(p * v < 0 for p, v in zip(anterior, actuales)):
                raise ValueError("Un denominador cambia de signo dentro del intervalo: posible discontinuidad.")
            anterior = actuales
        except (ArithmeticError, OverflowError) as error:
            raise ValueError(f"La función no es continua en el intervalo: {error}") from None
        except ValueError as error:
            raise ValueError(f"La función no cumple las condiciones de continuidad: {error}") from None


def biseccion(expresion, extremo_a, extremo_b, tolerancia, maximo):
    """Calcula la raíz por bisección y registra cada intervalo anterior al corte."""
    funcion = compilar_funcion(expresion)
    a = numero_finito(extremo_a, "a")
    b = numero_finito(extremo_b, "b")
    error = numero_finito(tolerancia, "La tolerancia")
    nmax = entero_positivo(maximo, "El máximo de iteraciones")
    if a >= b:
        raise ValueError("Se requiere a < b.")
    if not math.isfinite(b - a):
        raise ValueError("El intervalo excede el rango de float.")
    if error <= 0:
        raise ValueError("La tolerancia debe ser positiva.")
    fa, fb = funcion(a), funcion(b)
    teoricas = max(0, math.ceil(math.log2(b - a) - math.log2(error)))
    resultado = {"expresion": expresion, "intervalo_inicial": (a, b),
                 "iteraciones_teoricas": teoricas, "tabla": [], "referencia": None}
    if fa == 0 or fb == 0:
        raiz = a if fa == 0 else b
        resultado.update(raiz=raiz, valor_funcion=0.0, cota=0.0,
                         motivo="Raíz exacta en un extremo.", convergio=True,
                         intervalo_final=(raiz, raiz))
        return resultado
    # Comparar signos evita overflow/underflow en el producto fa*fb.
    if (fa < 0) == (fb < 0):
        raise ValueError("El intervalo no presenta cambio de signo; esto no descarta raíces en otros intervalos.")
    _revisar_continuidad(funcion, a, b)
    previo = None
    for k in range(1, nmax + 1):
        xr = a + (b - a) / 2
        eb = (b - a) / 2
        fr = funcion(xr)
        ea = None if previo is None else abs(xr - previo)
        er = None if previo is None or xr == 0 else ea / abs(xr)
        resultado["tabla"].append(dict(k=k, a=a, b=b, xr=xr, fa=fa, fb=fb,
                                       fr=fr, eb=eb, ea=ea, er=er))
        if fr == 0:
            motivo, convergio = "Raíz exacta en el punto medio.", True
            break
        if eb <= error:
            motivo, convergio = "Tolerancia absoluta alcanzada.", True
            break
        if xr == a or xr == b:
            motivo, convergio = "La precisión de float impide reducir más el intervalo.", False
            break
        if (fa < 0) != (fr < 0):
            b, fb = xr, fr
        else:
            a, fa = xr, fr
        previo = xr
    else:
        motivo, convergio = "Se alcanzó el máximo de iteraciones sin garantizar la tolerancia.", False
    # Una asíntota no puede convertirse en una raíz por reducir el intervalo.
    if convergio and fr != 0 and abs(fr) > max(abs(resultado["tabla"][0]["fa"]),
                                             abs(resultado["tabla"][0]["fb"])) * 1000:
        raise ValueError("El valor de f(x) crece al reducir el intervalo: posible discontinuidad, no raíz.")
    resultado.update(raiz=xr, valor_funcion=fr, cota=eb, motivo=motivo,
                     convergio=convergio, intervalo_final=(a, b))
    if convergio:
        try:
            from scipy.optimize import bisect as bisect_scipy
        except ImportError:
            pass
        else:
            try:
                referencia = bisect_scipy(funcion, *resultado["intervalo_inicial"])
                resultado["referencia"] = (referencia, abs(referencia - xr))
            except ValueError:
                pass
    return resultado


def puntos_grafica(expresion, limite_a, limite_b, cantidad=1201):
    """Muestrea la función, dejando cortes en dominios inválidos o saltos."""
    funcion = compilar_funcion(expresion)
    a = numero_finito(limite_a, "x mínimo")
    b = numero_finito(limite_b, "x máximo")
    if a >= b:
        raise ValueError("Se requiere x mínimo < x máximo.")
    if not math.isfinite(b - a):
        raise ValueError("El intervalo excede el rango de float.")
    cantidad = entero_positivo(cantidad, "La cantidad de puntos")
    if cantidad < 1000 or cantidad > 10000:
        raise ValueError("La gráfica requiere entre 1000 y 10000 puntos.")
    puntos = []
    for i in range(cantidad):
        x = a + (b - a) * i / (cantidad - 1)
        try:
            y = funcion(x)
        except ValueError:
            y = None
        puntos.append((x, y))
    validos = [abs(y) for _, y in puntos if y is not None]
    if not validos:
        raise ValueError("La función no tiene puntos reales finitos en este intervalo.")
    # Recortar extremos exagerados permite ver las ramas cerca de una asíntota.
    escala = sorted(validos)[int(0.95 * (len(validos) - 1))]
    limite = max(1.0, escala * 5)
    return {"expresion": expresion, "intervalo": (a, b), "puntos": puntos,
            "limite_visual": limite, "validos": len(validos)}


def notacion_posicional(texto, base):
    """Descompone un entero de origen decimal o binario en ambas bases."""
    if base not in (2, 10):
        raise ValueError("La base de origen debe ser 2 o 10.")
    entrada = str(texto).strip()
    if not entrada:
        raise ValueError("Escriba un número entero.")
    signo = -1 if entrada.startswith("-") else 1
    digitos = entrada.lstrip("+-")
    permitidos = "01" if base == 2 else "0123456789"
    if not digitos or any(c not in permitidos for c in digitos):
        raise ValueError(f"Escriba solo dígitos válidos para base {base}.")
    valor = signo * int(digitos, base)
    magnitud = abs(valor)
    decimal = str(magnitud)
    binario = format(magnitud, "b")
    def terminos(cadena, origen):
        return [(int(d), origen, len(cadena) - 1 - i,
                 int(d) * origen ** (len(cadena) - 1 - i))
                for i, d in enumerate(cadena)]
    return {"valor": valor, "base_origen": base, "entrada": entrada,
            "decimal": decimal, "binario": binario,
            "terminos_10": terminos(decimal, 10),
            "terminos_2": terminos(binario, 2)}


def calcular_errores(verdadero, aproximado):
    """Calcula errores absoluto, relativo y porcentual."""
    xv = numero_finito(verdadero, "El valor verdadero")
    xa = numero_finito(aproximado, "El valor aproximado")
    absoluto = abs(xv - xa)
    if not math.isfinite(absoluto):
        raise ValueError("La diferencia excede el rango de float.")
    relativo = None if xv == 0 else absoluto / abs(xv)
    return {"verdadero": xv, "aproximado": xa, "absoluto": absoluto,
            "relativo": relativo,
            "porcentual": None if relativo is None else relativo * 100}


def propagacion_error(x_entrada, delta_entrada):
    """Contrasta la derivada de sin(x)+x² con el cambio real."""
    x = numero_finito(x_entrada, "x")
    delta = numero_finito(delta_entrada, "Δx")
    try:
        funcion = lambda t: math.sin(t) + t * t
        derivada = math.cos(x) + 2 * x
        lineal = derivada * delta
        real = funcion(x + delta) - funcion(x)
        diferencia = abs(lineal - real)
    except (OverflowError, ValueError):
        raise ValueError("Los valores exceden el rango de cálculo.") from None
    if not all(map(math.isfinite, (derivada, lineal, real, diferencia))):
        raise ValueError("Los valores exceden el rango de cálculo.")
    return {"x": x, "delta": delta, "derivada": derivada,
            "lineal": lineal, "real": real, "diferencia": diferencia}


def ejemplos_punto_flotante():
    """Ejecuta ejemplos de representación con el float del equipo actual."""
    suma = 0.1 + 0.2
    try:
        overflow = (1e308 * 1e308)
    except OverflowError:
        overflow = math.inf
    underflow = sys.float_info.min * sys.float_info.epsilon / 4
    try:
        import numpy
        epsilon = float(numpy.finfo(float).eps)
    except ImportError:
        epsilon = math.nextafter(1.0, math.inf) - 1.0
    return {"suma": suma, "igual": suma == 0.3,
            "epsilon": epsilon,
            "overflow": overflow, "underflow": underflow}
