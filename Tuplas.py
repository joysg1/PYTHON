# Vamos a crear una tupla que es un objeto inmutable

colores = "amarillo","verde","rojo","azul"

print(f"Contenido de la tupla: {colores}")
print(f"Tipo: {type(colores)}")

print("*"*80)
print("\n")

# Mostrar los dos primeros valores de la tupla colores
print(colores[:2])

print("\n")
print("*"*80)

# Crear una tupla vacia y mostrarla

tupla = ()
print(f"Tupla vacia: {tupla}")
print(f"Tipo: {type(tupla)}")
print("\n")
print("*"*80)


# Probar un indice fuera de rango en la tupla

try:
    print(colores[4])
except IndexError:
    print(f"Indice fuera del rango, la tupla tiene {len(colores)} elementos")  
    
# Tratar de agregar un elemento a la tupla

print("\n")
print("*"*80)

try:
    colores[1]= 'violeta'
except TypeError:
    print("Lo sentimos no podemos agregar elementos a la tupla, al ser este un objeto inmutable")  
    
    
print("\n")
print("*"*80)

a = len(colores)
print(f"Longitud de la tupla colores: {a}")
print(f"Elementos de la tupla colores: {colores}")

print("\n")
print("*"*80)

# Creacion de una tupla unitaria

tuplaUnitaria = (50,)


print(f"Contenido de la tupla unitaria: {tuplaUnitaria}")
print(f"Tipo: {type(tuplaUnitaria)}")
print(f"Longitud de la tupla unitaria: {len(tuplaUnitaria)}")


print("\n")
print("*"*80)

# Empaquetado de tuplas

e1 = 50
e2 = "palabra"
e3 = 0.23

tuplaEmpaquetada = e1, e2, e3

print(f"Contenido de la tupla empaquetada {tuplaEmpaquetada}")
print(f"Tipo de dato de la tupla empaquetada: {type(tuplaEmpaquetada)}")

print("\n")
print("*"*80)

# Desempaquetado de tupla

e1, e2, e3 = tuplaEmpaquetada

print(e1)
print(type(e1))
print(e2)
print(type(e2))
print(e3)
print(type(e3))

print("\n")
print("*"*80)

