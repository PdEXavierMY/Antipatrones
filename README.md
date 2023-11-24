# Antipatrones

<h1>Ejercicio práctico: Identificación y refactorización de antipatrón "Spaghetti Code" en Python</h1>
Un antipatrón de programación es un patrón que puede ser considerado una mala práctica. "Spaghetti Code" es un antipatrón que se refiere a código con una estructura de control compleja, difícil de leer y seguir, generalmente debido a múltiples saltos de control, como instrucciones GOTO, ciclos y excepciones.

Enunciado del ejercicio

Dada una porción de código Python escrita en estilo "Spaghetti Code", se te pide que identifiques las principales características de este antipatrón y refactorices el código para mejorar su legibilidad y mantenibilidad.

Considera el siguiente fragmento de código:

```py
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```

Este código podría considerarse un ejemplo de "Spaghetti Code" debido a:

- **Falta de Estructura Modular:**
    - La función realiza múltiples tareas en una estructura lineal, sin una clara modularización.
    - Las diferentes operaciones están anidadas en múltiples declaraciones `if`, lo que hace que el código sea difícil de seguir.

- **Falta de Abstracción:**
    - La función no utiliza abstracciones adecuadas para las operaciones matemáticas, lo que puede hacer que sea difícil entender su propósito sin leer todo el código.

- **Manejo de Errores Inconsistente:**
    - La función maneja el caso de la división por cero imprimiendo un mensaje en lugar de lanzar una excepción. Esto puede hacer que sea difícil manejar este error de manera consistente en diferentes partes del programa.

- **Mensaje de Error Impreso:**
    - Imprimir mensajes de error directamente en la función puede no ser la mejor práctica, ya que limita la flexibilidad en el manejo de errores. En lugar de imprimir mensajes, sería mejor lanzar excepciones para que los llamadores de la función puedan decidir cómo manejar los errores.

- **Código Duplicado:**
    - Hay repeticiones en las verificaciones condicionales (`if operacion == ...`). Esto podría simplificarse para mejorar la legibilidad y el mantenimiento.

            <li>Hay repeticiones en las verificaciones condicionales (<code>if operacion == ...</code>). Esto podría simplificarse para mejorar la legibilidad y el mantenimiento.</li>
        </ul>
    </li>
</ul>

Ahora el nuevo código:

```py
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("No se puede dividir entre cero.")
```

## Cambios para Abordar Problemas de "Spaghetti Code"

### 1. Falta de Estructura Modular:
  
- **Cambio:** Se combinaron las funciones `suma`, `resta`, `multiplicacion`, y `division` en una única función `operar`.

- **Justificación:** Al agrupar todas las operaciones en una función única, se mejora la modularidad del código. Cada operación está encapsulada en una función única, facilitando la comprensión y el mantenimiento.

### 2. Falta de Abstracción:

- **Cambio:** Se introdujo la función `operar` con una interfaz más abstracta para realizar operaciones matemáticas.

- **Justificación:** La función `operar` abstrae el detalle de las operaciones, proporcionando una interfaz más clara y abstracta. Esto facilita la comprensión del propósito de la función sin necesidad de examinar el código interno.

### 3. Manejo de Errores Inconsistente:

- **Cambio:** Se reemplazó la impresión de mensajes de error con el lanzamiento de excepciones (`ValueError`).

- **Justificación:** Utilizar excepciones proporciona un manejo consistente de errores en todo el programa. Ahora, los errores se manejan de manera más predecible y se pueden gestionar de forma centralizada.

### 4. Mensaje de Error Impreso:

- **Cambio:** Se reemplazó la impresión de mensajes de error con el lanzamiento de excepciones (`ValueError`).

- **Justificación:** Lanzar excepciones en lugar de imprimir mensajes permite una mejor gestión de errores y proporciona flexibilidad al código cliente para manejar los errores de manera más efectiva.

### 5. Código Duplicado:

- **Cambio:** Se eliminó la repetición de verificaciones condicionales y se simplificó el código.

- **Justificación:** La eliminación de código duplicado mejora la legibilidad y facilita el mantenimiento. Al utilizar una estructura de selección (`if-elif-else`) en la función `operar`, se logra una implementación más eficiente y clara.

