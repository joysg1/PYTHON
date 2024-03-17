def imc(peso,estatura):
    return peso / (estatura **2)


peso = 0
estatura = 0 

while peso <=0 or estatura <=0:
 peso = float(input("Por favor ingrese el peso en kilogramos: "))
 estatura = float(input("Por favor ingrese su estatura en metros: "))

print("*"*80)
print("\n")
resultado = imc(peso,estatura)
print(f"Peso introducido = {peso} kg -- Estatura introducida = {estatura} m")
print(f"Su IMC es igual a = {resultado:.2f}") 
 
 