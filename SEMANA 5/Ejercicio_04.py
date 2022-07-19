#Ingreso de datos 

#Diseñe un programa que lea un número entero del intervalo 1 a 7 
#correspondiente a un día de la semana y determine el nombre del día. 
#Considere: 1 para lunes, 2 para martes, ..., 6 para sábado, 7 para domingo.

numeroDia= int(input("Ingrese el numero Lunes(1), Martes(2), Miercoles(3), Jueves(4), Viernes(5), Sabado(6), Domingo(7): "))

if numeroDia < 1:
    mensaje = "El número debe ser positivo"
if numeroDia == 1:
    mensaje= "El nombre del día es Lunes"
if numeroDia == 2:
    mensaje= "El nombre del día es Martes"
if numeroDia == 3:
    mensaje= "El nombre del día es Miercoles"
if numeroDia == 4:
    mensaje= "El nombre del día es Jueves"
if numeroDia == 5:
    mensaje= "El nombre del día es viernes"
if numeroDia == 6:
    mensaje= "El nombre del día es Sabado"
if numeroDia == 7:
    mensaje= "El nombre del día es Domingo"
if numeroDia > 7:
    mensaje = "No existen mas dias para mostrar"
    
#Mostrar resultados
print(mensaje)