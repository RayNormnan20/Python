#Ingreso de datos
ImporteVendido= float(input("Ingrese la cantidad de dinero"))

#Proceso
sueldoBasico= 750
comision= ImporteVendido * 10 / 100
sueldoBruto= sueldoBasico + comision
descuento= sueldoBruto * 15 / 100
sueldoNeto= sueldoBruto - descuento

#Mostrar resultados
print("sueldo basico es: " + str(sueldoBasico))
print("La comision es: " + str(comision))
print("sueldo bruto es: " + str(sueldoBruto))
print("descuento es: " + str(descuento))
print("sueldo neto es: " + str(sueldoNeto))