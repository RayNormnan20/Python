#Inegreso de datos
promedio = float(input("Promedio pónderado: "))

#Proceso
if promedio >=17:
    categoria = "A"
elif promedio >= 14:
    categoria = "B"
elif promedio >= 12:
    categoria = "C"
else:
    categoria = "D"

#Mostrar resultados

print("Categoria es: " + str(categoria))