import random
import sys

def iniciar():
    global partidas, ganadas, perdidas, empatadas 
    partidas = 0
    ganadas = 0 
    perdidas = 0 
    empatadas = 0

def menu():
    print(""" Indica el numero de la opcion 
          1. Piedra
          2. Papel
          3. Tijera
          0. Salir  
          """)
    
    opcion = str(input("Diga el numero de la opcion: "))
    
    if opcion not in ('1','2','3','0'):
        print("Selecciona una opcion valida \n")
        opcion_usuario = None
    else:
        if opcion == '1':
            opcion_usuario = 'Piedra'
        if opcion == '2':
            opcion_usuario = 'Papel'
        if opcion == '3':
            opcion_usuario = 'Tijera' 
        if opcion == '0':
            print("Hasta pronto")    
            sys.exit()  
             
    return opcion_usuario   


def IA():  
    lista_opciones = ['Piedra', 'Papel', 'Tijera']   
    opcion_IA = random.choice(lista_opciones)
    return opcion_IA
            
                
    
def main():
    iniciar()
    menu()
    
if __name__ =='__main__':
     main()