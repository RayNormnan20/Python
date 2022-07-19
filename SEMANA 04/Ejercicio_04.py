#Ingreso de datos

promedio = float(input("Ingrese el promedio del alumno: "))


#Proceso
if promedio >= 17:
    categoria = "A"
if promedio >= 14 or promedio < 17: 
    categoria = "B"
if promedio >= 12 or promedio < 14: 
    categoria = "C"
if promedio < 12:
    categoria = "D"



#Mostrar resultados 
print("La categoría es: " +str(categoria))