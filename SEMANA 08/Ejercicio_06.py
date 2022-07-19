numero = int(input("Ingrese un número natural: "))

i = 1
contador = 0
while i <= numero:
    if numero % i == 0:
        print(i, end=" ")
        contador += 1
    i += 1


print("\nNúmero de divisores: " + str(contador))
