from programas.programa_4.independencia_lineal import (
    analizar_independencia_lineal
)


# ==========================================================
# PROGRAMA 4
# RESOLVER INDEPENDENCIA LINEAL
# ==========================================================

def resolver_programa_4(
    vectores
):

    # ======================================================
    # ANALIZAMOS EL CONJUNTO DE VECTORES
    # ======================================================

    resultado = (
        analizar_independencia_lineal(
            vectores
        )
    )

    # ======================================================
    # DEVOLVEMOS UNA ESTRUCTURA UNIFORME
    # ======================================================

    return {
        "operacion":
            "independencia_lineal",

        "resultado":
            resultado
    }