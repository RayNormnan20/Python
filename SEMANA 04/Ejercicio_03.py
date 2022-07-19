#Ingreso de datos
num1 = int(input("Ingrese el 1er número: "))
num2 = int(input("Ingrese el 2do número: "))
num3 = int(input("Ingrese el 3er número: "))

#Proceso
mayor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

#Mostrar resultados 
print("El número mayor es: " + str(mayor))
