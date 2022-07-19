#Ingreso de datos 

peso = float(input("Ingrese su peso en kg: "))
estatura= float(input("Ingrese estatura en mtrs: "))


#Proceso

IMC = peso / (estatura * estatura)

if IMC < 20:
    Grado = "Delgado"
elif IMC < 25:
    Grado  = "Normal"
elif IMC < 30:
    Grado  = "Sobrepeso"
else:
    Grado  = "Obesidad"

#Mostrar resultados
print("Su IMC es: " + str(IMC))
print("Su grado es: " + str(Grado))

