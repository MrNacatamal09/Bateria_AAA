from fractions import Fraction

from programas.determinantes.determinante import (
    validar_matriz_cuadrada,
    obtener_menor,
    obtener_signo_cofactor,
    calcular_determinante,
    seleccionar_fila_o_columna
)


# ==========================================================
# PROCEDIMIENTO DEL DETERMINANTE
# ==========================================================


def calcular_determinante_con_procedimiento(
    matriz
):

    validar_matriz_cuadrada(
        matriz
    )

    orden = len(
        matriz
    )

    # ======================================================
    # CASO 1 x 1
    # ======================================================

    if orden == 1:

        valor = matriz[0][0]

        return {
            "orden":
                1,

            "matriz":
                matriz,

            "tipo_desarrollo":
                "directo",

            "determinante":
                valor,

            "terminos":
                []
        }

    # ======================================================
    # CASO 2 x 2
    # ======================================================

    if orden == 2:

        a = matriz[0][0]
        b = matriz[0][1]
        c = matriz[1][0]
        d = matriz[1][1]

        producto_1 = (
            a * d
        )

        producto_2 = (
            b * c
        )

        determinante = (
            producto_1
            - producto_2
        )

        return {
            "orden":
                2,

            "matriz":
                matriz,

            "tipo_desarrollo":
                "2x2",

            "a":
                a,

            "b":
                b,

            "c":
                c,

            "d":
                d,

            "producto_1":
                producto_1,

            "producto_2":
                producto_2,

            "determinante":
                determinante,

            "terminos":
                []
        }

    # ======================================================
    # MATRICES DE ORDEN 3 O MAYOR
    # ======================================================

    tipo, indice = seleccionar_fila_o_columna(
        matriz
    )

    determinante = Fraction(
        0
    )

    terminos = []

    # ======================================================
    # DESARROLLO POR FILA
    # ======================================================

    if tipo == "fila":

        fila = indice

        for columna in range(
            orden
        ):

            elemento = matriz[
                fila
            ][
                columna
            ]

            signo = obtener_signo_cofactor(
                fila,
                columna
            )

            # Si el elemento es cero,
            # el término completo vale cero.
            if elemento == 0:

                terminos.append(
                    {
                        "fila":
                            fila,

                        "columna":
                            columna,

                        "elemento":
                            elemento,

                        "signo":
                            signo,

                        "menor":
                            None,

                        "determinante_menor":
                            Fraction(0),

                        "cofactor":
                            Fraction(0),

                        "termino":
                            Fraction(0),

                        "omitido":
                            True
                    }
                )

                continue

            menor = obtener_menor(
                matriz,
                fila,
                columna
            )

            determinante_menor = (
                calcular_determinante(
                    menor
                )
            )

            cofactor = (
                signo
                * determinante_menor
            )

            termino = (
                elemento
                * cofactor
            )

            determinante += termino

            terminos.append(
                {
                    "fila":
                        fila,

                    "columna":
                        columna,

                    "elemento":
                        elemento,

                    "signo":
                        signo,

                    "menor":
                        menor,

                    "determinante_menor":
                        determinante_menor,

                    "cofactor":
                        cofactor,

                    "termino":
                        termino,

                    "omitido":
                        False
                }
            )

    # ======================================================
    # DESARROLLO POR COLUMNA
    # ======================================================

    else:

        columna = indice

        for fila in range(
            orden
        ):

            elemento = matriz[
                fila
            ][
                columna
            ]

            signo = obtener_signo_cofactor(
                fila,
                columna
            )

            if elemento == 0:

                terminos.append(
                    {
                        "fila":
                            fila,

                        "columna":
                            columna,

                        "elemento":
                            elemento,

                        "signo":
                            signo,

                        "menor":
                            None,

                        "determinante_menor":
                            Fraction(0),

                        "cofactor":
                            Fraction(0),

                        "termino":
                            Fraction(0),

                        "omitido":
                            True
                    }
                )

                continue

            menor = obtener_menor(
                matriz,
                fila,
                columna
            )

            determinante_menor = (
                calcular_determinante(
                    menor
                )
            )

            cofactor = (
                signo
                * determinante_menor
            )

            termino = (
                elemento
                * cofactor
            )

            determinante += termino

            terminos.append(
                {
                    "fila":
                        fila,

                    "columna":
                        columna,

                    "elemento":
                        elemento,

                    "signo":
                        signo,

                    "menor":
                        menor,

                    "determinante_menor":
                        determinante_menor,

                    "cofactor":
                        cofactor,

                    "termino":
                        termino,

                    "omitido":
                        False
                }
            )

    # ======================================================
    # RESULTADO
    # ======================================================

    return {
        "orden":
            orden,

        "matriz":
            matriz,

        "tipo_desarrollo":
            tipo,

        "indice_desarrollo":
            indice,

        "terminos":
            terminos,

        "determinante":
            determinante
    }