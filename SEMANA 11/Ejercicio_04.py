

lista = []
listaInversa = []

for i in range(5):
    cadena = input("Ingrese un texto: ")
    lista.append(cadena)



for elemento in lista:
    listaInversa.insert(0,elemento)

print(lista)
print(listaInversa)

#Se pueden usar las 2 opciones y la sda es mas fácil 
listaInversaSlice = lista [::-1]
print(listaInversaSlice)
