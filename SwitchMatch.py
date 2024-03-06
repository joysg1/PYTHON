# Ejemplo #1 utilizando colores

color = str(input("Por favor ingrese un color: "))

match color:
    case 'azul':
        print("El color ingresado es el azul")
    case 'rojo':
        print("El color ingresado es el rojo")
    case 'amarillo':
        print("El color ingresado es el amarillo")
    case 'verde':
        print("El color ingresado es el verde")
    case 'rosado':
        print("El color ingresado es el rosado")
    case _:
        print("El color ingresado no esta en la lista")  
        
print("\n")
print("*"*80)        
        

# Ejemplo #2 utilizando numero de mes


numMes = int(input("Por favor ingrese un numero del mes: "))

match numMes:
    case 1:
        print(f" Numero ingresado = {numMes} el mes es Enero")
    case 2:
        print(f" Numero ingresado = {numMes} el mes es Febrero")
    case 3:
        print(f" Numero ingresado = {numMes} el mes es Marzo")
    case 4:
        print(f" Numero ingresado = {numMes} el mes es Abril")
    case 5:
        print(f" Numero ingresado = {numMes} el mes es Mayo")
    case 6:
        print(f" Numero ingresado = {numMes} el mes es Junio")
    case 7:
        print(f" Numero ingresado = {numMes} el mes Julio")
    case 8:
        print(f" Numero ingresado = {numMes} el mes es Agosto")
    case 9: 
        print(f" Numero ingresado = {numMes} el mes es Septiembre")
    case 10:
        print(f" Numero ingresado = {numMes} el mes es Octubre")
    case 11:
        print(f" Numero ingresado = {numMes} el mes es Noviembre") 
    case 12:
        print(f" Numero ingresado = {numMes} el mes es Diciembre")  
    case _:
        print(f"Numero ingresado = {numMes} este no corresponde a un mes")                                          
                    