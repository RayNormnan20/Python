#Ingreso de datos 

donación= float(input("Ingrese el monto de la donación: "))

#Proceso
talleres=  20 / 100 * donación 
biblioteca= 25 / 100 * donación 
investigación= 45 / 100 * biblioteca
becas= 75 / 100 * (talleres + investigación)
deportes= donación - (talleres + biblioteca + investigación + becas)

#Mostrar resultados 
print("A Talleres le corresponde: " + str(talleres))
print("A biblioteca le corresponde: " + str(biblioteca))
print("A investigación le corresponde: " + str(investigación))
print("A becas le corresponde: " + str(becas))
print("A deportes le corresponde: " + str(deportes))




















