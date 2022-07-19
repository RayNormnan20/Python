#Ingreso de datos 

informaccion = int(input("Ingrese un numero positivo de 4 cifras: "))

#Proceso

estadoCivil = (informaccion % 10000 - informaccion % 1000) // 1000

if estadoCivil == 1:
    estado =  "Soltero"
elif  estadoCivil == 2:
    estado = "Casado"
elif  estadoCivil == 3:
    estado = "Viudo"
elif estadoCivil == 4:
  estado ="Divorciado"

edad = (informaccion % 1000 - informaccion % 10)  // 10


sexo = informaccion % 10 
if sexo == 1:
    sexo = "Femenino"
if sexo == 2:
    sexo ="Masculino"
#Mostrar resultados    

print("El estado civil es: " + str(estado))
print("La edad es: " + str(edad) + " años")
print("El sexo es: " +str(sexo))


