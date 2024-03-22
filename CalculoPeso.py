
# Creacion de la funcion

def CalculoPeso(masa, gravedad):
    peso = masa * gravedad
    return peso



# Datos son pedidos al usuario

masaUsuario = 0

while masaUsuario <= 0:

 masaUsuario = float(input("Por favor ingrese la masa en kg: "))

print("-"*70)


gravedadUsuario = 0


while gravedadUsuario <=0:
   
   gravedadUsuario = float(input("Por favor ingrese la gravedad en m/s2: "))

print("*"*70)
print("\n")

# Llamada a la funcion 

resultadoPesoUsuario = CalculoPeso(masaUsuario, gravedadUsuario)

# Impresion de resultados

print("--- RESULTADOS FINALES ---")
print(f"Masa = {masaUsuario} - Gravedad = {gravedadUsuario}")
print(f"Peso = {resultadoPesoUsuario}")

print("*"*70)
print("\n")

