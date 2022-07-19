
from random import randint


sumaSueldos = 0
contador = 0
contMayor = 0
contMenorIgual = 0

while True:
    sueldo  = randint(2500, 3500)
    contador += 1
    sumaSueldos += sueldo
    print("Sueldo # {}: {}" . format(contador, sueldo))
    if sueldo < 3000:
        contMayor += 1
    else:
        contMenorIgual += 1
        
    if sueldo == 2500 or sueldo == 3500:
        break

    promedio = round(sumaSueldos / contador,2)

print("\nSueldo promdio: " + str(promedio))
print("Cantidad de sueldos mayores a 3000: " + str(contMayor))
print("CAntidad de sueldos menores a iguales a 3000: " + str(contMenorIgual))