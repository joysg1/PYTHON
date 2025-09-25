import tkinter as tk
from tkinter import messagebox
import pydawiki
import pydawolframalpha

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscador Wolfram Alpha y Wikipedia")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Configurar el fondo
        self.root.configure(bg='#f0f0f0')
        
        # Título
        titulo = tk.Label(
            root, 
            text="Buscador Wolfram Alpha y Wikipedia",
            font=('Arial', 16, 'bold'),
            bg='#f0f0f0',
            fg='#333333'
        )
        titulo.pack(pady=20)
        
        # Frame para los botones
        frame_botones = tk.Frame(root, bg='#f0f0f0')
        frame_botones.pack(expand=True)
        
        # Botón para Wolfram Alpha
        btn_wolfram = tk.Button(
            frame_botones,
            text="🔍 Buscar en Wolfram Alpha",
            font=('Arial', 12),
            bg='#ff6b35',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            command=self.ejecutar_wolfram,
            cursor='hand2'
        )
        btn_wolfram.pack(pady=10, fill='x')
        
        # Botón para Wikipedia
        btn_wiki = tk.Button(
            frame_botones,
            text="📖 Buscar en Wikipedia",
            font=('Arial', 12),
            bg='#4285f4',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            command=self.ejecutar_wiki,
            cursor='hand2'
        )
        btn_wiki.pack(pady=10, fill='x')
        
        # Botón para salir
        btn_salir = tk.Button(
            frame_botones,
            text="❌ Salir",
            font=('Arial', 12),
            bg='#dc3545',
            fg='white',
            relief='flat',
            padx=20,
            pady=10,
            command=self.salir,
            cursor='hand2'
        )
        btn_salir.pack(pady=10, fill='x')
        
        # Efectos hover para los botones
        self.agregar_efectos_hover()
    
    def agregar_efectos_hover(self):
        """Agrega efectos hover a los botones"""
        def on_enter_wolfram(e):
            e.widget.configure(bg='#e55a2b')
        
        def on_leave_wolfram(e):
            e.widget.configure(bg='#ff6b35')
        
        def on_enter_wiki(e):
            e.widget.configure(bg='#3367d6')
        
        def on_leave_wiki(e):
            e.widget.configure(bg='#4285f4')
        
        def on_enter_salir(e):
            e.widget.configure(bg='#c82333')
        
        def on_leave_salir(e):
            e.widget.configure(bg='#dc3545')
        
        # Obtener referencias a los botones
        botones = self.root.winfo_children()[1].winfo_children()  # frame_botones children
        
        # Aplicar efectos a cada botón
        for i, boton in enumerate(botones):
            if i == 0:  # Wolfram
                boton.bind("<Enter>", on_enter_wolfram)
                boton.bind("<Leave>", on_leave_wolfram)
            elif i == 1:  # Wiki
                boton.bind("<Enter>", on_enter_wiki)
                boton.bind("<Leave>", on_leave_wiki)
            elif i == 2:  # Salir
                boton.bind("<Enter>", on_enter_salir)
                boton.bind("<Leave>", on_leave_salir)
    
    def ejecutar_wolfram(self):
        """Ejecuta la función de Wolfram Alpha"""
        try:
            messagebox.showinfo("Ejecutando", "Ejecutando búsqueda en Wolfram Alpha...")
            pydawolframalpha.buscar_en_wolframalpha()
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar Wolfram Alpha:\n{str(e)}")
    
    def ejecutar_wiki(self):
        """Ejecuta la función de Wikipedia"""
        try:
            messagebox.showinfo("Ejecutando", "Ejecutando búsqueda en Wikipedia...")
            pydawiki.buscar_en_wikipedia()
        except Exception as e:
            messagebox.showerror("Error", f"Error al ejecutar Wikipedia:\n{str(e)}")
    
    def salir(self):
        """Cierra la aplicación"""
        respuesta = messagebox.askyesno(
            "Confirmar salida", 
            "¿Estás seguro de que quieres salir?"
        )
        if respuesta:
            self.root.quit()

def main():
    """Función principal para ejecutar la aplicación"""
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()