def mayorEdad(edad):
    if 0 < edad < 18:
        msj = "Eres menor de edad"
        
    elif edad <= 0:  
        msj = "Edad invalida"
    else:
        msj = "Eres mayor de edad"
    return msj
    
    
edad = int(input("Ingrese su edad: "))
print(mayorEdad(edad))
