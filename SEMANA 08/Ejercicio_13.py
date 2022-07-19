
from random import randint

i= 1
while True: 
    dado1 = randint (1, 6)
    dado2 = randint (1, 6)
    dado3 = randint (1, 6)
    print("Lanzamiento # {}: Dado 1 = {}, Dado 2 = {}, Dado 3 = {}".format(i,dado1, dado2, dado3))

    if dado1 == dado2  and dado2 == dado3:
        break
    i += 1
print("Cantidad de movimientos efectuados: " + str(i))