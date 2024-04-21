"""

Crea para el ejercicio anterior un 
script que llame al archivo donde 
tengas las funciones de base de 
datos y mediante un menu de opciones 
permita al usuario seleccionar que 
accion ejecutar con la base de datos.

"""

import BaseDeDatosEstudiante

print("1. Consultar \n")
print("2. Actualizar \n")
print("3. Insertar \n")
print("4. Borrar \n")
print("0. Salir \n")


opcion = int(input("Por favor seleccione una opcion: "))

match opcion:
    case 0:
        exit()
    case 1:
        BaseDeDatosEstudiante.consultar()
        Alumnos = BaseDeDatosEstudiante.consultar() 
        print("Lista de los nombres de los alumnos\n")
        for Alumno in Alumnos:
         print(f"Nombre del alumno: {Alumno[1]}, Calificacion: {Alumno[2]}")
         print("\n")
    case 2:
        id = int(input("Ingrese el id del estudiante a modificar: "))
        nombre = str(input("Ingrese el nuevo nombre del alumno: ")) 
        nota = int(input("Ingrese la nueva nota del estudiante: ")) 
        BaseDeDatosEstudiante.actualizar(id,nombre,nota)
    case 3:
        id = int(input("Ingrese el id del nuevo estudiante: "))
        nombre = str(input("Ingrese el nombre del nuevo estudiante: ")) 
        nota = int(input("Ingrese la nota del nuevo estudiante: "))
        alumno = (id,nombre,nota) 
        BaseDeDatosEstudiante.insertar(alumno)     
    case 4: 
        id = int(input("Ingrese el id del estudiante a borrar: "))
        BaseDeDatosEstudiante.borrar(id) 
    case _:
        print("Opcion fuera de rango")       