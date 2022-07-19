
from random import randint


cantAprobados = 0
cantDesaprobados = 0
sumaNota = 0

for i in range (40):
    nota = randint (0, 20)
    print(nota, end=" ")

    if nota >= 13:
        cantAprobados += 1
    else:
        cantDesaprobados += 1

promedio = round(sumaNota / 40, 2)


print("\nNota promedio: " + str(promedio))
print("Cantidad aprobados: ") + str(cantAprobados)
print("Cantidad desaprobados: ") + str(cantDesaprobados)