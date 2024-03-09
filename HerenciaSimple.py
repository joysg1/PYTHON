# La herencia simple permite que una clase herede atributos y metodos de otra clase
# La subclase hereda todos los atributos y metodos de la clase padre
# La subclase puede modificar los atributos y metodos y agregar mas

# Creacion de la clase padre

class Vehiculo:
    def __init__(self, marca, modelo):  #constructor
        self.marca = marca
        self.modelo = modelo
    def describir(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo}"    
    
    
# Creacion de la clase hija, que va a heredar de vehiculo

class Auto(Vehiculo): #La clase Auto hereda de la clase Vehiculo
    def __init__(self, marca, modelo, color): #constructor de la clase Auto
        super().__init__(marca, modelo) #constructor de la clase padre
        self.color = color 
    def describir_auto(self):
        return f"{self.describir()} Color: {self.color}"  #Usamos el metodo describir de la clase padre y agregamos la impresion del atributo color  
    
    
#Instanciar la clase

miAuto = Auto('Toyota','Corolla','Rojo')

#Acceder a metodos y atributos

print(f"Descripcion de mi auto desde metodo de la clase Auto = {miAuto.describir_auto()}")
print("\n")
print("*"*80)

print(f"Descripcion de mi auto desde metodo de la clase padre (Vehiculo) = {miAuto.describir()}")
print("\n")
print("*"*80)

print(f"Acceso a uno de los atributos de mi auto (marca): {miAuto.marca}")
print("\n")
print("*"*80)