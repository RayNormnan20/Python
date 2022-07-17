#Ingreso de datos 
peso= float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su estatura en mt: "))

#Proceso
imc= peso/(altura**2)

#Mostrar resultados
print("IMC: " + str(imc))
