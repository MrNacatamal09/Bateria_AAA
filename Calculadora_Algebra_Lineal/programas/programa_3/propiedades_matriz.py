# ==========================================================
# VALIDACIONES
# ==========================================================

def validar_matriz(matriz):

    if not matriz:
        raise ValueError(
            "La matriz A no puede estar vacía."
        )

    numero_columnas = len(
        matriz[0]
    )

    if numero_columnas == 0:
        raise ValueError(
            "La matriz A debe tener al menos una columna."
        )

    for fila in matriz:

        if len(fila) != numero_columnas:

            raise ValueError(
                "Todas las filas de la matriz A deben "
                "tener la misma cantidad de columnas."
            )


def validar_vector(
    vector,
    nombre_vector
):

    if not vector:

        raise ValueError(
            f"El vector {nombre_vector} no puede estar vacío."
        )


def validar_dimension_vector(
    matriz_a,
    vector,
    nombre_vector
):

    validar_matriz(
        matriz_a
    )

    validar_vector(
        vector,
        nombre_vector
    )

    numero_columnas = len(
        matriz_a[0]
    )

    if len(vector) != numero_columnas:

        raise ValueError(
            f"La dimensión del vector {nombre_vector} "
            "debe coincidir con el número de columnas de A."
        )


def validar_vectores_suma(
    matriz_a,
    u,
    v
):

    validar_dimension_vector(
        matriz_a,
        u,
        "u"
    )

    validar_dimension_vector(
        matriz_a,
        v,
        "v"
    )

    if len(u) != len(v):

        raise ValueError(
            "Los vectores u y v deben tener "
            "la misma dimensión."
        )


# ==========================================================
# OPERACIONES CON VECTORES
# ==========================================================

def sumar_vectores_propiedad(
    u,
    v
):

    if len(u) != len(v):

        raise ValueError(
            "Los vectores deben tener "
            "la misma dimensión."
        )

    resultado = []

    for i in range(
        len(u)
    ):

        resultado.append(
            u[i] + v[i]
        )

    return resultado


def multiplicar_vector_escalar_propiedad(
    vector,
    escalar
):

    resultado = []

    for valor in vector:

        resultado.append(
            escalar * valor
        )

    return resultado


# ==========================================================
# MULTIPLICACIÓN MATRIZ POR VECTOR
# ==========================================================

def multiplicar_matriz_vector(
    matriz_a,
    vector
):

    validar_matriz(
        matriz_a
    )

    numero_columnas = len(
        matriz_a[0]
    )

    if len(vector) != numero_columnas:

        raise ValueError(
            "La dimensión del vector debe coincidir "
            "con el número de columnas de la matriz."
        )

    resultado = []

    # i representa las filas
    for i in range(
        len(matriz_a)
    ):

        suma = 0

        # j representa las columnas
        for j in range(
            numero_columnas
        ):

            suma += (
                matriz_a[i][j]
                * vector[j]
            )

        resultado.append(
            suma
        )

    return resultado


# ==========================================================
# PROPIEDAD A(u + v) = Au + Av
# ==========================================================

def verificar_propiedad_suma(
    matriz_a,
    u,
    v
):

    validar_vectores_suma(
        matriz_a,
        u,
        v
    )

    # Calculamos u + v
    suma_uv = sumar_vectores_propiedad(
        u,
        v
    )

    # Lado izquierdo
    lado_izquierdo = multiplicar_matriz_vector(
        matriz_a,
        suma_uv
    )

    # Calculamos Au
    au = multiplicar_matriz_vector(
        matriz_a,
        u
    )

    # Calculamos Av
    av = multiplicar_matriz_vector(
        matriz_a,
        v
    )

    # Lado derecho
    lado_derecho = sumar_vectores_propiedad(
        au,
        av
    )

    return {
        "suma_uv":
            suma_uv,

        "au":
            au,

        "av":
            av,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "se_cumple":
            lado_izquierdo
            == lado_derecho
    }


# ==========================================================
# PROPIEDAD A(cu) = c(Au)
# ==========================================================

def verificar_propiedad_escalar(
    matriz_a,
    u,
    escalar
):

    validar_dimension_vector(
        matriz_a,
        u,
        "u"
    )

    # Calculamos cu
    cu = multiplicar_vector_escalar_propiedad(
        u,
        escalar
    )

    # Lado izquierdo
    lado_izquierdo = multiplicar_matriz_vector(
        matriz_a,
        cu
    )

    # Calculamos Au
    au = multiplicar_matriz_vector(
        matriz_a,
        u
    )

    # Lado derecho
    lado_derecho = (
        multiplicar_vector_escalar_propiedad(
            au,
            escalar
        )
    )

    return {
        "cu":
            cu,

        "au":
            au,

        "lado_izquierdo":
            lado_izquierdo,

        "lado_derecho":
            lado_derecho,

        "se_cumple":
            lado_izquierdo
            == lado_derecho
    }


# ==========================================================
# RESOLUCIÓN DE LA PROPIEDAD SELECCIONADA
# ==========================================================

def verificar_propiedades_matriz(
    operacion,
    matriz_a,
    u,
    v=None,
    escalar=None
):

    validar_matriz(
        matriz_a
    )

    if operacion not in (
        "suma",
        "escalar",
        "ambas"
    ):

        raise ValueError(
            "La propiedad seleccionada no es válida."
        )

    propiedad_suma = None
    propiedad_escalar = None

    # ======================================================
    # SOLO A(u + v) = Au + Av
    # ======================================================

    if operacion == "suma":

        if v is None:

            raise ValueError(
                "Debe ingresar el vector v."
            )

        propiedad_suma = (
            verificar_propiedad_suma(
                matriz_a,
                u,
                v
            )
        )

        teorema_verificado = (
            propiedad_suma[
                "se_cumple"
            ]
        )

    # ======================================================
    # SOLO A(cu) = c(Au)
    # ======================================================

    elif operacion == "escalar":

        if escalar is None:

            raise ValueError(
                "Debe ingresar el escalar c."
            )

        propiedad_escalar = (
            verificar_propiedad_escalar(
                matriz_a,
                u,
                escalar
            )
        )

        teorema_verificado = (
            propiedad_escalar[
                "se_cumple"
            ]
        )

    # ======================================================
    # AMBAS PROPIEDADES
    # ======================================================

    else:

        if v is None:

            raise ValueError(
                "Debe ingresar el vector v."
            )

        if escalar is None:

            raise ValueError(
                "Debe ingresar el escalar c."
            )

        propiedad_suma = (
            verificar_propiedad_suma(
                matriz_a,
                u,
                v
            )
        )

        propiedad_escalar = (
            verificar_propiedad_escalar(
                matriz_a,
                u,
                escalar
            )
        )

        teorema_verificado = (
            propiedad_suma[
                "se_cumple"
            ]
            and
            propiedad_escalar[
                "se_cumple"
            ]
        )

    return {
        "operacion":
            operacion,

        "matriz_a":
            matriz_a,

        "vector_u":
            u,

        "vector_v":
            v,

        "escalar":
            escalar,

        "filas_a":
            len(
                matriz_a
            ),

        "columnas_a":
            len(
                matriz_a[0]
            ),

        "propiedad_suma":
            propiedad_suma,

        "propiedad_escalar":
            propiedad_escalar,

        "teorema_verificado":
            teorema_verificado
    }