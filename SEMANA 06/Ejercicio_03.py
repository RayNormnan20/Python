#Ingreso de datos 
velocidad = float(input("Ingrese la velocidad: "))

#Proceso
if velocidad <=70:
    multa = "Sin sancion"
elif velocidad <=90:
    multa = "S/. 100.00"
elif velocidad <=100:
    multa = "S/. 140.00"
else:
    multa = "S/. 200.00"

#Mostrar resultados 

print("La multa que debrá pagar es: " + str(multa))