from random import randint
contador = 0
sumaNotas = 0
aprobado = 0
desaprobado = 0
 
for i in range(1,41):
    nota=randint(0,100)
    contador += 1
    print("Nota {}: {}".format(i,nota))
    if nota  < 70:
        desaprobado += 1
    else: 
        aprobado +=1
    sumaNotas += nota
    
promedio=round(sumaNotas/40,2)


print("\nLa cantidad de notas generados es: " + str(contador))
print("La nota promedio es: " + str(promedio))
print("Los alumnos aprobados son: " + str(aprobado))
print("Los alumnos desaprobados: " + str(desaprobado))


