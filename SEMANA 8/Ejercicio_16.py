
from random import randint

contador = 0
notaMin = 0
notaMax = 0
sumaNotas = 0

while True:
    nota = randint(1,45)
    contador += 1
    sumaNotas += nota
    print(nota, end=" ")


    if notaMin < notaMax:
        notaMin += 1
    else:
        notaMax += 1

    if sumaNotas == 45:
        break

promedio = sumaNotas / contador

print("\nLa nota promedio es: " +str(promedio) )
print("La nota minima es: " +str(notaMin))
print("La nota maxima es: " +str (notaMax))



