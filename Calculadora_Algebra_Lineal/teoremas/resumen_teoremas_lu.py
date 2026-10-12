"""
Resume la teoría utilizada por el módulo de Factorización LU.
Incluye construcción de L y U, resolución de Ax=b y propiedades consolidadas.
Tema de clase: factorización LU, reducción y encadenamiento de resultados.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_lu():
    """Devuelve el resumen teórico del Módulo V."""
    return """
========================================================
MÓDULO V - FACTORIZACIÓN LU
========================================================

1. DEFINICIÓN DE FACTORIZACIÓN LU

La factorización LU expresa una matriz A como:

A = L·U

donde:

L = matriz triangular inferior unitaria.

U = forma escalonada obtenida a partir de A.

La matriz L contiene unos en su diagonal principal y guarda
los multiplicadores utilizados durante la eliminación.

2. CONSTRUCCIÓN DE U

La matriz U se obtiene reduciendo A mediante operaciones de
reemplazo de filas:

Fᵢ -> Fᵢ - lᵢⱼFⱼ

No se realizan intercambios de filas cuando se busca una
factorización directa:

A = LU

3. MULTIPLICADORES Y MATRIZ L

Cada entrada debajo de un pivote se elimina utilizando:

lᵢⱼ =
elemento a eliminar / pivote

El multiplicador lᵢⱼ debe almacenarse en L antes de modificar
la fila correspondiente de U.

Por ejemplo:

l₂₁ = a₂₁ / a₁₁

y la operación utilizada será:

F₂ -> F₂ - l₂₁F₁

4. ESTRUCTURA PARA MATRICES m × n

Si A tiene m filas y n columnas:

A es m × n

L es m × m

U es m × n

Por tanto:

A(m×n) = L(m×m) · U(m×n)

5. MATRIZ L

L es triangular inferior.

Su diagonal principal contiene unos:

lᵢᵢ = 1

Los elementos situados encima de la diagonal son cero.

Los elementos debajo de la diagonal son los multiplicadores
utilizados para construir U.

6. MATRIZ U

U es la forma escalonada obtenida mediante las operaciones
de reemplazo aplicadas a A.

La factorización debe satisfacer:

L·U = A

7. PIVOTE CERO Y PERMUTACIONES

Si el pivote necesario es cero y existe una entrada no nula
debajo, sería necesario realizar un intercambio de filas.

En ese caso no se continúa con una factorización directa
A = LU.

El programa debe informar:

"La matriz no admite Factorización LU sin permutación
(requiere pivoteo parcial PA = LU)."

Cuando interviene una matriz de permutación P:

PA = LU

8. RESOLUCIÓN DE Ax = b

Si:

A = LU

entonces:

Ax = b

puede escribirse como:

LUx = b

Se define:

Ux = y

por lo que el problema se divide en dos sistemas:

Ly = b

Ux = y

9. OBTENCIÓN DEL VECTOR y

Para resolver:

Ly = b

se construye la matriz aumentada:

[L | b]

El programa reutiliza el método de Gauss-Jordan desarrollado
anteriormente hasta obtener:

[I | y]

La última columna contiene el vector intermedio:

y

No se solicita al usuario que vuelva a ingresar L ni b.

10. OBTENCIÓN DEL VECTOR x

Una vez obtenido y se construye:

[U | y]

La matriz aumentada se reduce mediante Gauss-Jordan hasta:

[I | x]

La última columna contiene la solución final:

x

El vector y se transfiere directamente desde el resultado
anterior sin solicitar nuevamente sus componentes.

11. VERIFICACIÓN DE LA FACTORIZACIÓN

Una vez obtenidas L y U se calcula:

L·U

utilizando la función de producto matricial desarrollada en
la Calculadora.

La factorización es correcta cuando:

L·U = A

12. VERIFICACIÓN DE LA SOLUCIÓN

Después de calcular x se verifica:

A·x = b

Si ambos vectores son iguales, la solución obtenida es
correcta.

13. ENCADENAMIENTO DE RESULTADOS

Los resultados intermedios se almacenan en listas anidadas y
se envían directamente a otras funciones.

El flujo es:

A
↓
Factorización LU
↓
L y U
↓
[L|b]
↓
y
↓
[U|y]
↓
x
↓
A·x
↓
comparación con b

No se vuelven a pedir al usuario:

L
U
y
x

14. VENTAJA DE LA FACTORIZACIÓN LU

Si la matriz A permanece fija y se desean resolver varios
sistemas con distintos vectores b:

Ax₁ = b₁
Ax₂ = b₂
Ax₃ = b₃

la factorización:

A = LU

se realiza una sola vez.

Para cada nuevo vector b únicamente deben resolverse:

Ly = b

Ux = y

15. PROPIEDADES DE OPERACIONES MATRICIALES

El verificador consolidado reutiliza las funciones internas
del proyecto para comprobar:

A(BC) = (AB)C

A(B + C) = AB + AC

(B + C)A = BA + CA

r(AB) = (rA)B = A(rB)

IA = A = AI

16. PROPIEDADES DE LA TRANSPUESTA

(Aᵀ)ᵀ = A

(A + B)ᵀ = Aᵀ + Bᵀ

(rA)ᵀ = rAᵀ

(AB)ᵀ = BᵀAᵀ

Además:

(r(A + B))ᵀ = rAᵀ + rBᵀ

17. PROPIEDADES DE LA MATRIZ INVERSA

Si A es invertible:

(A⁻¹)⁻¹ = A

(Aᵀ)⁻¹ = (A⁻¹)ᵀ

A·A⁻¹ = I

A⁻¹·A = I

Por tanto:

A·A⁻¹ = I = A⁻¹·A

Si A y B son invertibles:

(AB)⁻¹ = B⁻¹A⁻¹

18. PROPIEDADES DEL DETERMINANTE

det(Aᵀ) = det(A)

det(AB) = det(A)det(B)

Si A es invertible:

det(A⁻¹) = 1/det(A)

Para A de orden n × n:

det(rA) = rⁿdet(A)

19. DETERMINANTE Y OPERACIONES DE FILA

Intercambiar dos filas cambia el signo:

det(B) = -det(A)

Reemplazar una fila mediante:

Fᵢ -> Fᵢ + kFⱼ

conserva el determinante.

Multiplicar una fila por k multiplica el determinante por k.

20. DETERMINANTE DE UNA MATRIZ TRIANGULAR

Si A es triangular:

det(A)

es el producto de los elementos de su diagonal principal.

El programa compara este resultado con el determinante
obtenido mediante los métodos anteriores.

21. PROPIEDADES CONSOLIDADAS

El módulo calcula las propiedades una sola vez y conserva sus
resultados en memoria.

Posteriormente pueden filtrarse por:

- Número.
- Nombre.
- Palabra parcial.
- Fórmula.
- Categoría.

Filtrar los resultados no vuelve a ejecutar determinantes,
inversas ni productos matriciales.

22. CATEGORÍAS DEL VERIFICADOR

Las propiedades se organizan en:

- Operaciones matriciales.
- Transposición.
- Matriz inversa.
- Determinantes.
- Operaciones de fila.
- Matriz triangular.

Cada propiedad muestra sus dos miembros, o tres miembros
cuando corresponde, y concluye:

"Se cumple"

o:

"No se cumple"

Si una propiedad de inversa no puede aplicarse porque la
matriz es singular, el programa informa:

"No aplicable"

========================================================
"""