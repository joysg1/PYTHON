import random
from random import randint as azar



def pensarNumero():
 piensaNumero = azar(1,100)
 return piensaNumero

def solicitarNumero():
 numeroUsuario = int(input("Ingrese un numero del 1 al 100: "))
 return numeroUsuario


pNumero = pensarNumero()
numeroUsuario = solicitarNumero()
intentos = 0
continua = True

while(continua):   
    if(numeroUsuario > pNumero):
        print("El numero que tengo en mente es menor")
        intentos += 1
        numeroUsuario = solicitarNumero()
    if(numeroUsuario < pNumero):
        print("El numero que tengo en mente es mayor")
        intentos += 1
        numeroUsuario = solicitarNumero()
    else:  
        print(f"En {intentos} intentos adivinaste el numero")
        continua = False
    
#video 106 minuto 36



            