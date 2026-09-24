# Validamos que una matriz tenga una estructura correcta
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

    for i in range(len(matriz)):

        if len(matriz[i]) != numero_columnas:
            raise ValueError(
                "Todas las filas de la matriz A deben "
                "tener la misma cantidad de columnas."
            )


# Validamos que dos vectores tengan la misma dimensión
def validar_vectores(u, v):

    if not u:
        raise ValueError(
            "El vector u no puede estar vacío."
        )

    if not v:
        raise ValueError(
            "El vector v no puede estar vacío."
        )

    if len(u) != len(v):
        raise ValueError(
            "Los vectores u y v deben tener "
            "la misma dimensión."
        )


# Validamos las dimensiones según A de m x n
def validar_dimensiones(matriz_a, u, v):

    validar_matriz(
        matriz_a
    )

    validar_vectores(
        u,
        v
    )

    numero_columnas = len(
        matriz_a[0]
    )

    # u y v pertenecen a R^n
    if len(u) != numero_columnas:
        raise ValueError(
            "La dimensión del vector u debe coincidir "
            "con el número de columnas de A."
        )

    if len(v) != numero_columnas:
        raise ValueError(
            "La dimensión del vector v debe coincidir "
            "con el número de columnas de A."
        )


# Sumamos dos vectores
def sumar_vectores_propiedad(u, v):

    validar_vectores(
        u,
        v
    )

    resultado = []

    for i in range(len(u)):

        resultado.append(
            u[i] + v[i]
        )

    return resultado


# Multiplicamos un vector por un escalar
def multiplicar_vector_escalar_propiedad(
    vector,
    escalar
):

    resultado = []

    for i in range(len(vector)):

        resultado.append(
            escalar * vector[i]
        )

    return resultado


# Multiplicamos una matriz A por un vector x
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

    # i representa las filas de A
    for i in range(len(matriz_a)):

        suma = 0

        # j representa las columnas de A
        for j in range(numero_columnas):

            suma += (
                matriz_a[i][j]
                * vector[j]
            )

        resultado.append(
            suma
        )

    return resultado


# Verificamos la propiedad A(u + v) = Au + Av
def verificar_propiedad_suma(
    matriz_a,
    u,
    v
):

    validar_dimensiones(
        matriz_a,
        u,
        v
    )

    # Calculamos u + v
    suma_uv = sumar_vectores_propiedad(
        u,
        v
    )

    # Lado izquierdo: A(u + v)
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

    # Lado derecho: Au + Av
    lado_derecho = sumar_vectores_propiedad(
        au,
        av
    )

    return {
        "suma_uv": suma_uv,
        "au": au,
        "av": av,
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "se_cumple": (
            lado_izquierdo
            == lado_derecho
        )
    }


# Verificamos la propiedad A(cu) = c(Au)
def verificar_propiedad_escalar(
    matriz_a,
    u,
    escalar
):

    validar_matriz(
        matriz_a
    )

    numero_columnas = len(
        matriz_a[0]
    )

    if not u:
        raise ValueError(
            "El vector u no puede estar vacío."
        )

    if len(u) != numero_columnas:
        raise ValueError(
            "La dimensión del vector u debe coincidir "
            "con el número de columnas de A."
        )

    # Calculamos cu
    cu = multiplicar_vector_escalar_propiedad(
        u,
        escalar
    )

    # Lado izquierdo: A(cu)
    lado_izquierdo = multiplicar_matriz_vector(
        matriz_a,
        cu
    )

    # Calculamos Au
    au = multiplicar_matriz_vector(
        matriz_a,
        u
    )

    # Lado derecho: c(Au)
    lado_derecho = (
        multiplicar_vector_escalar_propiedad(
            au,
            escalar
        )
    )

    return {
        "cu": cu,
        "au": au,
        "lado_izquierdo": lado_izquierdo,
        "lado_derecho": lado_derecho,
        "se_cumple": (
            lado_izquierdo
            == lado_derecho
        )
    }


# Verificamos las dos propiedades del teorema
def verificar_propiedades_matriz(
    matriz_a,
    u,
    v,
    escalar
):

    validar_dimensiones(
        matriz_a,
        u,
        v
    )

    propiedad_suma = verificar_propiedad_suma(
        matriz_a,
        u,
        v
    )

    propiedad_escalar = (
        verificar_propiedad_escalar(
            matriz_a,
            u,
            escalar
        )
    )

    return {
        "matriz_a": matriz_a,
        "vector_u": u,
        "vector_v": v,
        "escalar": escalar,

        "filas_a": len(
            matriz_a
        ),

        "columnas_a": len(
            matriz_a[0]
        ),

        "propiedad_suma": propiedad_suma,
        "propiedad_escalar": propiedad_escalar,

        "teorema_verificado": (
            propiedad_suma["se_cumple"]
            and propiedad_escalar["se_cumple"]
        )
    }