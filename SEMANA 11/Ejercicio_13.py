lista = [1, 4, 45, 8, 10, 15]


ordenada = True
for i in range (1,len(lista)):
    if lista [i] < lista [i-1]:
        ordenada =False
        break
if ordenada:
    print("La lista está ordenada de forma ascendente")
else:
    print("La lista NO está ordenada en forma ascendente")