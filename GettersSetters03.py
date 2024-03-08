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
        if edad >=0 and edad <150:          
            self._edad = edad
        elif edad <=0:
            print('La edad introducida es negativa, favor verifique')
        elif edad >=150:
            print('La edad introducidad es muy alta, favor verifique')
         
 
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
# Prueba de introducir una edad muy grande
persona2.edad = 150