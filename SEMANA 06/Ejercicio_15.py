#Ingreso de datos 
CantidadChocolates = int(input("Ingrese la cantidad de chocolates: "))

#Proceso
if CantidadChocolates >= 1:
    tipoChocolate = int(input("Ingrese el tipo de chocolate (1-2-3-4): "))
    if tipoChocolate == 1 or  tipoChocolate == 2 or  tipoChocolate == 3 or tipoChocolate == 4:
        if tipoChocolate == 1:
            precioUnitario = 8.50
        elif tipoChocolate == 2:
            precioUnitario = 10.00
        elif tipoChocolate ==3:
            precioUnitario = 7.00
        elif tipoChocolate == 4:
            precioUnitario = 12.50 

        importCompra = precioUnitario * CantidadChocolates

        if CantidadChocolates < 5:
            descuento = importCompra * 4 / 100
        elif CantidadChocolates < 10:
            descuento = importCompra * 6.5 /100
        elif CantidadChocolates  < 15:
            descuento = importCompra * 9 / 100
        else:
            descuento = importCompra * 11 / 100
        
        importePagar = importCompra - descuento
    
        if importePagar >= 250:
            obsequio= CantidadChocolates * 3
        else:
            obsequio= CantidadChocolates * 2
              
        print("El importe compra es: S/ " + str(importCompra))
        print("El importe a pagar es: S/ " + str(importePagar))
        print("El descuento es: S/ " + str(descuento))
        print("La cantidadd de caramelos de obsequio es: " + str(obsequio) + " Caramelos" )
    else:
        print("Tipo  no valido")
else:
    print("Cantidad  no valida")

