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
