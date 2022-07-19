from random import randint

contador = 0
a = 9
b = 100

while True:
    numero = randint (10, 99)
    contador += 1
    print("El número #{} es {}:".format(contador, numero))

    if numero > a:
        a = numero
    elif numero < b:
        b = numero

    decenas = numero // 10 % 10
    unidades = numero % 10 

    if decenas + unidades == 3 or decenas + unidades ==5:
        break

print("\nLa cantidad de números generados es: " + str(contador))
print("El mayor número generado: " + str(a))
print("El menor número generado: " + str(b))
