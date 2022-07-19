def diccionario (t):
    listaNum1 = []
    listaNum2 = list(t)
    listaNum3 = []

    for i in range(len(listaNum2)):
        listaNum1.append (listaNum2 [i] )
        listaNum3.append (listaNum2.count(listaNum2 [i] ))
    return dict(zip(listaNum1, listaNum3))


t = ("a", "b", "c", "a", "d", "b", "a", "e", "d", "e", "a", "e")
diccionarioTotal = diccionario (t)

print(diccionarioTotal)