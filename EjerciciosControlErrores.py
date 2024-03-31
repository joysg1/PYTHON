# 1. Crea un script que al dividir entre 0 muestre que no es posible
# asegurando de que se muestre un mensaje al usuario

'''
def divide(num1, num2):
  try:
      resultado = num1 / num2
  except ZeroDivisionError:
      resultado = "indeterminado"
  finally:
      return resultado        
      
    




print("---DIVISION DE DOS NUMEROS --- \n")


num1U = int(input("Por favor ingrese un numero: "))


num2U = int(input("Por favor ingrese un segundo numero: "))

resultadoU = divide(num1U, num2U)  

print("\n")
print("*"*80)

print(f"{num1U} / {num2U} = {resultadoU}") 


'''

# 2. Crea un script que intente mostrar un elemento de una lista
# haciendo uso de un indice que no exista

'''

numeros = [0,1,2,3,4,5]

indice = -1 
while indice <0:
 indice = int(input("Ingrese un numero de indice: "))
 
 
try:
    numeros[indice]
    mensaje = print(f"Contenido de la lista en el indice [{indice}] = {numeros[indice]}")  
except IndexError:
    mensaje = (f"La lista no tiene el indice = {indice}") 
finally:
     print(mensaje)            
    
'''