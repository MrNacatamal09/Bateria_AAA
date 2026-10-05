"""
Reúne los teoremas y propiedades usados por los módulos de la calculadora.
Proporciona textos de consulta para sistemas, vectores, matrices y determinantes.
Tema de clase: fundamentos y teoremas principales de Álgebra Lineal.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_sistemas():
    """Devuelve los teoremas clave del módulo de sistemas de ecuaciones."""
    return """
========================================================
MÓDULO 1 - SISTEMAS DE ECUACIONES LINEALES
========================================================

1. OPERACIONES ELEMENTALES POR FILAS

Las operaciones elementales por filas permiten transformar
una matriz en otra equivalente sin cambiar el conjunto de
soluciones del sistema.

Las operaciones permitidas son:

- Intercambiar dos filas.
- Multiplicar una fila por un escalar distinto de cero.
- Sumar a una fila un múltiplo de otra fila.


2. SISTEMAS EQUIVALENTES

Dos sistemas de ecuaciones son equivalentes cuando poseen
el mismo conjunto de soluciones.

Por esta razón, las operaciones elementales pueden utilizarse
para transformar un sistema complicado en otro más sencillo.


3. SISTEMA CONSISTENTE DETERMINADO

Un sistema es consistente determinado cuando posee una única
solución.

En su forma escalonada reducida existe un pivote para cada
variable y no existen variables libres.


4. SISTEMA CONSISTENTE INDETERMINADO

Un sistema es consistente indeterminado cuando posee infinitas
soluciones.

Esto ocurre cuando existe al menos una variable libre y no
aparece ninguna contradicción en el sistema.


5. SISTEMA INCONSISTENTE

Un sistema es inconsistente cuando no posee solución.

En la matriz aumentada reducida puede aparecer una fila de la
forma:

[ 0  0  ...  0 | b ]

donde b es diferente de cero.


6. VARIABLES BÁSICAS

Las variables básicas son aquellas asociadas con columnas que
contienen pivotes.


7. VARIABLES LIBRES

Las variables libres son aquellas cuyas columnas no contienen
pivote.

Normalmente se representan mediante parámetros como:

t₁, t₂, t₃, ...


8. FORMA ESCALONADA REDUCIDA POR FILAS

Una matriz está en forma escalonada reducida cuando:

- Cada pivote es igual a 1.
- Cada pivote es el único valor distinto de cero de su columna.
- Los pivotes avanzan hacia la derecha.
- Las filas nulas quedan en la parte inferior.


9. MÉTODO DE GAUSS

El método de Gauss transforma la matriz aumentada hasta
obtener una forma escalonada.


10. MÉTODO DE GAUSS-JORDAN

Gauss-Jordan continúa la reducción hasta obtener la forma
escalonada reducida por filas.

Permite identificar directamente:

- Pivotes.
- Variables básicas.
- Variables libres.
- Solución del sistema.

========================================================
"""


def obtener_teoremas_vectores():
    """Devuelve los teoremas clave del módulo de vectores."""
    return """
========================================================
MÓDULO 2 - VECTORES E INDEPENDENCIA LINEAL
========================================================

1. COMBINACIÓN LINEAL

Un vector b es combinación lineal de los vectores

v₁, v₂, ..., vₖ

si existen escalares

c₁, c₂, ..., cₖ

tales que:

c₁v₁ + c₂v₂ + ... + cₖvₖ = b


2. ECUACIÓN MATRICIAL Ax = b

Si los vectores se colocan como columnas de una matriz A,
la combinación lineal puede escribirse como:

Ax = b


3. SISTEMA HOMOGÉNEO

Un sistema es homogéneo cuando tiene la forma:

Ax = 0

Todo sistema homogéneo posee al menos la solución trivial.


4. SOLUCIÓN TRIVIAL

La solución trivial es:

x₁ = 0
x₂ = 0
...
xₖ = 0


5. SOLUCIÓN NO TRIVIAL

Una solución es no trivial cuando al menos uno de sus
coeficientes es diferente de cero.


6. INDEPENDENCIA LINEAL

Un conjunto de vectores

v₁, v₂, ..., vₖ

es linealmente independiente si:

c₁v₁ + c₂v₂ + ... + cₖvₖ = 0

solamente posee la solución:

c₁ = c₂ = ... = cₖ = 0


7. DEPENDENCIA LINEAL

Un conjunto es linealmente dependiente cuando la ecuación

c₁v₁ + c₂v₂ + ... + cₖvₖ = 0

posee una solución no trivial.


8. CRITERIO MEDIANTE VARIABLES LIBRES

Si al reducir Ax = 0:

- No existen variables libres:
  los vectores son linealmente independientes.

- Existe al menos una variable libre:
  los vectores son linealmente dependientes.


9. CRITERIO MEDIANTE PIVOTES

Si A tiene una columna por cada vector:

- Un pivote en cada columna:
  vectores linealmente independientes.

- Alguna columna sin pivote:
  vectores linealmente dependientes.


10. RELACIÓN ENTRE COLUMNAS DE A

Si:

A = [ v₁  v₂  ...  vₖ ]

entonces:

Ax = 0

representa:

x₁v₁ + x₂v₂ + ... + xₖvₖ = 0

========================================================
"""


def obtener_teoremas_matrices():
    """Devuelve los teoremas requeridos para el Módulo III y Programa 5."""
    return """
========================================================
MÓDULO 3 - ÁLGEBRA DE MATRICES
PROGRAMA 5
========================================================

1. IGUALDAD DE MATRICES

Dos matrices son iguales si poseen las mismas dimensiones y
sus entradas correspondientes son iguales.


2. SUMA Y RESTA DE MATRICES

A + B y A - B están definidas solamente cuando A y B poseen
las mismas dimensiones.

Las operaciones se realizan entrada por entrada.


3. MULTIPLICACIÓN POR ESCALAR

Si r es un escalar y A = [aᵢⱼ], entonces:

rA = [raᵢⱼ]

El escalar multiplica cada entrada de la matriz.


4. MULTIPLICACIÓN DE MATRICES

Si A tiene dimensión m × n y B tiene dimensión n × p,
entonces AB está definido y posee dimensión:

m × p

Cada entrada se obtiene mediante la regla fila-columna:

(AB)ᵢⱼ =
aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + ... + aᵢₙbₙⱼ

Por tanto, para calcular AB debe cumplirse:

Columnas de A = Filas de B


5. PROPIEDADES DE LA MULTIPLICACIÓN

Siempre que las operaciones estén definidas:

A(BC) = (AB)C

A(B + C) = AB + AC

(B + C)A = BA + CA

r(AB) = (rA)B = A(rB)

IₙA = A = AIₙ


6. LA MULTIPLICACIÓN NO ES CONMUTATIVA EN GENERAL

En general:

AB ≠ BA

Por tanto, el orden de los factores matriciales no puede
intercambiarse libremente.


7. TRANSPUESTA

Si A tiene dimensión m × n, entonces Aᵀ tiene dimensión n × m.

Las filas de A se convierten en las columnas de Aᵀ.

Propiedades:

(Aᵀ)ᵀ = A

(A + B)ᵀ = Aᵀ + Bᵀ

(rA)ᵀ = rAᵀ

(AB)ᵀ = BᵀAᵀ


8. DETERMINANTE

El determinante está definido para matrices cuadradas.

Para una matriz de orden 2:

A = [ a  b ]
    [ c  d ]

se tiene:

det(A) = ad - bc

Para matrices de mayor orden puede utilizarse el desarrollo
por cofactores.


9. MENOR Y COFACTOR

El menor Mᵢⱼ se obtiene eliminando la fila i y la columna j.

El cofactor correspondiente es:

Cᵢⱼ = (-1)^(i+j) det(Mᵢⱼ)


10. DESARROLLO POR COFACTORES

El determinante puede desarrollarse por cualquier fila o
columna.

Por una fila i:

det(A) =
aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢₙCᵢₙ


11. REGLA DE SARRUS

Para una matriz de orden 3 × 3 también puede utilizarse la
regla de Sarrus.

Este método es exclusivo para matrices 3 × 3.


12. DETERMINANTE DE UNA MATRIZ TRIANGULAR

Si A es triangular, entonces:

det(A) = a₁₁a₂₂ ... aₙₙ

Es decir, el determinante es el producto de las entradas
de la diagonal principal.


13. OPERACIONES DE FILA Y DETERMINANTE

El intercambio de dos filas cambia el signo del determinante.

Si:

A -> B

mediante un intercambio de dos filas, entonces:

det(B) = -det(A)

Sumar a una fila un múltiplo de otra no modifica el
determinante:

Fᵢ -> Fᵢ + kFⱼ

det(B) = det(A)

Multiplicar una fila por k multiplica el determinante por k:

Fᵢ -> kFᵢ

det(B) = k det(A)


14. MATRIZ INVERTIBLE

Una matriz cuadrada A es invertible si existe una matriz
A⁻¹ tal que:

AA⁻¹ = I

y

A⁻¹A = I


15. INVERSA Y DETERMINANTE

Una matriz cuadrada A es invertible si y solo si:

det(A) ≠ 0

Si:

det(A) = 0

la matriz es singular y no posee inversa.


16. INVERSA POR GAUSS-JORDAN

Para obtener la inversa mediante Gauss-Jordan se construye:

[A | I]

y se aplican operaciones elementales por filas.

Si A es invertible, se obtiene:

[I | A⁻¹]

Si no aparecen n posiciones pivote, la matriz es singular.


17. MATRIZ DE COFACTORES Y MATRIZ ADJUNTA

La matriz de cofactores de A contiene los valores Cᵢⱼ.

La matriz adjunta se obtiene transponiendo la matriz de
cofactores:

adj(A) = Cᵀ


18. INVERSA POR MATRIZ ADJUNTA

Si:

det(A) ≠ 0

entonces:

A⁻¹ = (1/det(A)) adj(A)

Esta fórmula solamente puede aplicarse cuando el determinante
es distinto de cero.


19. PROPIEDADES DE MATRICES INVERTIBLES

Si A es invertible:

(A⁻¹)⁻¹ = A

Si A y B son invertibles:

(AB)⁻¹ = B⁻¹A⁻¹

Si A es invertible:

(Aᵀ)⁻¹ = (A⁻¹)ᵀ


20. DETERMINANTE DE LA INVERSA

Si A es invertible:

det(A⁻¹) = 1/det(A)


21. TEOREMA DE LA MATRIZ INVERTIBLE

Sea A una matriz cuadrada de orden n × n.

Las siguientes afirmaciones son equivalentes:

- A es invertible.
- A es equivalente por filas a Iₙ.
- A tiene n posiciones pivote.
- Ax = 0 posee solamente la solución trivial.
- Las columnas de A son linealmente independientes.
- Ax = b posee una solución para cada b en ℝⁿ.
- Las columnas de A generan ℝⁿ.

En particular, para el Programa 5 se utilizan directamente
las siguientes caracterizaciones:

c) A tiene n posiciones pivote.

e) Las columnas de A son linealmente independientes.

h) Las columnas de A generan ℝⁿ.


22. RELACIÓN ENTRE LAS CONDICIONES DE INVERTIBILIDAD

Para una matriz cuadrada A de orden n × n, las siguientes
condiciones describen la misma situación:

det(A) ≠ 0

A tiene n posiciones pivote.

Las columnas de A son L.I.

Las columnas de A generan ℝⁿ.

A posee una matriz inversa.

Por tanto, si una de estas condiciones falla, A no es
invertible.

========================================================
"""


def obtener_teoremas_determinantes():
    """Devuelve los teoremas clave del módulo de determinantes."""
    return """
========================================================
MÓDULO 4 - DETERMINANTES
========================================================

1. DETERMINANTE DE UNA MATRIZ 2 × 2

Sea:

A = [ a  b ]
    [ c  d ]

Entonces:

det(A) = ad - bc


2. MENOR DE UNA MATRIZ

Sea A una matriz n × n.

El menor Mᵢⱼ se obtiene eliminando de A:

- La fila i.
- La columna j.

El resultado es una matriz de orden:

(n - 1) × (n - 1)


3. COFACTOR

El cofactor correspondiente a la posición (i, j) se obtiene
mediante:

Cᵢⱼ = (-1)^(i+j) det(Mᵢⱼ)


4. SIGNOS DE LOS COFACTORES

El signo depende de i + j:

Si i + j es par:

(-1)^(i+j) = 1

Si i + j es impar:

(-1)^(i+j) = -1


5. DESARROLLO POR COFACTORES

El determinante de una matriz cuadrada puede calcularse
desarrollando por una fila o por una columna.

Por una fila i:

det(A) =
aᵢ₁Cᵢ₁ + aᵢ₂Cᵢ₂ + ... + aᵢₙCᵢₙ

El proceso continúa calculando los determinantes de los
menores correspondientes.


6. ELECCIÓN DE FILA O COLUMNA

Al desarrollar por cofactores es conveniente seleccionar una
fila o columna que contenga la mayor cantidad posible de
ceros.

Los términos asociados con elementos iguales a cero no
aportan al determinante y pueden omitirse.


7. RELACIÓN CON LA INVERSA EN EL CASO 2 × 2

Para:

A = [ a  b ]
    [ c  d ]

si:

det(A) = ad - bc ≠ 0

la matriz es invertible.

Si:

det(A) = 0

la matriz no es invertible.


8. PROCEDIMIENTO UTILIZADO POR LA CALCULADORA

Para calcular un determinante por cofactores la calculadora:

1. Verifica que la matriz sea cuadrada.
2. Busca una fila o columna conveniente.
3. Obtiene cada menor Mᵢⱼ.
4. Calcula det(Mᵢⱼ).
5. Aplica el signo (-1)^(i+j).
6. Obtiene el cofactor Cᵢⱼ.
7. Multiplica el elemento por su cofactor.
8. Suma los términos del desarrollo.

========================================================
"""


def obtener_teoremas_modulo(numero_modulo):
    """Devuelve los teoremas correspondientes al número de módulo recibido."""
    if numero_modulo == 1:
        return obtener_teoremas_sistemas()

    if numero_modulo == 2:
        return obtener_teoremas_vectores()

    if numero_modulo == 3:
        return obtener_teoremas_matrices()

    if numero_modulo == 4:
        return obtener_teoremas_determinantes()

    raise ValueError(
        "El número de módulo no es válido."
    )