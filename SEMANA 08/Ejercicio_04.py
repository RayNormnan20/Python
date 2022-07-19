


i = 1
numerador = 2
denominador = 5
suma = 0
while i <= 50:
    print(str(numerador) + "/" + str(denominador), end="  ")
    suma += numerador / denominador
    numerador += 3
    denominador += 4
    i += 1
print("\nSuma: " + str(suma))