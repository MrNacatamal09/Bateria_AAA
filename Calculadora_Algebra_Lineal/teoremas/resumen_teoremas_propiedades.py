"""
Resume las propiedades matriciales consolidadas de la calculadora.
Agrupa operaciones, transpuesta, inversa y determinantes en una sección general.
Tema de clase: propiedades y teoremas fundamentales de matrices.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_propiedades():
    """Devuelve el resumen teórico de la sección Propiedades."""
    return """
============================================================
PROPIEDADES
Matrices, Transpuesta, Inversa y Determinantes
============================================================

1. OPERACIONES MATRICIALES

Siempre que las dimensiones sean compatibles:

A(BC) = (AB)C

A(B + C) = AB + AC

(B + C)A = BA + CA

r(AB) = (rA)B = A(rB)

IA = A = AI

La multiplicación matricial no es conmutativa en general:

AB ≠ BA


2. PROPIEDADES DE LA TRANSPUESTA

Para matrices compatibles:

(Aᵀ)ᵀ = A

(A + B)ᵀ = Aᵀ + Bᵀ

(rA)ᵀ = rAᵀ

(AB)ᵀ = BᵀAᵀ

También se verifica:

(r(A + B))ᵀ = rAᵀ + rBᵀ


3. PROPIEDADES DE LA MATRIZ INVERSA

Una matriz cuadrada A es invertible cuando existe A⁻¹ tal que:

A·A⁻¹ = I

A⁻¹·A = I

Por tanto:

A·A⁻¹ = I = A⁻¹·A

Si A es invertible:

(A⁻¹)⁻¹ = A

(Aᵀ)⁻¹ = (A⁻¹)ᵀ

Si A y B son invertibles:

(AB)⁻¹ = B⁻¹A⁻¹

Estas propiedades solamente son aplicables cuando las matrices
involucradas poseen inversa.


4. PROPIEDADES DEL DETERMINANTE

Para una matriz cuadrada A:

det(Aᵀ) = det(A)

Para matrices cuadradas A y B del mismo orden:

det(AB) = det(A)det(B)

Si A es invertible:

det(A⁻¹) = 1/det(A)

Si A es de orden n × n y r es un escalar:

det(rA) = rⁿdet(A)


5. OPERACIONES ELEMENTALES DE FILA

Intercambiar dos filas cambia el signo del determinante:

det(Fᵢ ↔ Fⱼ) = -det(A)

Reemplazar una fila mediante:

Fᵢ -> Fᵢ + rFⱼ

conserva el determinante:

det(B) = det(A)

Multiplicar una fila por r multiplica el determinante por r:

det(B) = r·det(A)


6. MATRIZ TRIANGULAR

Si A es triangular, entonces su determinante es el producto
de los elementos de su diagonal principal:

det(A) = a₁₁a₂₂...aₙₙ


7. VERIFICACIÓN DE PROPIEDADES

La calculadora recibe:

A
B
C
r

una sola vez.

A partir de esos datos se calculan las propiedades y se
comparan los miembros de cada igualdad.

Cada propiedad concluye con:

"Se cumple"

o:

"No se cumple"

Cuando una propiedad necesita una matriz invertible y la
hipótesis no se satisface, el resultado se indica como:

"No aplicable"


8. PROPIEDADES CONSOLIDADAS

La sección Propiedades verifica un total de 22 propiedades,
organizadas en las siguientes categorías:

- Operaciones matriciales.
- Transposición.
- Matriz inversa.
- Determinantes.
- Operaciones de fila.
- Matriz triangular.


9. ENCADENAMIENTO DE RESULTADOS

Los resultados intermedios se reutilizan dentro del cálculo.

Por ejemplo:

AB

se calcula una sola vez y puede utilizarse posteriormente en:

A(BC) = (AB)C

(AB)ᵀ = BᵀAᵀ

(AB)⁻¹ = B⁻¹A⁻¹

det(AB) = det(A)det(B)

De esta forma se evita volver a solicitar o calcular datos
que ya fueron obtenidos.


10. BÚSQUEDA Y FILTRADO

Después de calcular las propiedades, los resultados pueden
consultarse sin ejecutar nuevamente las operaciones.

La búsqueda permite utilizar:

- Número de propiedad.
- Nombre.
- Palabra parcial.
- Fórmula.
- Categoría.

Ejemplos:

13

inversa

A^-1

A⁻¹

A^T

Aᵀ

det(AB)

fila

triangular

============================================================
"""


def obtener_descripcion_propiedades():
    """Devuelve una descripción breve de la sección Propiedades."""
    return (
        "Verificación consolidada de propiedades matriciales, "
        "transpuesta, inversa y determinantes."
    )