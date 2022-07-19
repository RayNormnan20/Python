

from random import randint
contador = 0

for i in range (100, 901):
    if i % 3 == 0:
        print(i, end=" ")
        contador += 1
print("\nCantidad de multiplos: " +str(contador))