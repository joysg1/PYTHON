import customtkinter
from tkinter import messagebox
import tkinter as tk  # Importar tkinter para usar tk.CENTER

# Configuración de CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Crear la ventana principal
app = customtkinter.CTk()
app.geometry("400x500")
app.title("Dibujador de Pirámides")

# Crear los elementos de la interfaz
label_lineas = customtkinter.CTkLabel(master=app, text="Ingrese el número de líneas:", font=("Arial", 12))
label_lineas.pack(pady=10)

entry_lineas = customtkinter.CTkEntry(master=app, font=("Arial", 12))
entry_lineas.pack()

piramide_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
piramide_frame.pack(pady=10)

piramide_label = customtkinter.CTkLabel(master=piramide_frame, text="", justify=tk.CENTER, font=("Courier New", 12))
piramide_label.pack(padx=20, pady=20)

def generar_piramide():
    """Genera y muestra la pirámide según el número de líneas ingresadas."""
    try:
        lineas = int(entry_lineas.get())
        
        if lineas > 0:
            piramide = ""
            for i in range(lineas):
                # Crear cada línea de la pirámide con el número adecuado de asteriscos y espacios
                piramide += " " * (lineas - i - 1) + "*" * (2 * i + 1) + "\n"
            piramide_label.configure(text=piramide)  # Usa configure en lugar de config
        else:
            messagebox.showerror("Error", "El número de líneas debe ser un entero positivo.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

button_generar = customtkinter.CTkButton(master=app, text="Generar Pirámide", command=generar_piramide,
                                       font=("Arial", 12))
button_generar.pack(pady=15)

app.mainloop()
