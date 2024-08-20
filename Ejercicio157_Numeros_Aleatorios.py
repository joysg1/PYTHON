# Generar numeros aleatorios a partir de un rango dado por el usuario
import random


def generar_numero_aleatorio(rango_inicial, rango_final): #Funcion que genera numero aleatorio

    return random.randint(rango_inicial, rango_final) #Retorna numero aleatorio entre el rango dado


rango_1 = int(input("Ingrese el rango inicial: "))
rango_2 = int(input("Ingrese el rango final: "))
numero_aleatorio = generar_numero_aleatorio(rango_1, rango_2)
print(f"Numero aleatorio entre {rango_1} y {rango_2}: {numero_aleatorio}")