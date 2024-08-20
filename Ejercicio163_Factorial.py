import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox

def factorial(n):
    """Calcula el factorial de un número.

    Args:
        n: El número cuyo factorial se calculará.

    Returns:
        El factorial de n.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calcular_y_graficar():
    try:
        # Obtener el número ingresado por el usuario
        numero = int(entry_numero.get())
        if numero < 0:
            messagebox.showerror("Error", "Por favor, ingrese un número entero no negativo.")
            return

        # Generar los datos para la gráfica
        numeros = np.arange(0, numero + 1)
        factoriales = [factorial(num) for num in numeros]

        # Crear la gráfica lineal con marcadores
        plt.figure(figsize=(12, 8))  # Aumentar el tamaño de la figura
        plt.plot(numeros, factoriales, marker='o', label='Factorial')
        plt.xlabel('Número')
        plt.ylabel('Factorial')
        plt.title(f'Crecimiento del factorial hasta {numero}')
        plt.grid(True)

        # Agregar leyenda
        plt.legend()

        # Agregar etiquetas a algunos puntos, rotándolas y ajustando la posición
        for i in range(0, len(numeros), 5):
            plt.annotate(str(factoriales[i]), (numeros[i], factoriales[i]), 
                         textcoords="offset points", xytext=(5, 10), ha='center', rotation=45,
                         fontsize=10)

        plt.tight_layout()  # Ajustar automáticamente los márgenes
        plt.show()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número entero válido.")
    except OverflowError:
        messagebox.showerror("Error", "El factorial del número ingresado es demasiado grande.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Factorial y Gráfica Lineal")

# Crear un label y un campo de entrada para el número
label_numero = tk.Label(ventana, text="Ingrese un número:")
label_numero.pack()
entry_numero = tk.Entry(ventana)
entry_numero.pack()

# Crear un botón para iniciar el cálculo y generar la gráfica
boton = tk.Button(ventana, text="Calcular y Graficar", command=calcular_y_graficar)
boton.pack()

ventana.mainloop()