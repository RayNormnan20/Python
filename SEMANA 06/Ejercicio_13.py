#Ingreso de datos 
prestamo = float(input("Ingrese el monto del prestamo: "))

#Proceso
if prestamo <= 5000:
    numCutoas= 2
elif prestamo <= 10000:
    numCutoas= 4
elif prestamo <= 15000:
    numCutoas= 6
else:
    numCutoas= 10

if prestamo > 10000:
    interes = prestamo * 3 / 100
else:
    interes = prestamo * 5 / 100

montoMensual = prestamo / numCutoas + interes

interesTotal = interes * numCutoas
    
#Mostrar resultados 
print("El número de cuotas es: " + str(numCutoas))
print("La cuota mensual es: " + str(montoMensual))
print("El  interes total es: " + str(interesTotal))


