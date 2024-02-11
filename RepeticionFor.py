#tabla de multiplicar con for

tabla = int(input('Tabla a generar: '))
print(f"Tabla del {tabla}\n")

#repetir mientras sea menor que 12
for contador in range (1,13):
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}\n")
print("Fin de la tabla")  

#ejemplo for con listas

print("------------------------------\n")

nombres = ["Carlos", "Maria", "Juan", "Marcos"]

for nombre in nombres:
    print(f"Hola , {nombre}\n")  
    
    
#ejemplo for numeros del 1 al 100\

print("-----------------------------\n")

for contador in range(1,101):
    print(f"Numero {contador} \n")        