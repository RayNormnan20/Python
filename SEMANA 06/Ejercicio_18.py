codigo_del_empleado = int (input ("Ingresa el valor de codigo del empleado: "))



if codigo_del_empleado%2==0 and codigo_del_empleado%3==0 and codigo_del_empleado%5==0:
    tipoEmpleado = "Administrativo"
if codigo_del_empleado%2!=0 and codigo_del_empleado%3==0 and codigo_del_empleado%5==0:
    tipoEmpleado = "Directivo"
if codigo_del_empleado%2==0 and codigo_del_empleado%3!=0 and codigo_del_empleado%5!=0:
    tipoEmpleado ="Vendedor"
if codigo_del_empleado%2!=0 and codigo_del_empleado%3!=0 and codigo_del_empleado%5!=0:
   tipoEmpleado = "Seguridad"
print("El tipo de empleado es: " + str(tipoEmpleado))
