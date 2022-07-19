numerador = 1
denominador = 1
suma= 0

for i in range (30):
    print(str(numerador) + "/" + str(denominador), end="  ")
    suma += round(numerador / denominador,2)
    numerador += 5
    denominador += 4
    
print("\nSuma: " +str(suma))
