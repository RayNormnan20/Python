

def separarParesIMpares (lista):
    listaPares = []
    listaImpares = []
    for elemento in lista:
        if elemento % 2 == 0:
            listaPares.append(elemento)
        else:
            listaImpares.append(elemento)

    return sorted(listaPares),sorted(listaImpares)

lista = [6,5,2,1,7,3,8,9,12,32,43,22]

pares , impares = separarParesIMpares(lista)

print(pares)
print(impares)