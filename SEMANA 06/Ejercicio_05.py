#Ingreso de datos 

unidades = int(input("Ingrese la cantidad en unidades: "))


#Proceso
if unidades > 0:
    codigo = int(input("Ingrese código del producto (101-102-103): "))
    if codigo == 101 or codigo == 102 or codigo == 103:
        if codigo == 101:
           precio = 17.5
        elif codigo == 102:
           precio  = 25
        elif codigo == 103:
           precio  = 15.5

        importeCompra= precio  * unidades

        if  unidades <= 10:
            descuento = importeCompra * 5 / 100
        elif unidades <= 20:
           descuento = importeCompra * 7.5 / 100
        else:
           descuento = importeCompra * 10 / 100

        importepagar = importeCompra -  descuento

        #Modtrar resultados 
        print("El importe compra es: S/ " + str(importeCompra))
        print("El descuento es: S/ " + str(descuento))
        print("El importe a pagar es: S/ " + str(importepagar))
    else:
      print("Codigo no valido")
else:
   print("Cantidad de unidades no valida")



