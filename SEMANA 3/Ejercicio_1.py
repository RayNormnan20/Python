#Ingreso de datos
edad= int(input("Ingrese la edad: "))
peso= float(input("Ingrese su pero en kg: "))

#Preceso
frecuencia= 210 - (0.5 * edad) - (0.1 * peso + 4)

#Mostrar resultados 
print("Frecuencia cardiaca es: " + str(frecuencia))
