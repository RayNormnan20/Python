listaNotas = []

for i in range(1,6):
    nota = int(input("Ingrese la nota # " + str(i) + ": "))
    listaNotas.append(nota)


mayor = listaNotas[0]
menor = listaNotas[0]
suma = listaNotas[0]


for i in range (1,len(listaNotas)):
    if listaNotas [i] > mayor:
        mayor = listaNotas [i]
    if listaNotas [i] < menor:
        menor = listaNotas [i]
    suma += listaNotas[i]


promedio = suma / len (listaNotas)

print("Notas: ",listaNotas)
print("Nota Mayor: ",mayor)
print("Nota Menor: ",menor)
print("Promedio: ",promedio)
