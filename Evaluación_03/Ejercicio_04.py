from random import randint

contador = 0
numMayor = 0
numMenorIgual = 0

while True:
    numero  = randint(500, 1500)
    contador += 1
    print(numero, end =" ")
    if numero > 1000:
        numMayor += 1
    else:
        numMenorIgual += 1

    if numero % 2!= 0 and numero > 1000 and numero < 1050:
        break

print("\nCantidad de números mayores a 1000: " + str(numMayor))
print("Cantidad de números menores o iguales a 1000: " + str(numMenorIgual))