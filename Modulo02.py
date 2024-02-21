# importar del modulo random la funcion randint

from random import randint as azar

from random import *  
# de esta forma se importan todas las funciones dentro de random,
# no es muy recomendable ya que puede originar conflictos de nombres


# seccion de codigo usando solo el import de la funcion randint

continua = "s"
numero = 0

while continua =='s' or continua =='S':
    lanzaDado = azar(1,6)
    while numero <1 or numero >6:
     numero = int(input("Por favor ingrese un numero del 1 al 6: "))
    print(f"Numero obtenido al azar del 1 al 6: {lanzaDado}")
    if numero == lanzaDado:
        print("Haz adivinado felicidades")
        break
    elif numero != lanzaDado:
        print("Lo sentimos no haz adivinado")
    continua = input("Desea continuar [S/N]: ")
    
print("*"*80)

# seccion de codigo usando el import de toda la libreria


continua2 = "s"
numero2 = 0

while continua2 =='s' or continua2 =='S':
    lanzaDado2 = randint(1,6)
    while numero2 <1 or numero2 >6:
     numero2 = int(input("Por favor ingrese un numero del 1 al 6: "))
    print(f"Numero obtenido al azar del 1 al 6: {lanzaDado2}")
    if numero2 == lanzaDado2:
        print("Haz adivinado felicidades")
        break
    elif numero2 != lanzaDado2:
        print("Lo sentimos no haz adivinado")
    continua2 = input("Desea continuar [S/N]: ")

    

