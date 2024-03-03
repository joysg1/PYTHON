#Un diccionario es una estructura de datos comprendida por pares: una
# clave y uno o varios valores, que puede ser un elemento o una lista

# Los diccionarios se crean con las llaves {}
# Las listas se crean con corchetes []
# Las tuplas se crean con parentesis () o sin estos 

diccionario = {'nombre':'Marcos', 'apellido':'Lopez', 'telefono':'346-1234', 'gustos':['Ver series','Jugar futbol','Cocinar']}

print(f"Contenido del diccionario: {diccionario}")

a = type(diccionario)

print(f"Tipo de dato {a}")
print("\n")
print("*"*80)

print("Mostrar algunos valores de las claves del diccionario")
print(f"Nombre: {diccionario['nombre']}")
print(f"Gustos: {diccionario['gustos']}")
print(f"Gusto con indice 1: {diccionario['gustos'][1]}")

print("\n")
print("*"*80)

print("Recorrer todos los elementos de un diccionario")

for clave in diccionario:
    print(clave, ":" ,diccionario[clave])
    
print("\n")
print("*"*80)    


#Metodos de los diccionarios

persona = dict(nombre= 'Carlos', apellido = 'Garcia', edad = 32)

b = type(persona)

print(f"Contenido del diccionario persona: {persona}")
print(f"Tipo de datos: {b}")

print("\n")
print("*"*80)  

diccionario02 = dict(zip('aeiou',[1,2,3,4,5]))

c = type(diccionario02)
print(f"Contenido del diccionario02: {diccionario02}")
print(f"Tipo de datos: {c}")

print("\n")
print("*"*80) 

d = diccionario02.items()

print(f"Tuplas con claves y valores del diccionario02: {d}")

print("\n")
print("*"*80) 

e = diccionario02.keys()

print(f"Llaves del diccionario02 = {e}")

print("\n")
print("*"*80) 

f = diccionario02.values()

print(f"Valores del diccionario02: {f}")

print("\n")
print("*"*80) 


# Vaciar los valores del diccionario02

diccionario02.clear()
print(f"Diccionario02 tras ser limpiado: {diccionario02}")

print("\n")
print("*"*80) 


# Copiar un diccionario

copiaDic = diccionario

g = type(copiaDic)

print(f"Contenido de copiaDic: {copiaDic}")
print(f"Tipo de dato: {g}")

h = copiaDic == diccionario

print(f"Es copiaDic igual a diccionario? {h}")


print("\n")
print("*"*80) 


# Asignar a cada clave un valor

diccionario03 = dict.fromkeys(['a','e','i'],10)
print(f"Contenido del diccionario03: {diccionario03}")

i = type(diccionario03)

print(f"Tipo de dato: {i}")

print("\n")
print("*"*80) 


# Mostrar el contenido de una clave de un diccionario
c1 = diccionario.get('nombre')
print(f" Contenido de la clave nombre del diccionario: {c1}")
c2 = diccionario.get('apellido')
print(f" Contenido de la clave apellido del diccionario {c2}")
c3 = str(input('Por favor ingrese una clave para buscarla: '))
try:
 c4 = diccionario.get(c3)
 print(f"Contenido de la clave ingresada: {c4}")
 
except:
    print("Lo sentimos la clave ingresada no existe")
    
print("\n")
print("*"*80) 


# Borrar una clave de un diccionario

b1 = str(input('Por favor ingrese una clave a borrar en el diccionario: '))

try:
 diccionario.pop(b1)
 print(f"Clave {b1} encontrada")
 print(f"Contenido del diccionario tras operacion: {diccionario}")
except KeyError:
    print("Lo sentimos la clave ingresada no existe")
    
    
# Uso de update

diccionarioU = {'nombre':'Ana','pais':'Panama'}

# Se actualizara el diccionario con el diccionarioU


print(f"Contenido del diccionario sin haberle aplicado el update: {diccionario}")
diccionario.update(diccionarioU)
print(f"Contenido del diccionario tras haberle aplicado el update: {diccionario}")

print("\n")
print("*"*80) 
    