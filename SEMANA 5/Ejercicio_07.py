#Ingreso de datos
donacion = float(input("Ingrese el monto de la donacion: "))

#Proceso
if donacion >= 10000:
    centroSalud = donacion * 30 / 100
    comedorNiños= donacion * 50 / 100
    bolsa = donacion - (centroSalud + comedorNiños)

else:
    centroSalud = donacion * 25 / 100
    comedorNiños = donacion * 60 / 100
    bolsa = donacion - (centroSalud + comedorNiños)

#Mostrar resultados 
print("Centro de salud: " + str(centroSalud))
print("Comedor de niños: " + str(comedorNiños))
print("La bolsa: " + str(bolsa))