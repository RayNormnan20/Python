#Ingreso de datos 
numero= int(input("Ingrese el número entero del 1 al 4: "))

#Proceso
if numero <1 or numero >4:
   mensaje = "Numero no valido"
if numero== 1:
    mensaje= "Soltero"
if numero== 2:
    mensaje = "Casado"
if numero == 3:
    mensaje = "Viudo"
if numero== 4:
    mensaje = "Divorciado"

#Mostrar resultado
print("El estado civil de la persona es: " +str(mensaje))