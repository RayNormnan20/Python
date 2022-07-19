#Ingreso de datos 
mntsTardanza = float(input("Ingrese los minutos de tardanza: "))

#Proceso
if mntsTardanza >= 0:
    observaciones= int(input("Ingrese la cantidad de observaciones: "))
    if  observaciones == 0 or observaciones == 1 or observaciones == 2 or observaciones == 3 or observaciones > 3:
        if mntsTardanza == 0:
            puntajePuntualidad = 10
        elif mntsTardanza <= 2:
            puntajePuntualidad = 8
        elif mntsTardanza <= 5:
            puntajePuntualidad = 6
        elif mntsTardanza <= 9:
            puntajePuntualidad = 4
        else:
            puntajePuntualidad = 2

        if observaciones == 0:
            puntajeRendimiento= 10
        elif observaciones == 1:
            puntajeRendimiento = 8
        elif observaciones == 2:
            puntajeRendimiento = 5
        elif observaciones == 3:
            puntajeRendimiento = 1
        else:
            puntajeRendimiento = 0

        puntajeTotal =  puntajePuntualidad + puntajeRendimiento 

        if puntajeTotal < 11:
            bonificacion = puntajeTotal * 2.5 
        elif puntajeTotal <= 13:
            bonificacion = puntajeTotal * 5.0
        elif puntajeTotal <= 16:
            bonificacion = puntajeTotal * 7.5
        elif puntajeTotal <= 19:
            bonificacion = puntajeTotal * 10.0
        elif puntajeTotal == 20:
            bonificacion = puntajeTotal * 12.5
        
        #Mostrar resultados
        print("El puntaje por puntualidad es: " + str(puntajePuntualidad))
        print("El puntaje por rendimiento es: " + str(puntajeRendimiento))
        print("El puntaje total es: " + str(puntajeTotal))
        print("El bonificación es: " + " S/. " + str(bonificacion))        
    else:
        print("Observaciones incorrectas")     
else:
    print("Cantidad de unidades no valida")



