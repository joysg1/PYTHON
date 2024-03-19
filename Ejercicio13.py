class alumno:
    def __init__(self, nombre, calificacion):  #Constructor
        self.nombre = nombre
        self.calificacion = calificacion
    def validar_calificacion(self, calificacion):
        if calificacion >=71:
            return True
        else:
            return False 
    def __str__(self):
        return f"Nombre: {self.nombre} - Calificacion: {self.calificacion} - Aprobo ? = {self.validar_calificacion(self.calificacion)}"
            
# Crear objeto alumno:

miAlumno = alumno('Jose',80)
miAlumno2 = alumno('Luisa',61)

print("*"*80)
print(miAlumno)
print("\n")
print("*"*80)
print(miAlumno2)

 

   