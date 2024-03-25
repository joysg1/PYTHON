# Con los conocimientos adquiridos, intenta desarrollar el juego de Piedra, papel, tijera

# Funcion para determinar el ganador

def determinar(o1,o2):
    if o1 =="piedra" and o2 =="piedra":
        mensaje = f"Empate {o1} = {o2}"
    elif o1 =="papel" and o2 =="papel":
        mensaje = f"Empate {o1} = {o2}"
    elif o1 =="tijera" and o2 =="tijera":
        mensaje = f"Empate {o1} = {o2}"
    elif o1 =="piedra" and o2 =="papel":
        mensaje = f"Ganador = {o2}"
    elif o1 =="piedra" and o2 =="tijera":
        mensaje = f"Ganador = {o1}" 
    elif o1 =="papel" and o2 =="piedra":
        mensaje = f"Ganador = {o1}" 
    elif o1 =="papel" and o2 =="tijera":
        mensaje = f"Ganador = {o2}" 
    elif o1 =="tijera" and o2 =="papel":
        mensaje = f"Ganador = {o1}"
    elif o1 =="tijera" and o2 =="piedra":
        mensaje = f"Ganador = {o2}"   
                        
    return mensaje 

# Variables para recojer las opciones

opcion1 = ""
opcion2 = ""

# Verificacion de las opciones ingresadas: 

while opcion1 != "piedra" and opcion1 !="papel" and opcion1 !="tijera":
 opcion1 =str(input("Opcion jugador 1 (piedra, papel, o tijera): "))
 if opcion1 !="piedra" and opcion1 !="papel" and opcion1 !="tijera":
     print(f"Opcion ingresada = {opcion1} fuera del rango (piedra, papel, tijera)")
 
print("*"*80)
print("\n")
 
while opcion2 !="piedra" and opcion2 !="papel" and opcion2 !="tijera": 
 opcion2 = str(input("Opcion jugador 2 (piedra, papel o tijera): "))
 if opcion2 !="piedra" and opcion2 !="papel" and opcion2 !="tijera":
     print(f"Opcion ingresada = {opcion2} fuera del rango (piedra, papel, tijera)")
     
print("*"*80)
print("\n")
    
# Llamado de la funcion

resultado = determinar(opcion1,opcion2)  
print(resultado)   