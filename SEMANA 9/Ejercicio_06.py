
termino = 7
razonImpar = 2
razonPar = 4
suma = 0

for i in range (1,21):
    print(termino, end= " ")
    if i % 2 == 0:
        termino += razonPar
        razonPar += 1
    else:
        termino += razonImpar

    suma += i


print("\nsuma: "+ str (suma))