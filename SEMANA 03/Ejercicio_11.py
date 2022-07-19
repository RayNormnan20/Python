#Ingreso de datos
ImporteVendido= float(input("Ingrese la cantidad de dinero: "))

#Proceso
sueldoBasico = 750
comision = ImporteVendido * 10 / 100
sueldoBruto = sueldoBasico + comision
descuento = sueldoBruto * 15 / 100
sueldoNeto = sueldoBruto - descuento

#Mostrar resultados
print("sueldo basico es: S/. " + str(sueldoBasico))
print("La comision es: S/. " + str(comision))
print("sueldo bruto es: S/. " + str(sueldoBruto))
print("descuento es: S/. " + str(descuento))
print("sueldo neto es: S/. " + str(sueldoNeto))