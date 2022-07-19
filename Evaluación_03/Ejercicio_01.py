numerador = 1
denominador = 2
suma= 0

for i in range (50):
    print(str(numerador) + "/" + str(denominador), end="  ")
    suma += round(numerador / denominador,3)
    numerador += 4
    denominador *= 3
    
print("\nSuma: " +str(suma))