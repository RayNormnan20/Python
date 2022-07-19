#Ingreso de datos
categoría = input("Ingrese la categoría (A-B-C-D): ")
horasTrabajadas = int(input("Ingrese las horas trabajadas: "))

#Proceso
if categoría == "A":
    tarifaHoraria = 21 
elif categoría == "B":
    tarifaHoraria = 19.5 
elif categoría == "C":
    tarifaHoraria = 17 
else: 
    tarifaHoraria = 15.5
    
sueldoBruto = horasTrabajadas * tarifaHoraria

if sueldoBruto > 2500:
    descuento = sueldoBruto * 20 / 100
else:
    descuento = sueldoBruto * 15 / 100

sueldoNeto = sueldoBruto - descuento

#Mostrar resultados
print("El sueldo bruto es: " + str(sueldoBruto))
print("Descuento es: " + str(descuento))
print("El sueldo neto es: " + str(sueldoNeto))