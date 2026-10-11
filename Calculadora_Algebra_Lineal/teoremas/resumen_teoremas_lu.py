"""
Resume la teoría utilizada por el módulo de Factorización LU.
Incluye construcción de L y U, sustituciones, validaciones y propiedades.
Tema de clase: factorización LU y resolución eficiente de sistemas.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_lu():
    """Devuelve el resumen teórico del Módulo V."""
    return """
========================================================
MÓDULO V - FACTORIZACIÓN LU
========================================================

1. DEFINICIÓN

La factorización LU expresa una matriz A como:

A = L·U

donde:

L = matriz triangular inferior unitaria.
U = forma escalonada obtenida a partir de A.

La diagonal principal de L contiene unos.

2. CONSTRUCCIÓN DE U

U se obtiene reduciendo A mediante operaciones de
reemplazo de filas:

Fᵢ -> Fᵢ - mᵢⱼFⱼ

No se realizan intercambios de filas en la factorización
A = LU usada en este módulo.

3. MULTIPLICADORES Y MATRIZ L

Cada multiplicador utilizado para eliminar una entrada se
guarda en L.

Si el pivote es p y la entrada que se desea eliminar es a:

m = a / p

Ese valor se coloca en la posición correspondiente debajo
de la diagonal principal de L.

4. ESTRUCTURA PARA MATRICES m × n

Si A tiene m filas y n columnas:

L tiene tamaño m × m.

U tiene tamaño m × n.

Por tanto:

A(m×n) = L(m×m) · U(m×n)

5. PIVOTE CERO

Si durante la reducción la entrada pivote es cero y existe
una entrada no nula debajo, se necesita intercambiar filas.

En ese caso ya no se trabaja directamente con:

A = LU

sino con una factorización con permutación:

PA = LU

donde P es una matriz de permutación.

6. RESOLUCIÓN DE Ax = b

Si:

A = LU

entonces:

Ax = b

se convierte en:

L(Ux) = b

Se define:

Ux = y

y el problema se resuelve en dos etapas:

Ly = b
Ux = y

7. SUSTITUCIÓN HACIA ADELANTE

Como L es triangular inferior, Ly = b se resuelve desde la
primera ecuación hacia la última.

El resultado es el vector intermedio:

y

8. SUSTITUCIÓN HACIA ATRÁS

Como U es triangular superior, Ux = y se resuelve desde la
última ecuación hacia la primera.

El resultado final es:

x

9. VERIFICACIONES

La factorización debe comprobar:

L·U = A

La solución del sistema debe comprobar:

A·x = b

10. VENTAJA DE LU

Si A permanece fija y cambian distintos vectores b, la
factorización A = LU se calcula una sola vez.

Para cada nuevo b solamente se resuelven:

Ly = b
Ux = y

11. ENCADENAMIENTO DE RESULTADOS

Las matrices obtenidas por una función se conservan como
listas anidadas y se pasan directamente a las siguientes
funciones.

Ejemplo:

A -> factorizar -> L y U
L y b -> y
U y y -> x
A y x -> comprobación

No es necesario volver a ingresar L, U, y ni x.

12. PROPIEDADES CONSOLIDADAS

El módulo reutiliza las operaciones desarrolladas
anteriormente para verificar propiedades de:

- Operaciones matriciales.
- Producto matricial.
- Transpuesta.
- Matriz inversa.
- Determinantes.
- Operaciones elementales por filas.

Entre ellas:

(AB)ᵀ = BᵀAᵀ

(AB)⁻¹ = B⁻¹A⁻¹

det(Aᵀ) = det(A)

det(AB) = det(A)det(B)

det(A⁻¹) = 1/det(A)

========================================================
"""
