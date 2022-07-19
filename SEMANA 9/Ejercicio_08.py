

posicionImpar = 2
posicionPar = 7
suma = 0

for i in range (1,26):
    if i % 2!= 0:
        suma += posicionImpar
        print(posicionImpar, end=" ")
        posicionImpar *= 2 
    else:
        print(posicionPar, end=" ")
        suma += posicionPar
        posicionPar +=2

print("\nsuma: "+ str (suma))
      
    




