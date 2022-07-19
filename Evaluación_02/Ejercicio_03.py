#Ingreso de datos 
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de los productos: "))

#Proceso
importeCompra = cantidad  *  precio 

if cantidad >= 50:
    descuento = importeCompra * 25 / 100
else:
    descuento = importeCompra * 15 / 100

importePagar = importeCompra - descuento

#Mostrar resultados 
print("El importe de compra es: S/. " + str(importeCompra))
print("El importe del descuento es: S/. " + str(descuento))
print("El importe a pagar es: S/." + str(importePagar))