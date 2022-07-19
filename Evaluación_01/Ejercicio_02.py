
#Ingreso de datos 

número = int(input("ingrese el número de 5 cifras: "))

#Proceso
a = número //10000
b = número //1000%10
d=  número //10%10
e=  número //1%10

#Mostrar resultados
print(str(a) + str(b) + str(d) + str(e))