
    
#Creacion de la funcion que devuelva los numeros impares 

def impares():
    for numero in  range (1,51,2):
        yield numero
            
            
#Creacion de un objeto iterable

generador = impares()

#Impresion de los tres primeros elementos de forma manual:

print(next(generador))
print(next(generador))
print(next(generador))

print("------------------------------\n")
print("Termina la impresion normal y sigue mediante el ciclo for\n")

#Impresion de todos los elementos restantes mediante un ciclo for:

for numero in generador:
    print(f"Numero: {numero}")