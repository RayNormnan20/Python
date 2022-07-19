#Ingreso de datos
matematicas=int(input("Matemáticas: "))
lenguaje=int(input("Lenguaje: "))
historia=int(input("Historia: "))
#proceso
propina = 100 

if matematicas >= 13:
    propina += 20 #propina = propina +20
if lenguaje >= 13:
    propina += 20 #propina = propina +20
if historia >= 13:
    propina += 20 #propina = propina +20
#Mostrar resultado
print("Propina: "+str(propina))