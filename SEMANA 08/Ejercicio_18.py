
from random import randint



i = 1
print("Nota\tHistograma")

while i <= 30:
    nota = randint (0,20)
    print(str(nota) + "\t" + "*"*nota)
    i += 1