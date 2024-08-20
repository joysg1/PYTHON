import tkinter as tk

class NumeroPositivoNegativo:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Número Positivo o Negativo")

        # Etiqueta y entrada para el número
        self.etiqueta_numero = tk.Label(self.ventana, text="Ingrese un número:")
        self.etiqueta_numero.pack(padx=5, pady=5)
        self.entrada_numero = tk.Entry(self.ventana, width=10)
        self.entrada_numero.pack(padx=5, pady=5)

        # Botón para verificar si el número es positivo o negativo
        self.boton_verificar = tk.Button(self.ventana, text="Verificar", command=self.verificar_numero)
        self.boton_verificar.pack(padx=5, pady=5)

        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(self.ventana, text="")
        self.etiqueta_resultado.pack(padx=5, pady=5)

    def verificar_numero(self):
        try:
            numero = float(self.entrada_numero.get())
            if numero > 0:
                self.etiqueta_resultado.config(text="El número es positivo", fg="green")
                self.ventana.config(bg="lightgreen")
            elif numero < 0:
                self.etiqueta_resultado.config(text="El número es negativo", fg="red")
                self.ventana.config(bg="lightcoral")
            else:
                self.etiqueta_resultado.config(text="El número es 0", fg="black")
                self.ventana.config(bg="white")
        except ValueError:
            self.etiqueta_resultado.config(text="Error: ingresa un valor numérico", fg="gray")
            self.ventana.config(bg="red")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    programa = NumeroPositivoNegativo()
    programa.run()
