import customtkinter
from tkinter import messagebox
import tkinter as tk

# Configuración de CustomTkinter
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Crear la ventana principal
app = customtkinter.CTk()
app.geometry("400x600")
app.title("Ciclos Repetitivos en Arduino")

# Crear los elementos de la interfaz
label_ciclos = customtkinter.CTkLabel(master=app, text="Ciclos Repetitivos en Arduino", font=("Arial", 24))
label_ciclos.pack(pady=10)

# Crear una ventana para el combobox de los ciclos
ciclos_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
ciclos_frame.pack(pady=5)

ciclos_options = ["For", "While", "Do-While"]
ciclos_listbox = customtkinter.CTkComboBox(master=ciclos_frame, values=ciclos_options, font=("Arial", 12))
ciclos_listbox.pack(pady=5)

# Crear una ventana para mostrar la información del ciclo seleccionado
info_frame = customtkinter.CTkFrame(master=app, corner_radius=10)
info_frame.pack(pady=10)

info_label = customtkinter.CTkLabel(master=info_frame, text="", justify=tk.CENTER, font=("Courier New", 18))
info_label.pack(padx=20, pady=20)

def mostrar_info_ciclo():
    """Muestra la información del ciclo seleccionado."""
    try:
        ciclo = ciclos_listbox.get()
        if not ciclo:
            messagebox.showerror("Error", "Por favor, seleccione un ciclo.")
            return
        
        if ciclo == "For":
            info_label.configure(text="El ciclo for se utiliza para repetir un bloque de código un número determinado de veces.\n\nEjemplo:\n```c\nfor (int i = 0; i < 10; i++) {\n  // código a ejecutar\n}\n```", font=("Courier New", 18))
        elif ciclo == "While":
            info_label.configure(text="El ciclo while se utiliza para repetir un bloque de código mientras se cumpla una condición.\n\nEjemplo:\n```c\nint i = 0;\nwhile (i < 10) {\n  // código a ejecutar\n  i++;\n}\n```", font=("Courier New", 18))
        elif ciclo == "Do-While":
            info_label.configure(text="El ciclo do-while se utiliza para repetir un bloque de código mientras se cumpla una condición.\n\nEjemplo:\n```c\nint i = 0;\ndo {\n  // código a ejecutar\n  i++;\n} while (i < 10);\n```", font=("Courier New", 18))
    except Exception as e:
        messagebox.showerror("Error", f"Se produjo un error: {str(e)}")

button_mostrar_info = customtkinter.CTkButton(master=app, text="Mostrar Información del Ciclo", command=mostrar_info_ciclo,
                                         font=("Arial", 18))
button_mostrar_info.pack(pady=15)

# Ejecutar la aplicación
app.mainloop()



