#Ingreso de datos
nota = int(input("Ingrese la nota: "))


#Proceso
if nota <=1 or nota > 20:
   nota= "Nota no es valida"
if nota < 11:
    nota +=2
if nota ==20:
    nota= 20

#Mostrar resultados 
print("La nota es: " +str(nota))

