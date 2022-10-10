import random

def cargarlista():
    lista = []
    for x in range (10):
        num = random.randint(1, 1000)
        lista.append(num)
    return lista

def imprimir (lista):
    print(lista)
