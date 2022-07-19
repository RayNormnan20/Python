#Ingreso de datos 


dias = int(input("Ingrese los dias de alquiler: "))

#Proceso

if dias > 0:
    if dias == 1:
        costoDia = 50.00
    elif dias == 2:
        costoDia =  45.00
    elif dias <= 5:
        costoDia =  40.00
    elif dias <= 10:
       costoDia =  35.00
    else:
        costoDia = 30.00

    #Mostrar resultados 
    print("El monto que pagará por hora para alquiler del automovil es:  " "S/. " + str(costoDia))

    if dias > 10:
        obsequio = "Agenda"
    else:
        obsequio ="Cuaderno"
    
    #Mostrar resultados
    print("El obsequio que recibirá es: " + str(obsequio))
    
else:
    print("El número de los dias no son correctos")


