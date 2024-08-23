import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        # Entrada de texto para mostrar los números y resultados
        self.entrada = tk.Entry(self.ventana, width=35, borderwidth=5)
        self.entrada.grid(row=0, column=0, columnspan=4)

        # Botones de números y operadores
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        fila = 1
        columna = 0

        for boton in botones:
            tk.Button(self.ventana, text=boton, width=5, command=lambda boton=boton: self.click_boton(boton)).grid(row=fila, column=columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

        # Botón de limpiar
        tk.Button(self.ventana, text="C", width=21, command=self.limpiar).grid(row=fila, column=0, columnspan=4)

    def click_boton(self, boton):
        if boton == '=':
            try:
                resultado = eval(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except Exception as e:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Error")
        else:
            self.entrada.insert(tk.END, boton)

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()
