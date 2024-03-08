# Los getters y setters permiten acceder y modificar los atributos
# de una clase de forma controlada

# Los getters se usan para obtener el valor del atributo

# Los setters se usan para establecer el valor del atributo

class persona:
    def __init__(self, nombre, edad):   #Constructor del metodo
        self._nombre = nombre  # Con el _ protegemos los atributos
        self._edad = edad 
    def get_nombre(self):   #Obtener nombre
        return self._nombre   
    def set_nombre(self, nombre): #Dar valor a nombre
        self._nombre = nombre 
    def get_edad(self):    #Obtener edad    
        return self._edad
    def set_edad(self, edad): #Dar valor a edad
        if edad >=0:          #Comprobacion de la edad
            self._edad = edad
        else:
            print('La edad introducida es negativa, favor verifique')
 
 
 # Nota el _ indica que el atributo esta protegido y no puede ser accedido
 # desde fuera de la clase
 
            
# Crear objetos, instanciar la clase


persona1 = persona("Maria",15) 
print("Nombre persona1: ",persona1.get_nombre())
print("Edad persona1: ",persona1.get_edad())  
print("\n")
print("*"*80)
persona2 = persona("Carlos",22)
print("Nombre persona2: ",persona2.get_nombre())
print("Edad persona2: ",persona2.get_edad())  

print("*"*80)
print("\n")



# Usar setter para establecer los nombres y las edades

print("+++ Nuevos valores usando setter +++")
persona1.set_nombre("Luis") 
persona1.set_edad(19)
persona2.set_nombre("Karla")
persona2.set_edad(22)
persona2.set_edad(-1)  # Probamos que no se pueda ingresar edad negativa
print("Nombre persona1: ",persona1.get_nombre())
print("Edad persona1: ",persona1.get_edad())  
print("\n")
print("*"*80)
print("Nombre persona2: ",persona2.get_nombre())
print("Edad persona2: ",persona2.get_edad())   

print("*"*80)
print("\n")
 