# Uso de zip para combinar dos listas

nombres = ['Juan','Carlos','Maria']
edades = [20,15,23]

combinado = zip(nombres,edades)
print(f" Tipo de dato combinado por default: {type(combinado)}")
print(f" Combinado por default: {combinado}")
print("*"*80)
print("\n")

combinadoL = list(combinado)
print(f"Tipo de datos del combinado tras convertirlo a lista: {type(combinadoL)}")
print(f"Contenido del combinado tras volverlo lista: {combinadoL}")

print("*"*80)
print("\n")

print("Impresion de los pares utilizando un ciclo for")

for nombre, edad in combinadoL:
    print(nombre, " tiene ", edad, " años")

print("*"*80)
print("\n")


# Uso de zip para combinar tres listas

nombres = ['Juan','Carlos','Maria']
edades = [20,15,23]
alturas = [1.80,1.75,1.60]

combinadoL2 = list(zip(nombres,edades,alturas))

print(f"Tipo de datos del combinado de tres listas {combinadoL2}")
print(f"Contenido del combinado de tres listas {combinadoL2}")
print(f"Recorrido de los elementos del combinado de tres listas: ")
for nombres, edades, alturas in combinadoL2:
    print(f"{nombres} tiene {edades} años y mide {alturas} metros")
    
    
print("*"*80)
print("\n")


# Desempaquetado, pasar a variables los contenidos del combinado

print("Recorrido del desempaquetado del combinado de las tres listas")
for persona in combinadoL2:
        nombre, edad, altura = persona
        print(f"{nombre} tiene {edad} años y mide {altura} metros")
        
print("*"*80)
print("\n")        