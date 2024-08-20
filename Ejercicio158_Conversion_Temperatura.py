# Usando tkinter realiza un programa para convertir de celsius a fahrenheit y viceversa

import tkinter as tk

class ConversorTemperatura:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Conversor de Temperatura")

        # Etiqueta y entrada para la temperatura en Celsius
        self.etiqueta_celsius = tk.Label(self.ventana, text="Temperatura en Celsius:")
        self.etiqueta_celsius.grid(row=0, column=0, padx=5, pady=5)
        self.entrada_celsius = tk.Entry(self.ventana, width=10)
        self.entrada_celsius.grid(row=0, column=1, padx=5, pady=5)

        # Botón para convertir de Celsius a Fahrenheit
        self.boton_celsius_fahrenheit = tk.Button(self.ventana, text="Convertir a Fahrenheit", command=self.convertir_celsius_fahrenheit)
        self.boton_celsius_fahrenheit.grid(row=0, column=2, padx=5, pady=5)

        # Etiqueta para mostrar el resultado en Fahrenheit
        self.etiqueta_fahrenheit = tk.Label(self.ventana, text="Temperatura en Fahrenheit:")
        self.etiqueta_fahrenheit.grid(row=1, column=0, padx=5, pady=5)
        self.resultado_fahrenheit = tk.Label(self.ventana, text="")
        self.resultado_fahrenheit.grid(row=1, column=1, padx=5, pady=5)

        # Etiqueta y entrada para la temperatura en Fahrenheit
        self.etiqueta_fahrenheit_entrada = tk.Label(self.ventana, text="Temperatura en Fahrenheit:")
        self.etiqueta_fahrenheit_entrada.grid(row=2, column=0, padx=5, pady=5)
        self.entrada_fahrenheit = tk.Entry(self.ventana, width=10)
        self.entrada_fahrenheit.grid(row=2, column=1, padx=5, pady=5)

        # Botón para convertir de Fahrenheit a Celsius
        self.boton_fahrenheit_celsius = tk.Button(self.ventana, text="Convertir a Celsius", command=self.convertir_fahrenheit_celsius)
        self.boton_fahrenheit_celsius.grid(row=2, column=2, padx=5, pady=5)

        # Etiqueta para mostrar el resultado en Celsius
        self.etiqueta_celsius_resultado = tk.Label(self.ventana, text="Temperatura en Celsius:")
        self.etiqueta_celsius_resultado.grid(row=3, column=0, padx=5, pady=5)
        self.resultado_celsius = tk.Label(self.ventana, text="")
        self.resultado_celsius.grid(row=3, column=1, padx=5, pady=5)

    def convertir_celsius_fahrenheit(self):
        try:
            celsius = float(self.entrada_celsius.get())
            fahrenheit = celsius * 9/5 + 32
            self.resultado_fahrenheit.config(text=f"{fahrenheit:.2f}°F")
        except ValueError:
            self.resultado_fahrenheit.config(text="Error: ingresa un valor numérico")

    def convertir_fahrenheit_celsius(self):
        try:
            fahrenheit = float(self.entrada_fahrenheit.get())
            celsius = (fahrenheit - 32) * 5/9
            self.resultado_celsius.config(text=f"{celsius:.2f}°C")
        except ValueError:
            self.resultado_celsius.config(text="Error: ingresa un valor numérico")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    conversor = ConversorTemperatura()
    conversor.run()



