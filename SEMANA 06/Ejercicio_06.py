#Ingreso de datos 
numEntero = int(input("Ingrese el numero entero Lu(1), Ma(2), Mi(3), Ju(4), Vi(5), Sa(6), Dom(7):  "))

#Proceso
if numEntero== 1:
    dia = "Lunes"
elif numEntero == 2:
    dia = "Martes"
elif numEntero == 3:
    dia = "Miercoles"
elif numEntero == 4:
    dia = "Jueves"
elif numEntero == 5:
    dia = "Viernes"
elif numEntero == 6:
    dia = "Sabado"
elif numEntero == 7:
    dia = "Domingo"
else:
    dia = "No valido"

#Mostrar resultados 

print("El dia es: " + str(dia))