"""
Reúne los resúmenes teóricos utilizados por los cuatro módulos.
Separa matrices de determinantes e inversa según la organización actual.
Tema de clase: fundamentos y teoremas de Álgebra Lineal.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_sistemas():
    """Devuelve el resumen teórico del Módulo I."""
    return """
========================================================
MÓDULO 1 - SISTEMAS DE ECUACIONES LINEALES
========================================================

1. SISTEMA DE ECUACIONES LINEALES

Un sistema lineal es un conjunto de ecuaciones que puede
representarse mediante una matriz aumentada.

2. OPERACIONES ELEMENTALES POR FILAS

Las operaciones permitidas son:

- Intercambiar dos filas.
- Multiplicar una fila por un escalar diferente de cero.
- Sumar a una fila un múltiplo de otra.

Estas operaciones conservan el conjunto solución del sistema.

3. SISTEMA CONSISTENTE DETERMINADO

Posee una única solución.

En la forma escalonada reducida existe un pivote para cada
variable y no existen variables libres.

4. SISTEMA CONSISTENTE INDETERMINADO

Posee infinitas soluciones.

Existe al menos una variable libre y no aparece ninguna
contradicción.

5. SISTEMA INCONSISTENTE

No posee solución.

Puede aparecer una fila de la forma:

[ 0  0  ...  0 | b ]

con b diferente de cero.

6. VARIABLES BÁSICAS Y VARIABLES LIBRES

Las variables básicas corresponden a columnas pivote.

Las variables libres corresponden a columnas sin pivote y
pueden representarse con parámetros:

t₁, t₂, t₃, ...

7. FORMA ESCALONADA REDUCIDA POR FILAS

Una matriz está en forma escalonada reducida cuando:

- Cada pivote es 1.
- Cada pivote es el único valor distinto de cero de su columna.
- Los pivotes avanzan hacia la derecha.
- Las filas nulas quedan abajo.

8. MÉTODO DE GAUSS

Transforma la matriz aumentada hasta obtener una forma
escalonada.

9. MÉTODO DE GAUSS-JORDAN

Continúa la reducción hasta obtener la forma escalonada
reducida por filas.

Permite identificar pivotes, variables básicas, variables
libres y la solución del sistema.

========================================================
"""


def obtener_teoremas_vectores():
    """Devuelve el resumen teórico del Módulo II."""
    return """
========================================================
MÓDULO 2 - VECTORES E INDEPENDENCIA LINEAL
========================================================

1. COMBINACIÓN LINEAL

Un vector b es combinación lineal de:

v₁, v₂, ..., vₖ

si existen escalares:

c₁, c₂, ..., cₖ

tales que:

c₁v₁ + c₂v₂ + ... + cₖvₖ = b

2. ECUACIÓN MATRICIAL Ax = b

Si los vectores se colocan como columnas de A:

A = [ v₁  v₂  ...  vₖ ]

entonces la combinación lineal puede escribirse como:

Ax = b

3. SISTEMA HOMOGÉNEO

Un sistema homogéneo tiene la forma:

Ax = 0

Siempre posee la solución trivial.

4. SOLUCIÓN TRIVIAL

x₁ = 0
x₂ = 0
...
xₖ = 0

5. INDEPENDENCIA LINEAL

Los vectores son linealmente independientes cuando:

c₁v₁ + c₂v₂ + ... + cₖvₖ = 0

solo posee la solución trivial.

6. DEPENDENCIA LINEAL

Existe dependencia lineal cuando la ecuación homogénea posee
al menos una solución no trivial.

7. CRITERIO MEDIANTE VARIABLES LIBRES

- Sin variables libres: columnas linealmente independientes.
- Con al menos una variable libre: columnas dependientes.

8. CRITERIO MEDIANTE PIVOTES

- Un pivote en cada columna: independencia lineal.
- Alguna columna sin pivote: dependencia lineal.

========================================================
"""


def obtener_teoremas_matrices():
    """Devuelve los teoremas de operaciones y propiedades de matrices."""
    return """
========================================================
MÓDULO 3 - ÁLGEBRA DE MATRICES
========================================================

1. IGUALDAD DE MATRICES

Dos matrices son iguales si poseen las mismas dimensiones y
sus entradas correspondientes son iguales.

2. SUMA Y RESTA DE MATRICES

A + B y A - B están definidas cuando A y B poseen las mismas
dimensiones.

Las operaciones se realizan entrada por entrada.

3. MULTIPLICACIÓN POR ESCALAR

Si r es un escalar:

rA

se obtiene multiplicando cada entrada de A por r.

4. PROPIEDADES DE SUMA Y ESCALAR

Siempre que las operaciones estén definidas:

A + B = B + A

(A + B) + C = A + (B + C)

A + 0 = A

r(A + B) = rA + rB

(r + s)A = rA + sA

r(sA) = (rs)A

5. PRODUCTO MATRICIAL

Si A es m × n y B es n × p, entonces AB está definido y su
dimensión es:

m × p

Cada entrada se obtiene mediante la regla fila-columna:

(AB)ᵢⱼ =
aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ... + aᵢₙbₙⱼ

6. PROPIEDADES DEL PRODUCTO MATRICIAL

Siempre que las operaciones estén definidas:

A(BC) = (AB)C

A(B + C) = AB + AC

(B + C)A = BA + CA

r(AB) = (rA)B = A(rB)

IA = A = AI

En general:

AB ≠ BA

por lo que la multiplicación matricial no es conmutativa.

7. TRANSPUESTA

Si A es m × n, entonces Aᵀ es n × m.

Las filas de A pasan a ser las columnas de Aᵀ.

8. PROPIEDADES DE LA TRANSPUESTA

(Aᵀ)ᵀ = A

(A + B)ᵀ = Aᵀ + Bᵀ

(rA)ᵀ = rAᵀ

(AB)ᵀ = BᵀAᵀ

También puede combinarse la distributividad del escalar y
de la transpuesta:

(r(A + B))ᵀ = rAᵀ + rBᵀ

========================================================
"""


def obtener_teoremas_determinantes():
    """Devuelve determinantes, inversa, adjunta, Cramer y teoremas relacionados."""
    return """
========================================================
MÓDULO 4 - DETERMINANTES E INVERSA
========================================================

1. DETERMINANTE DE UNA MATRIZ 2 × 2

Sea:

A = [ a  b ]
    [ c  d ]

Entonces:

det(A) = ad - bc

2. MENOR Y COFACTOR

El menor Mᵢⱼ se obtiene eliminando la fila i y la columna j.

El cofactor correspondiente es:

Cᵢⱼ = (-1)^(i+j) det(Mᵢⱼ)

Los signos siguen el patrón alternado:

+  -  +  - ...
-  +  -  + ...
+  -  +  - ...
...

3. DESARROLLO POR COFACTORES

El determinante de una matriz cuadrada puede desarrollarse
por cualquier fila o columna.

Por la fila i:

det(A) =
aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢₙCᵢₙ

Conviene utilizar una fila o columna con muchos ceros.

4. REGLA DE SARRUS

La regla de Sarrus se aplica únicamente a matrices 3 × 3.

Se suman los productos de las diagonales descendentes y se
restan los productos de las diagonales ascendentes.

5. DETERMINANTE POR TRIANGULARIZACIÓN

Una matriz puede transformarse a forma triangular mediante
operaciones elementales por filas.

En una matriz triangular:

det(A)

es el producto de los elementos de la diagonal, considerando
los cambios producidos por las operaciones de fila.

6. EFECTO DE OPERACIONES DE FILA SOBRE det(A)

Intercambiar dos filas cambia el signo:

det(B) = -det(A)

Reemplazar una fila mediante:

Fᵢ -> Fᵢ + kFⱼ

no cambia el determinante.

Multiplicar una fila por k multiplica el determinante por k.

7. MATRIZ INVERTIBLE Y MATRIZ SINGULAR

Una matriz cuadrada A es invertible si existe A⁻¹ tal que:

AA⁻¹ = I

A⁻¹A = I

Si:

det(A) ≠ 0

A es invertible.

Si:

det(A) = 0

A es singular y no posee inversa.

8. INVERSA POR GAUSS-JORDAN

Para calcular A⁻¹ se construye:

[A | I]

y se aplican operaciones elementales hasta obtener:

[I | A⁻¹]

Si la parte izquierda no puede transformarse en I, A es
singular.

9. MATRIZ DE COFACTORES Y MATRIZ ADJUNTA

La matriz de cofactores de A se forma con todos los Cᵢⱼ.

La matriz adjunta se obtiene transponiendo la matriz de
cofactores:

adj(A) = Cᵀ

10. INVERSA POR MATRIZ ADJUNTA

Si det(A) ≠ 0:

A⁻¹ = (1 / det(A)) adj(A)

Este resultado debe coincidir con la inversa obtenida mediante
Gauss-Jordan.

11. PROPIEDADES DE LA MATRIZ INVERSA

Si A es invertible:

(A⁻¹)⁻¹ = A

Si A y B son invertibles:

(AB)⁻¹ = B⁻¹A⁻¹

Si A es invertible:

(Aᵀ)⁻¹ = (A⁻¹)ᵀ

Además:

det(A⁻¹) = 1 / det(A)

12. TEOREMA DE LA MATRIZ INVERTIBLE

Para una matriz cuadrada A de orden n × n son equivalentes,
entre otras, las siguientes afirmaciones:

- A es invertible.
- A es equivalente por filas a Iₙ.
- A tiene n posiciones pivote.
- Ax = 0 posee solamente la solución trivial.
- Las columnas de A son linealmente independientes.
- Las columnas de A generan ℝⁿ.
- Ax = b posee una solución para todo b en ℝⁿ.
- Aᵀ es invertible.
- det(A) ≠ 0.

Por ello, cuando det(A) ≠ 0, A tiene n posiciones pivote,
sus columnas son L.I. y generan ℝⁿ.

13. MÉTODO DE CRAMER

El método de Cramer permite resolver un sistema cuadrado:

Ax = b

cuando:

det(A) ≠ 0

Para cada variable xᵢ se construye una matriz Aᵢ sustituyendo
la columna i de A por el vector b.

Luego:

xᵢ = det(Aᵢ) / det(A)

Por ejemplo, para un sistema de dos variables:

x₁ = det(A₁) / det(A)

x₂ = det(A₂) / det(A)

Si det(A) = 0, el método de Cramer no puede utilizarse para
obtener una solución única.

La condición det(A) ≠ 0 también confirma que A es invertible
y que el sistema cuadrado posee una única solución.

========================================================
"""


def obtener_teoremas_modulo(numero_modulo):
    """Devuelve los teoremas correspondientes al número de módulo."""
    funciones = {
        1: obtener_teoremas_sistemas,
        2: obtener_teoremas_vectores,
        3: obtener_teoremas_matrices,
        4: obtener_teoremas_determinantes,
    }

    obtener_teoremas = funciones.get(
        numero_modulo
    )

    if obtener_teoremas is None:
        raise ValueError(
            "El número de módulo no es válido."
        )

    return obtener_teoremas()
