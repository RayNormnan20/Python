from random import randint

i= 1
while True: 
    dado1 = randint (1, 6)
    dado2 = randint (1, 6)

    print("Lanzamiento # {}: Dado 1 = {}, Dado 2 = {}".format(i,dado1, dado2))

    if dado1 == 6 and dado2 ==6:
        break
    i += 1

print("Cantidad de movimientos efectuados: " + str(i))