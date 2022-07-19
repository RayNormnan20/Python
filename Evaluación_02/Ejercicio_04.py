#Ingreso de datos 

horas = float(input("Ingrese las horas: "))
torniDefectuosos = int(input("Ingrese la cantidad de tornillos def. : "))
torniNoDefectuosos = int(input("Ingrese la cantidad de tornillos no def. : "))

if horas < 1.5 and torniDefectuosos > 300 and torniNoDefectuosos < 1000:
    grado = 5
if horas <= 1.5:
    grado = 7
if torniDefectuosos < 300:
    grado = 8
if torniNoDefectuosos > 10000:
    grado = 9
if horas <= 1.5 and torniDefectuosos < 300:
    grado= 12
if horas >= 1.5 and torniNoDefectuosos > 10000:
    grado = 13
if torniDefectuosos < 300 and torniNoDefectuosos > 10000:
    grado = 15
if horas <= 1.5 and torniDefectuosos < 300 and torniNoDefectuosos > 10000:
    grado = 20

#Mostrar resultados 
print("El grado asignado de eficiencia es: " + str(grado))

    


