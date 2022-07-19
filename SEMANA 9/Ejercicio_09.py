

posicionImpar = 0
posicionPar = 1
suma = 0

for i in range (1,26):
    if i % 2!= 0:
        suma += posicionImpar
        print(posicionImpar, end=" ")
        posicionImpar *= 3
    else:
        print(posicionPar, end=" ")
        suma += posicionPar
        posicionPar **= 2 - 3


print("\nsuma: "+ str (suma))