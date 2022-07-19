
lista = []

for i in range (1,11):
    lista.append(i)
print(lista)

for elemento in lista:
    print("{}\t{}\t{}".format(elemento,(elemento**2),(elemento**3)))
