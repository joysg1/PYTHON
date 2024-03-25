import math   #Importe de la libreria math



def CalculoVolumenEsfera(r):        #Se define la funcion
 result = (4/3 * math.pi ) * r **3
 return result


radioUsuario = 0  # Variable para capturar el radio


while radioUsuario <=0: # Comprobacion de que el radio introducido no sea ni cero ni negativo
 radioUsuario = float(input("Por favor ingrese el radio: "))
 if radioUsuario <=0:
  print(f"El radio introducido = {radioUsuario} debe ser verificado")


# Llamado de la funcion
  
resultadoUsuario = CalculoVolumenEsfera(radioUsuario)
print("\n")
print("*"*80)
print("\t\t\t ---RESULTADOS---\n")
print(f"Radio = {radioUsuario} -- Volumen Esfera = {resultadoUsuario:,.2f}") 


block = input()
  