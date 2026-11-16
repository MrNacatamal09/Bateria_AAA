"""Resume la teoría del Programa 8 para la calculadora de Álgebra Lineal.

Tema de clase: métodos iterativos de Jacobi y Gauss-Seidel para Ax = b.
Elaborado por: Alexa Loaisiga, Adolfo Ramírez y Andy Díaz.
"""


def obtener_teoremas_iterativos() -> str:
    """Devuelve los conceptos necesarios para interpretar ambos métodos."""
    return """
========================================================
MÓDULO 7 - MÉTODOS ITERATIVOS · PROGRAMA 8
========================================================

1. SISTEMAS Y APROXIMACIONES

Los métodos iterativos buscan una solución aproximada de
Ax = b. Parten de un vector inicial x⁽⁰⁾ y producen una
sucesión x⁽¹⁾, x⁽²⁾, ... sin reducir A por filas en cada paso.

2. MÉTODO DE JACOBI

Cada componente nueva se calcula con los valores de la
iteración anterior:

xᵢ⁽ᵏ⁺¹⁾ = (bᵢ - Σⱼ≠ᵢ aᵢⱼxⱼ⁽ᵏ⁾) / aᵢᵢ

Todas las componentes se actualizan simultáneamente. Ningún
valor recién calculado se usa dentro de la misma iteración.

3. MÉTODO DE GAUSS-SEIDEL

Al calcular la componente i se utilizan de inmediato las
componentes nuevas anteriores y se conservan las antiguas
para las posteriores:

xᵢ⁽ᵏ⁺¹⁾ = (bᵢ - Σⱼ<ᵢ aᵢⱼxⱼ⁽ᵏ⁺¹⁾
                - Σⱼ>ᵢ aᵢⱼxⱼ⁽ᵏ⁾) / aᵢᵢ

Esta actualización inmediata es la diferencia esencial con
Jacobi. El número de iteraciones de cada método se observa
en los resultados, no se supone de antemano.

4. DIAGONAL Y REORDENAMIENTO

Cada aᵢᵢ debe ser distinto de cero para poder dividir. Una
permutación de ecuaciones puede colocar coeficientes no nulos
en la diagonal. Al intercambiar filas de A también deben
intercambiarse las entradas correspondientes de b; así se
conserva el mismo sistema de ecuaciones.

Si no existe una permutación adecuada, no se ejecutan los
métodos con una diagonal inválida.

5. DOMINANCIA DIAGONAL ESTRICTA

A es estrictamente diagonal dominante por filas cuando, para
cada fila i:

|aᵢᵢ| > Σⱼ≠ᵢ |aᵢⱼ|

Esta condición es suficiente para garantizar convergencia de
Jacobi y Gauss-Seidel; no es necesaria. Si no se cumple, los
métodos aún pueden converger. Su ausencia por sí sola no
demuestra divergencia.

6. ERROR, TOLERANCIA Y PARADA

Ambos métodos usan el mismo error entre iteraciones:

Eₖ = ||x⁽ᵏ⁾ - x⁽ᵏ⁻¹⁾||∞
   = maxᵢ |xᵢ⁽ᵏ⁾ - xᵢ⁽ᵏ⁻¹⁾|

El criterio principal de parada se cumple cuando Eₖ ≤ ε,
con ε > 0. También se detienen al alcanzar el máximo de
iteraciones. Llegar al máximo indica que no se verificó la
tolerancia solicitada, no demuestra por sí solo divergencia.

7. RESIDUO Y VALIDACIÓN

Para comprobar la aproximación obtenida se calcula:

R = ||Ax - b||∞ = maxᵢ |(Ax)ᵢ - bᵢ|

Un residuo pequeño indica que x satisface aproximadamente el
sistema. Cuando existe solución única, la reducción previa
por Gauss-Jordan ofrece una referencia independiente para
comparar las aproximaciones iterativas.

8. POSIBLE NO CONVERGENCIA

Errores crecientes de forma sostenida o valores no finitos
requieren una advertencia prudente. Un único aumento del
error, o la falta de dominancia estricta, no basta para afirmar
que el método diverge.

========================================================
"""
