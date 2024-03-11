# El polimorfismo permite que diferentes objetos de clases distintas
# puedan responder de manera uniforme a la misma accion o mensaje

# En python el poliformismo se implementa a traves de la herencia y la 
# sobrecarga de metodos 

# La herencia permite que una subclase herede los atributos y metodos de una
# superclase

# La sobrecarga de metodos permite que una subclase defina un metodo con el
# mismo nombre que una superclase pero con un comportamiento diferente

# Esto permite que objetos de distintas clases respondan de forma personalizada
# una misma accion



# Ejemplo superclase Animal y subclases Perro y Gato

class Animal:
    def hacer_sonido(self):  
        pass

class Perro(Animal):
    def hacer_sonido(self): #Sobrecarga del metodo hacer sonido con implementacion personalizada
        return "Gau"

class Gato(Animal):
    def hacer_sonido(self): #Sobrecarga del metodo hacer sonido con implementacion personalizada
        return "Miau"
    
    
    
    
# Funcion para interactuar con animales

def interactuar_con_animal(animal):
    return animal.hacer_sonido()
    
    
    
# Crear las instancias de las clases perro y gato

MiPerro = Perro()
MiGato = Gato()   


# Uso de las funcion interactuar con animales y guardado del resultado

resultado1 = interactuar_con_animal(MiPerro)
resultado2 = interactuar_con_animal(MiGato)


print(f"Resultado de la interaccion con el Perro = {resultado1}")
print(f"Resultado de la interaccion con el Gato = {resultado2}")
print("\n")
print("*"*80)


# Acceso directo al atributo de los objetos de las clases perro y gato

print(f"Sonido que hace un perro = {MiPerro.hacer_sonido()}")
print(f"Sonido que hace un gato = {MiGato.hacer_sonido()}")
print("\n")
print("*"*80)