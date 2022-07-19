#Ingreso de datos 

magnitud = int(input("Ingrese la mannitud del ángulo: "))

#Proceso

if magnitud >= 0 and magnitud <= 360:
    if magnitud == 0:
        clasificacion = "Nulo"
    elif magnitud < 90: 
          clasificacion = "Agudo"
    elif magnitud == 90:
        clasificacion = "Recto"
    elif magnitud < 180:
        clasificacion = "Obtuso"
    elif magnitud == 180:
        clasificacion = "Llano"
    elif magnitud <360:
        clasificacion = "Cóncavo"
    else:
        clasificacion = "Completo"
    #Mostrar resultados   
    print("La clasificación del ángulo es: " + str(clasificacion))
else:
    print("La data ingresada no es valida ")

