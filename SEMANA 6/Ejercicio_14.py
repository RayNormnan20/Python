
#Ingreso de datos 


promedio = float(input("Ingrese el promedio del estudiante: "))

#Proceso

if promedio > 0 or promedio <= 20:
    categoria = input("Ingrese la categoría (A-B-C-D): ")
    if categoria == "A" or categoria == "B" or categoria == "C" or categoria == "D":
        if categoria == "A":
            pension = 3000
        elif categoria == "B":
            pension = 2500
        elif categoria == "C":
            pension = 2000
        else: 
            pension = 1500

        if promedio < 14:
            descuento = 0
        elif promedio < 16:
            descuento = pension * 10 / 100
        elif promedio < 18:
            descuento = pension * 12 / 100
        else:
            descuento = pension * 15 / 100

        nuevaPension = pension - descuento
        
        #Mostrar resultados
        print("La pensión actual es: " + str(pension))
        print("La nueva pensión es: " + str(nuevaPension))
    else:
        print("Categoría incorrecta")
else:
    print("El promedio ingresado es incorrecto")


