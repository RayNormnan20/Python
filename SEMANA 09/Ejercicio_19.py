from random import randint

sumaEdades = 0
cantMenorIgual = 0
cantMayores = 0


for i in range (45):
    edad = randint(18,70)
    if edad > 30:
        cantMayores += 1
    else:
        cantMenorIgual +=1
    sumaEdades += edad

promedio = round(sumaEdades / 45,2)


print("Cantidad de mayores a 30: " + str(cantMayores))
print("Cantidad de menores o igualesa 30: " + str(cantMenorIgual))
print("Promedio: " + str(promedio))