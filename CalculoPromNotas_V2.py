
import statistics

# Funcion que recibe el numero de notas y en funcion de este numero
# pide las notas para guardarlas en una lista


def Promedio(numNotas):
    ListaNotas = []
    PromNotas = ""  
    
    for nota in range(1, numNotas +1):
      
      valorNota = int(input(f"Por favor ingrese la nota #{nota}: "))
      ListaNotas.append(valorNota)  
  
    resultProm = statistics.mean(ListaNotas)
    return resultProm



# Funcion que en base al promedio sacado devolvera la letra correspondiente

def letraPromedio(Promedio):
  letraCal = ""
  
  if Promedio >=91:
    letraCal = "A"
  elif Promedio >=81 and Promedio <=90:
    letraCal = "B"
  elif Promedio >=71 and Promedio <=80:
    letraCal = "C"
  elif Promedio >=61 and Promedio <=70:
    letraCal = "D"
  elif Promedio <61:
    letraCal = "F"   

  return letraCal




# Funcion para determinar si la letra corresponde a una letra de pase o no

def Pase(letra):
  mensaje = ""
  
  if letra =="A":
    mensaje = f"Al ser una = {letra} usted ha aprobado sobresalientemente"
  elif letra =="B":
    mensaje = f"Al ser una = {letra} usted ha aprobado exitosamente"
  elif letra =="C":
    mensaje = f"Al ser una = {letra} usted ha aprobado regularmente" 
  elif letra =="D":
    mensaje = f"Al ser una = {letra} usted ha obtenido la minima de la promocion"
  elif letra =="F":
    mensaje = f"Al ser una = {letra} usted ha fracasado" 

  return mensaje



# Se procede a pedir el numero de notas

NumNotasUser = 0

while NumNotasUser <=0:
   
 NumNotasUser = int(input("Por favor ingrese el numero de notas: "))



# Llamado a la funcion Promedio

r = Promedio(NumNotasUser)

print(f"El promedio de las notas ingresadas es: {r}")
print("-"*80)
print("\n")




# Llamado a la funcion letraPromedio


letraObtenida = letraPromedio(r)

print(f"La letra correspondiente al promedio es: {letraObtenida}")
print("-"*80)
print("\n")


# Llamado a la funcion Pase

MensajeFinal = Pase(letraObtenida)
print(MensajeFinal)
print("-"*80)
print("\n")







