#Ingreso de datos
numero = int(input("Ingrese un # de 5 cifras: "))



a = numero // 10000
b = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
e= numero % 10 

   

if  a == e and b == d:
    mensaje = "El numero " + str(numero) + " es capicua"
else:
    mensaje = "El numero " + str(numero) + " No es capicua"

     
#Mostrar resultados 

print(mensaje)