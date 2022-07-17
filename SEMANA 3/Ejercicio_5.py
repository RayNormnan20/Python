#Ingreso de datos

numero= int(input("Ingrese el número de 3 cifras"))

#Proceso
# abc vamosa usar como ejemplo el número 583
centena= numero // 100
decena= numero //10 % 10
unidad= numero % 10

nuevoNumero= unidad * 100 + decena * 10 + centena 
#Mostrar resultados

print("El reves del numero es: " + str(nuevoNumero))




