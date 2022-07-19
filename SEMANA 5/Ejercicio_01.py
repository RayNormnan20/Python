#Ingreso de datos 
veocidad = float(input("Velocidad: "))


#Proceso
if veocidad <= 0: 
    mensaje = "velocidad no valida"
if veocidad >0 and veocidad <= 70:
    mensaje = "No hay sanción"
if veocidad >70: 
    mensaje = "La multa es S/. 100.00"
if veocidad >90:
    mensaje = "La multa es S/. 140.00"
if veocidad >100:
    mensaje = "La multa es S/. 200.00"

#Mostrar resultados 
print(mensaje)

