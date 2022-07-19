numerador = 3
denominador = 4
suma= 0

for i in range (10):
    print(str(numerador) + "/" + str(denominador), end="  ")
    suma += round(numerador / denominador,3)
    numerador += 2
    denominador += 3
    
print("\nSuma: " +str(suma))
