#Ingreso de datos 
monto = float(input("Ingrese el monto de dinero a repartir: "))

#Proceso
juan = 45 / 100 * monto
pablo = 60 / 100 * juan
luis = monto - (juan + pablo)

#Mostrar resultados 
print("A juan le corresponde: " + str(juan))
print("A pablo le corresponde: " + str(pablo))
print("A luis le corresponde: " + str(luis))