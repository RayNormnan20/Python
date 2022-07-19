#Ingreso de datos 
número = int(input("Ingrese un número del (1-4): "))


#Proceso

if número == 1 or número == 2 or número == 3 or número == 4:
    if número == 1:
       estadoCivil= "Soltero"
    elif número == 2:
       estadoCivil= "Casado"
    elif número == 3:
        estadoCivil= "viudo"
    else: 
        estadoCivil = "Divorciado"

    #Mostrar resultados 
    print("El estado Civil es: " + str(estadoCivil))
else:
    print("La data ingresada no es correcta. ")
    
