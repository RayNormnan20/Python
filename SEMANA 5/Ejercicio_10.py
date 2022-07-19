#Ingreso de datos 
importeVendido = float(input("Importe vendido: "))
numHijos = int(input("Número de hijos: "))

#Proceso
sueldoBasico = 600

if importeVendido > 15000:
    comision = importeVendido * 7 / 100
else:
    comision = importeVendido * 5 / 100

if numHijos < 5:
    bonificacion = numHijos *  25
else:
    bonificacion = numHijos * 22

sueldoBruto = sueldoBasico + comision + bonificacion

if sueldoBruto > 3500:
    descuento = sueldoBruto * 15 / 100
else: 
    descuento = sueldoBruto * 11 / 100

sueldoNeto = sueldoBruto - descuento

#Mostrar resultados 

print("ELa comisión es: S/ " + str(comision))
print("La bonificacion es: S/ " + str(bonificacion))
print("El sueldo bruto es: S/ " + str(sueldoBruto))
print("El descuento es: S/ " + str(descuento))
print("El sueldo neto es: S/ " + str(sueldoNeto))

