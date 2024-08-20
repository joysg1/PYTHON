import tkinter as tk
from matplotlib import pyplot as plt
import numpy as np

class MayorDeTresNumeros:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mayor de Tres Números")

        # Etiquetas y entradas para los números
        self.etiqueta_numero1 = tk.Label(self.ventana, text="Ingrese el primer número:")
        self.etiqueta_numero1.pack(padx=5, pady=5)
        self.entrada_numero1 = tk.Entry(self.ventana, width=10)
        self.entrada_numero1.pack(padx=5, pady=5)

        self.etiqueta_numero2 = tk.Label(self.ventana, text="Ingrese el segundo número:")
        self.etiqueta_numero2.pack(padx=5, pady=5)
        self.entrada_numero2 = tk.Entry(self.ventana, width=10)
        self.entrada_numero2.pack(padx=5, pady=5)

        self.etiqueta_numero3 = tk.Label(self.ventana, text="Ingrese el tercer número:")
        self.etiqueta_numero3.pack(padx=5, pady=5)
        self.entrada_numero3 = tk.Entry(self.ventana, width=10)
        self.entrada_numero3.pack(padx=5, pady=5)

        # Botón para verificar el mayor de los números
        self.boton_verificar = tk.Button(self.ventana, text="Verificar", command=self.verificar_numeros)
        self.boton_verificar.pack(padx=5, pady=5)

        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(self.ventana, text="")
        self.etiqueta_resultado.pack(padx=5, pady=5)

    def verificar_numeros(self):
        try:
            numero1 = float(self.entrada_numero1.get())
            numero2 = float(self.entrada_numero2.get())
            numero3 = float(self.entrada_numero3.get())

            numeros = [numero1, numero2, numero3]
            mayor = max(numeros)

            self.etiqueta_resultado.config(text=f"El mayor de los números es: {mayor}")

            # Calcular estadísticas
            promedio = np.mean(numeros)
            varianza = np.var(numeros)
            desviacion_estandar = np.std(numeros)

            # Generar gráfica
            plt.bar(["Número 1", "Número 2", "Número 3"], numeros)
            plt.xlabel("Número")
            plt.ylabel("Valor")
            plt.title("Gráfica de los Números")

            # Agregar etiquetas a las barras
            for i, numero in enumerate(numeros):
                plt.text(i, numero + 0.1, f"{numero:.2f}", ha="center")

            plt.text(0.5, 0.9, f"Promedio: {promedio:.2f}\nVarianza: {varianza:.2f}\nDesviación Estándar: {desviacion_estandar:.2f}", ha="center", transform=plt.gca().transAxes)
            plt.show()
        except ValueError:
            self.etiqueta_resultado.config(text="Error: ingresa valores numéricos")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    programa = MayorDeTresNumeros()
    programa.run()
