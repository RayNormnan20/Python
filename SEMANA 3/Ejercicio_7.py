#Ingreso de datos

numero= int(input("Ingrese el número de 4 cifras"))

#Proceso
# abc vamosa usar como ejemplo el número 5674
millar= numero// 1000
centena= numero //100 % 10
decena= numero // 10 % 10
unidad= numero % 10

suma= millar + centena + decena + unidad
nuevoNumero= millar* 1000 + unidad * 100 + decena * 10 + centena 
#Mostrar resultados

print("suma de cifras: " + str(suma))
print("El reves del numero es: " + str(nuevoNumero))