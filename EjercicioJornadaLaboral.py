from datetime import datetime

actual = datetime.now().time()
print(actual)

hora_salida = 21
minuto_salida = 30

if actual.hour >=hora_salida:
    print("Ya se ha cumplido tu jornada laboral")
else:
    faltan_horas = hora_salida - actual.hour
    faltan_minutos = minuto_salida - actual.minute
    if faltan_minutos <0:
        faltan_horas = faltan_horas - 1 
        faltan_minutos = (-1 * faltan_minutos) + 30 
    print("No se ha cumplido tu jornada laboral")  
    print(f"Faltan {faltan_horas} horas y {faltan_minutos} minutos para que puedas salir")  
    