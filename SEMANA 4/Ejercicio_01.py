#Ingreso de datos
numero = int(input("Ingrese el número entero: "))



#Proceso
if numero >0:
    signo = "Positivo"
if numero < 0:
    signo= "Negativo"
if numero==0:
    signo= "Cero"


#Mostrar resultados 
print("Signo: " + signo)