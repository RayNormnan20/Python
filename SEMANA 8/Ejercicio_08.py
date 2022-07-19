from random import randint

suma = 0
contPares = 0
contImpares = 0
sumaPares = 0
sumaImpares = 0

while True:
    numero = randint(100,999)
    if numero % 2 == 0:
        contPares += 1
        sumaPares += numero
    else:
        contImpares += 1
        sumaImpares += numero

    suma += numero
    print(numero, end=" ")

    if numero % 2 == 0 and numero >= 500:
        break

print("\nSuma: " + str(suma))
print("Cantidad de pares: " + str(contPares))
print("Cantidad de impares: " + str(contImpares))
print("Suma de pares: " + str(sumaPares))
print("Suma de impares: " + str(sumaImpares))