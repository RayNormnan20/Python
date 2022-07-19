#Ingreso de datos 

temperatura = int(input("Ingrese la temperatura promedio: "))

#Proceso
if temperatura <= 10:
    clima = "Frío"
elif temperatura <= 20:
    clima = "Nublado"
elif temperatura <= 30:
    clima = "Caluroso"
else:
    clima = "Trópico"

#Mostrar resultados
print("La temperatura promedio del día es: " + str(clima))