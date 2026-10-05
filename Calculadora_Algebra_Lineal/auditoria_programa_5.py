"""
Audita los archivos relacionados con el Programa 5.
Comprueba sintaxis, imports prohibidos, docstrings y separación del cálculo.
Tema de clase: revisión final del Módulo III de Álgebra de Matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""

import ast
from pathlib import Path


RAIZ = Path(__file__).parent


ARCHIVOS_PROGRAMA_5 = [
    "main.py",
    "modulos/modulo_matrices.py",
    "controladores/modulo_matrices_controller.py",
    "interfaz/modulo_matrices_interfaz.py",
    "teoremas/resumen_teoremas.py",
    "programas/determinantes/determinante.py",
    "programas/determinantes/procedimiento_determinante.py",
    "programas/matrices/inversa_adjunta.py",
    "programas/matrices/diagnostico_invertibilidad.py",
    "programas/matrices/verificador_propiedades.py",
    "utilidades/formato_determinantes.py",
    "utilidades/formato_inversa_adjunta.py",
    "utilidades/formato_propiedades_programa_5.py"
]


ARCHIVOS_CALCULO = [
    "programas/determinantes/determinante.py",
    "programas/determinantes/procedimiento_determinante.py",
    "programas/matrices/inversa_adjunta.py",
    "programas/matrices/diagnostico_invertibilidad.py",
    "programas/matrices/verificador_propiedades.py"
]


AUTORES = [
    "Alexa Loaisiga",
    "Adolfo Ramírez",
    "Andy Díaz"
]


MODULOS_PROHIBIDOS = {
    "math",
    "numpy",
    "scipy"
}


def cargar_arbol(ruta):
    """Lee un archivo Python y devuelve su árbol sintáctico."""
    contenido = ruta.read_text(
        encoding="utf-8"
    )

    return ast.parse(
        contenido,
        filename=str(ruta)
    )


def auditar_sintaxis():
    """Comprueba que todos los archivos Python tengan sintaxis válida."""
    errores = []

    for ruta in RAIZ.rglob("*.py"):
        try:
            cargar_arbol(
                ruta
            )

        except SyntaxError as error:
            errores.append(
                (
                    ruta.relative_to(RAIZ),
                    error.lineno,
                    error.msg
                )
            )

    return errores


def auditar_imports_prohibidos():
    """Busca imports de math, NumPy o SciPy en todos los archivos Python."""
    errores = []

    for ruta in RAIZ.rglob("*.py"):
        try:
            arbol = cargar_arbol(
                ruta
            )

        except SyntaxError:
            continue

        for nodo in ast.walk(arbol):
            if isinstance(
                nodo,
                ast.Import
            ):
                for alias in nodo.names:
                    modulo = alias.name.split(
                        "."
                    )[0]

                    if modulo in MODULOS_PROHIBIDOS:
                        errores.append(
                            (
                                ruta.relative_to(RAIZ),
                                nodo.lineno,
                                alias.name
                            )
                        )

            elif isinstance(
                nodo,
                ast.ImportFrom
            ):
                if nodo.module is None:
                    continue

                modulo = nodo.module.split(
                    "."
                )[0]

                if modulo in MODULOS_PROHIBIDOS:
                    errores.append(
                        (
                            ruta.relative_to(RAIZ),
                            nodo.lineno,
                            nodo.module
                        )
                    )

    return errores


def auditar_docstrings():
    """Comprueba docstring de módulo, autores y funciones del Programa 5."""
    errores = []

    for nombre_archivo in ARCHIVOS_PROGRAMA_5:
        ruta = RAIZ / nombre_archivo

        if not ruta.exists():
            errores.append(
                (
                    nombre_archivo,
                    "Archivo no encontrado"
                )
            )
            continue

        try:
            arbol = cargar_arbol(
                ruta
            )

        except SyntaxError:
            continue

        docstring_modulo = ast.get_docstring(
            arbol
        )

        if not docstring_modulo:
            errores.append(
                (
                    nombre_archivo,
                    "Falta docstring de módulo"
                )
            )

        else:
            for autor in AUTORES:
                if autor not in docstring_modulo:
                    errores.append(
                        (
                            nombre_archivo,
                            f"Falta autor: {autor}"
                        )
                    )

        for nodo in ast.walk(arbol):
            if isinstance(
                nodo,
                (
                    ast.FunctionDef,
                    ast.AsyncFunctionDef
                )
            ):
                if not ast.get_docstring(
                    nodo
                ):
                    errores.append(
                        (
                            nombre_archivo,
                            (
                                "Falta docstring en función: "
                                + nodo.name
                            )
                        )
                    )

    return errores


def auditar_entrada_salida_calculo():
    """Detecta input() o print() dentro de los motores matemáticos del Programa 5."""
    errores = []

    for nombre_archivo in ARCHIVOS_CALCULO:
        ruta = RAIZ / nombre_archivo

        if not ruta.exists():
            continue

        try:
            arbol = cargar_arbol(
                ruta
            )

        except SyntaxError:
            continue

        for nodo in ast.walk(arbol):
            if not isinstance(
                nodo,
                ast.Call
            ):
                continue

            if not isinstance(
                nodo.func,
                ast.Name
            ):
                continue

            if nodo.func.id in {
                "input",
                "print"
            }:
                errores.append(
                    (
                        nombre_archivo,
                        nodo.lineno,
                        nodo.func.id
                    )
                )

    return errores


def mostrar_resultado(
    titulo,
    errores,
    formateador
):
    """Muestra el estado de una categoría de auditoría."""
    print()
    print(
        "=" * 60
    )

    print(
        titulo
    )

    print(
        "=" * 60
    )

    if not errores:
        print(
            "CORRECTO"
        )
        return

    for error in errores:
        print(
            formateador(
                error
            )
        )


def main():
    """Ejecuta todas las comprobaciones de la auditoría final."""
    errores_sintaxis = auditar_sintaxis()

    errores_imports = auditar_imports_prohibidos()

    errores_docstrings = auditar_docstrings()

    errores_entrada_salida = (
        auditar_entrada_salida_calculo()
    )

    mostrar_resultado(
        "1. SINTAXIS",
        errores_sintaxis,
        lambda error: (
            f"{error[0]} | línea {error[1]} | {error[2]}"
        )
    )

    mostrar_resultado(
        "2. IMPORTS PROHIBIDOS",
        errores_imports,
        lambda error: (
            f"{error[0]} | línea {error[1]} | {error[2]}"
        )
    )

    mostrar_resultado(
        "3. DOCUMENTACIÓN DEL PROGRAMA 5",
        errores_docstrings,
        lambda error: (
            f"{error[0]} | {error[1]}"
        )
    )

    mostrar_resultado(
        "4. INPUT / PRINT EN MOTORES MATEMÁTICOS",
        errores_entrada_salida,
        lambda error: (
            f"{error[0]} | línea {error[1]} | {error[2]}()"
        )
    )

    total_errores = (
        len(
            errores_sintaxis
        )
        + len(
            errores_imports
        )
        + len(
            errores_docstrings
        )
        + len(
            errores_entrada_salida
        )
    )

    print()
    print(
        "=" * 60
    )

    print(
        "RESULTADO FINAL"
    )

    print(
        "=" * 60
    )

    if total_errores == 0:
        print(
            "AUDITORÍA DEL PROGRAMA 5: CORRECTA"
        )

    else:
        print(
            "Se encontraron "
            + str(
                total_errores
            )
            + " observaciones."
        )


if __name__ == "__main__":
    main()