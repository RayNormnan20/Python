#Ingreso de datos
horasTrabajadas= float(input("Ingrese horas trabajadas: "))
tarifaHoraria= float(input("Ingrese tarifa horaria: "))

#Proceso
sueldoBruto= horasTrabajadas * tarifaHoraria
descuentoEsSalud=  11.5 / 100 * sueldoBruto
descuentoONP= 12.5 / 100 * sueldoBruto
descuentoTotal= descuentoONP + descuentoEsSalud
sueldoNeto= sueldoBruto - descuentoTotal

#Mostrar resultadoss
print("El sueldo bruto es: " + str(sueldoBruto))
print("El descuento de EsSalud es: " + str(descuentoEsSalud))
print("El descuento de ONP es: " + str(descuentoONP))
print("el descuento total es: " + str(descuentoTotal))
print("El sueldo neto es: " + str(sueldoNeto))


 