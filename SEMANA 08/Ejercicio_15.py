from random import randint

sumaEdades = 0
contador = 0
edadMayor = 0
edadMenor = 0

while True:
    edad = randint(14,70)
    contador += 1
    sumaEdades += edad
    print("Edad nº {}: {}" . format(contador, edad))
    if edad < 18:
        edadMenor += 1
    else:
        edadMayor += 1

    if edad > 45 and edad < 50:
        break
    promedio = round(sumaEdades / contador,2)

print("\nLa edad promedio: " + str(promedio))
print("Cantidad de personas mayores de edad: " + str(edadMayor))
print("Cantidad de personas menores de edad: " + str(edadMenor))

