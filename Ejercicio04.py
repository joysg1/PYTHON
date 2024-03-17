

cadena = 'Hola'
numero = 77

print(f"Variable tipo cadena = {cadena}")
print(f"Comprobacion de tipo = {type(cadena)}")
print("*"*80)
print("\n")

print(f"Variable tipo numero = {numero}")
print(f"Comprobacion de tipo = {type(numero)}")
print("*"*80)
print("\n")


# Procedemos a modificar las variables
print("A continuacion procederemos a modificar los valores")
cadena = str(input("Por favor ingrese el nuevo valor de la variable cadena: "))
numero = int(input("Por favor ingrese el nuevo valor de la variable numero: "))
print("*"*80)
print("\n")

print("---- Valores actualizados ----")
print(f"Variable tipo cadena = {cadena}")
print(f"Comprobacion de tipo = {type(cadena)}")
print("*"*80)
print("\n")

print(f"Variable tipo numero = {numero}")
print(f"Comprobacion de tipo = {type(numero)}")
print("*"*80)
print("\n")



print("Ejemplo extra, multiplicacion de cadena")
print("Hola"*5)
