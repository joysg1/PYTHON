

class persona:
    def __init__(self, nombre, edad):   
        self._nombre = nombre  
        self._edad = edad 
    @property           #Uso de decorador @property
    def nombre(self):   
        return self._nombre
    @nombre.setter   
    def nombre(self, nombre): 
        self._nombre = nombre 
    @property    
    def edad(self):       
        return self._edad
    @edad.setter
    def edad(self, edad): 
        if edad >=0:          
            self._edad = edad
        else:
            print('La edad introducida es negativa, favor verifique')
 
 
 
# Crear objetos, instanciar las clase
            



persona1 = persona("Maria",15) 
print("Nombre persona1: ",persona1.nombre)
print("Edad persona1 = ",persona1.edad)
persona1.nombre = "Luis"
print("Nombre persona1 actualizado: ",persona1.nombre)
persona1.edad = 12
print("Edad persona1 actualizada: ",persona1.edad)
# Prueba de introducir una edad negativa
persona1.edad = -1
print("\n")
print("*"*80)


persona2 = persona("Juan",22)
print("Nombre persona2: ",persona2.nombre)
print("Edad persona2: ",persona2.edad)
persona2.nombre = "Sara"
print("Nombre persona2 actualizado: ",persona2.nombre)
persona2.edad = 19
print("Edad persona2 actualizada: ",persona2.edad)
# Prueba de introducir una edad negativa
persona2.edad = -5



# El decorador @property permite que el metodo nombre se comporte como
# un getter, lo que significa que puedes acceder al metodo nombre
# como si fuera un atributo directo de la instancia de la clase
# mediante, ejemplo: persona1.nombre


# El decorador @nombre.setter permite que el metodo nombre se comporte
# como un setter lo que significa que puedes establecer el atributo nombre
# como si fuera un atributo directo de la instancia de la clase, 
# permitiendo cambiar su valor mediante ejemplo persona1.nombre = "nombre"

# Lo anteriormente dicho aplica para el atributo edad con los getters y
# setters correspondientes


# Usar getter y setters nos proporciona un mayor control sobre los atributos 
# de una clase y nos permite implementar logica adicional como validaciones
# cuando sea necesario 
 