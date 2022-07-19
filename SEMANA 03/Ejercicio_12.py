#ingreso de datos 
donacion= float(input("Ingrese la cantidad de la donacion"))

#Proceso
medecinaGeneral= 45 / 100 * donacion
ginecología= 30 / 100 * donacion
Pediatría= 20 / 100  * (medecinaGeneral + ginecología) 
traumatología= donacion - (medecinaGeneral + ginecología + Pediatría)

#Mostrar resultados
print("A medicina general le corresponde: " + str(medecinaGeneral))
print("A ginecología le corresponde: " + str(ginecología))
print("A pediatría le corresponde: " + str(Pediatría))
print("A traumatología le corresponde: " + str(traumatología))
