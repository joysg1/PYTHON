import datetime

hora_actual = datetime.datetime.now()
hora_actual_f = hora_actual.strftime("%H:%M")


hora_salida = datetime.datetime(2024,3,19,22,30,0)
hora_salida_f = hora_salida.strftime("%H:%M")




if hora_actual >= hora_salida:
    mensaje = "Usted ya ha cumplido su jornada laboral"
    print(f"Hora actual = {hora_actual_f} > Hora de salida = {hora_salida_f}")
else:
    mensaje = "Usted no ha cumplido su jornada laboral"
    print(f"Hora actual = {hora_actual_f} < Hora de salida = {hora_salida_f}") 
    dif_h = hora_salida.hour - hora_actual.hour
    print(f"Numero de horas para salir de turno = {dif_h}")
    
      
print(mensaje)
