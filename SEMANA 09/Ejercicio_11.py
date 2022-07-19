
numerador = 1
denominador = 2
suma= 0

for i in range (20):
    print(str(numerador) + "/" + str(denominador), end="  ")
    suma += round(numerador / denominador,3)
    numerador += 3
    denominador += 2
    
print("\nSuma: " +str(suma))