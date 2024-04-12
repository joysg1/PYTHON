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

def comprobar(opcion_usuario, opcion_maquina):
    global partidas, ganadas, perdidas, empatadas
    partidas = partidas + 1
    print("\n")
    if (opcion_usuario == opcion_maquina):
        print("Hemos empatado")
        empatadas = empatadas + 1
    elif (opcion_usuario == 'Piedra') and  (opcion_maquina =='Tijera'):
        print("Haz ganado")  
        ganadas = ganadas +1
    elif (opcion_usuario == 'Papel') and  (opcion_maquina =='Piedra'):
        print("Haz ganado")  
        ganadas = ganadas +1
    elif (opcion_usuario == 'Tijera') and  (opcion_maquina =='Papel'):
        print("Haz ganado")  
        ganadas = ganadas +1
    else:
        print("Haz perdido")
        perdidas = perdidas +1
    print("\n")   
    print("*"*20)  
    print(f"Opcion IA = {opcion_maquina}")
    print(f"Opcion USUARIO = {opcion_usuario}")
    print(f"Llevamos {partidas} partidas")  
    print(f"Llevamos {ganadas} partidas ganadas")   
    print(f"Llevamos {perdidas} partidas perdidas") 
    print(f"Llevamos {ganadas} partidas ganadas")  
     
     
     
     
            
           
            
                
    
def main():
    iniciar()
    opcion_usuario = menu()
    while True:
        if opcion_usuario != None:
            opcion_maquina = IA()
            comprobar(opcion_usuario,IA)
        opcion_usuario = menu()    
    
if __name__ =='__main__':
     main()