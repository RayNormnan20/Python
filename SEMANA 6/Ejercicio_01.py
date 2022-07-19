#Inegreso de datos
golesA = int(input("Goles de A: "))
golesB = int(input("Goles de B: "))

#Proceso
if golesA > golesB: 
    resultado = "Ganó A"
elif golesB > golesA:
    resultado = "Ganó B"
else:
    resultado = "Empate"

#Mostrar resultados
print("El resultado del partido es: " +str(resultado))