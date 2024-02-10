#tabla de multiplicar

tabla = int((input("Por favor ingrese la tabla que desea ver: ")))

#variable contador

contador = 1

print(f"Tabla del numero {tabla}\n")

#repeticion

while contador <13:
    #calculo de la tabla de multiplicar
    resultado = tabla * contador 
    #impresion de resultado
    print(f"{tabla} X {contador} = {resultado} \n")
    #incremento del contador
    contador = contador + 1
print("Fin de la tabla")    


#version del codigo en donde se comprueba que el contador valga 4 para
#salir del bucle

print("------------------------------")

contador = 1

while contador<13:
    resultado = tabla * contador
    print(f"{tabla} X {contador} = {resultado}")
    
    
    if contador ==4:
        print(f"Contador = {contador} el ciclo se ha terminado")
        break
    contador = contador +1
print("Fin de la tabla")    
