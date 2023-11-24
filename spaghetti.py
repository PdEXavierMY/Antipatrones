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

import tkinter as tk

class CalculadoraApp:
    def __init__(self, root):
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

    def on_button_click(self, text):
        current_text = self.pantalla_var.get()

        if text == 'C':
            self.pantalla_var.set('')
        elif text == '=':
            try:
                result = eval(current_text)
                self.pantalla_var.set(result)
            except Exception as e:
                self.pantalla_var.set('Error')
        else:
            self.pantalla_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()