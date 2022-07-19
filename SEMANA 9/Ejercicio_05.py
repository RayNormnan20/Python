
suma = 0
termino = 3

for i in range (10):
    cuadrado = termino ** 2
    print(cuadrado, end=" ")
    termino += 1
    suma += cuadrado

print("\nsuma: "+ str (suma))
