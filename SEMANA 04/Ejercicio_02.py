#Ingreso de datos
equipoA= int(input("Goles del equipo \"A\": "))
equipoB= int(input("Goles del equipo \"B\": "))


#Proceso
if equipoA > equipoB:
    resultado=  "Ganó el equipo \"A\""
if equipoB > equipoA:
    resultado= "Ganó equipo \"B\""
if equipoA == equipoB:
    resultado= "Empate"



#Mostrar resultados 
print("el resultado del partido es: " + str(resultado))

