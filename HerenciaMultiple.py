# La herencia multiple permite que una sublclase herede atributos y metodos
# de multiples superclases


# Creacion de la clase vehiculo

class Vehiculo:
    def __init__(self, marca, modelo): #Constructor
        self.marca = marca
        self.modelo = modelo
        
# Creacion de la clase transporte

class Transporte:
    def __init__(self, capacidad): #Constructor
        self.capacidad = capacidad    
        
        
# Las clases vehiculo y transporte actuaran como las clases padres (de las cuales heredaran)


# Creacion de la clase camnion, que heredara de ambas clases padre (vehiculo y transporte)   

class Camion(Vehiculo, Transporte):
    def __init__(self, marca, modelo, capacidad, carga): #Constructor de la clase camion
        Vehiculo.__init__(self, marca, modelo) #Constructor de la clase padre Vehiculo
        Transporte.__init__(self, capacidad) #Constructor de la clase padre transporte 
        self.carga = carga 
    def describir_camion(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Capacidad: {self.capacidad} - Carga: {self.carga}"
    
# Instanciar la clase

miCamion = Camion("Toyota","Full",1000,"Madera")  

print(f"Descripcion de miCamion = {miCamion.describir_camion()}")  

print("\n")
print("*"*80)

print(f"Tipo de carga de miCamion = {miCamion.carga}")
print(f"Capacidad de mi camion = {miCamion.capacidad}")

print("\n")
print("*"*80)