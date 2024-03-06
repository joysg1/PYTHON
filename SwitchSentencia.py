# Ejemplo #1, el usuario da el numero del mes y se retorna el valor en letras

# En python la sentencia switch se emula usando diccionarios

def damenum(num):
    
    seleccion = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"  
        
    }
    
    return seleccion.get(num, "Mes no valido")


valor = int(input("Por favor ingrese un numero de mes: "))
print(f"El mes acorde al numero es: {damenum(valor)}")

print("\n")
print("*"*80)

