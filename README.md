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


El código completo del ejercicio con su interfaz es:

```py
import tkinter as tk

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

class CalculadoraApp:
    def __init__(self, root): # Constructor
        self.root = root
        self.root.title("Calculadora")

        # Pantalla
        self.pantalla_var = tk.StringVar()
        pantalla = tk.Entry(root, textvariable=self.pantalla_var, font=('Arial', 18), bd=10, insertwidth=4, width=14,
                            justify='right')
        pantalla.grid(row=0, column=0, columnspan=4)

        # Botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 1, 4),  # El botón '=' ocupa 1 fila y 4 columnas
        ]

        for (text, row, col, *options) in botones:
            tk.Button(root, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, rowspan=options[0] if options else 1, columnspan=options[1] if options else 1)

        # Diccionario para mapear operadores a funciones
        self.operadores = {
            '+': suma,
            '-': resta,
            '*': multiplicacion,
            '/': division
        }

        # Variables para almacenar la operación actual y los operandos
        self.operacion_actual = ''
        self.operando1 = None

    def on_button_click(self, text):
        if text in self.operadores:
            # Si el texto es un operador, actualizar la operación actual y almacenar el operando
            self.operacion_actual = text
            self.operando1 = float(self.pantalla_var.get())
            self.pantalla_var.set('')
        elif text == '=':
            try:
                # Obtener el segundo operando
                operando2 = float(self.pantalla_var.get())
                
                # Realizar la operación usando la función correspondiente
                resultado = self.operadores[self.operacion_actual](self.operando1, operando2)

                # Mostrar el resultado en la pantalla
                self.pantalla_var.set(resultado)

                # Reiniciar las variables de operación
                self.operacion_actual = ''
                self.operando1 = None
            except Exception as e:
                # Manejo de errores, muestra 'Error' en la pantalla
                self.pantalla_var.set('Error')
        elif text == 'C':
            # Limpiar la pantalla y reiniciar las variables de operación
            self.pantalla_var.set('')
            self.operacion_actual = ''
            self.operando1 = None
        else:
            # Números y otros caracteres, simplemente agregan al texto actual
            current_text = self.pantalla_var.get()
            self.pantalla_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
```

Y la interfaz queda como:

<img src="https://github.com/Xavitheforce/Antipatrones/blob/main/img/calculadora.png">

El UML es:

<img src="https://github.com/Xavitheforce/Antipatrones/blob/main/img/UML_calculadora.png">


También se ha implementado en un django la calculadora.
