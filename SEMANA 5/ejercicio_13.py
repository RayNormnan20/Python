#Ingreso de datos
precio_ciento=float(input('Ingrese precio por ciento: '))
cantinda_ciento=int(input('Ingrese la cantidad por ciento de papel: '))



#Proceso

if cantinda_ciento <=5:
    descuento = precio_ciento * cantinda_ciento * 10 / 100
else:
    descuento = (precio_ciento * 5 *10 /100) + (precio_ciento * (cantinda_ciento - 5) * 15 /100)

importeBruto = precio_ciento * cantinda_ciento
importePagar = importeBruto - descuento


#Mostrar resultados 
print("El importe bruto es: S/ " + str(importeBruto))
print("El descuento es: S/ " + str(descuento))
print("El pimporte a pagar es: S/ " + str(importePagar))
