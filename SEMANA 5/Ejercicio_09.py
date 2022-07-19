#Ingreso de datos

sexo =  int(input("Ingrese el sexo Masculino (M) , Femenino (F): "))
edad = int(input("Ingrese la edad: "))

#Proceso
if sexo == "F":
  if edad < 23:
   categoría = "FA"
else:
  categoría=  "FB"

if sexo == "M":
  if edad <25:
    categoría = "MA"
else: 
    categoría= "MB"


print("Categoria: " + categoría)

