#Ingreso de datos 

compra=float(input('Ingrese compra: '))
numero_oculto=int(input('Ingrese numero oculto: '))

#Proceso
if numero_oculto%2==0 and numero_oculto >=100:
    descuento=compra*0.15
else:
    descuento=compra*0.05

total_pagar = compra-descuento


#Mostrar resultados        
print("El importe de descuento es: " + str(descuento))
print("El total a pagar es: " + str(total_pagar))


    