#Ingreso de datos 
numCuadernos = int(input("Ingrese la cantidad de los cuadernos: "))
#Proceso

if numCuadernos < 12:
    lucas = 0
    cross = 0
    novo = 0
elif numCuadernos < 24:
    lucas = numCuadernos // 4
    cross = 0
    novo = 0
elif numCuadernos < 36:
    lucas = 0
    cross = ( numCuadernos // 4 ) * 2 
    novo = 0
else:
    lucas = 1
    cross = (numCuadernos // 4 ) * 2
    novo = 1


print("Los lapiceros Lucas: " + str(lucas))
print("Los lapiceros Cross: " + str(cross))
print("Los lapiceros Novo: " + str(novo))