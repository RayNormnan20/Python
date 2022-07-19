#Ingreso de datos 
horasTrabajadas= int(input("horas trabajadas"))
tarifaHoraria= float(input("Tarifa horaria"))

#Proceso
sueldoBasico= horasTrabajadas * tarifaHoraria
bonificacion= sueldoBasico * 20 / 100
sueldoBruto= sueldoBasico + bonificacion
descuento= sueldoBruto * 10 / 100
sueldoNeto= sueldoBruto - descuento

#Mostrar resultados 
print("Sueldo basico es: " + str(sueldoBasico))
print("Bonificacion es: " + str(bonificacion))
print("Sueldo bruto es: " + str(sueldoBruto))
print("Sueldo descuento es: " + str(descuento))
print("Sueldo neto es: " + str(sueldoNeto))