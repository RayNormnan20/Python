
def numEnteropositivo(numero):
    if numero > 0:
        return len(str(numero))
    else:
        return -1

numero = int(input("Ingrese el número positivo: "))

print(numEnteropositivo(numero))