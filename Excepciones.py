import os

# Ejemplo #1 dividir entre 0

numero1 = 45
numero2 = 20

try:
  resultado = numero1 / numero2
except:
    resultado = "indeterminado"
    print(f"Error el numero2 es igual a = {numero2} por ende la division no puede llevarse a cabo")
finally:
    print("Esta seccion del codigo siempre se ejecuta")
    print(f"Resultado de dividir {numero1} / {numero2} = {resultado}")  
    
    
# Ejemplo #2 tratar de eliminar un archivo que no existe

print("\n")
print("*"*80)

try:
  os.remove(os.getcwd()+"/archivo_ejemplo.txt") 
except FileNotFoundError:
    print("Archivo no encontrado disculpe")
finally:
    print("Esta seccion del codigo se ejecuta siempre")           
