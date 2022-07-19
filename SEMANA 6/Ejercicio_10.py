#Ingreso de datos 
altura = float(input("Ingrese la altura en metros: "))

if altura > 0:
    if altura <= 1:
       clasificacion = "mala"
    elif altura <= 4:
        clasificacion = "Arbusto"
    elif altura <= 8:
        clasificacion = "Arbolillo"
    else:
        clasificacion = "Árbol"

    #Mostrar resultados
    print("La clasificación es: "+ str(clasificacion))
else:
    print("La data no es correcta")