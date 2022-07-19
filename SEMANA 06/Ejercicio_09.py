#Ingreso de datos 
fosforo= float(input("Ingrese el porcentaje de fosforo: "))

if fosforo < 0.05:
    clasificacion = "Bessemer"
elif fosforo <= 0.18:
    clasificacion = "No Bessemer"
else:
    clasificacion = "Fosforoso"


#Mostrar resultados
print("La clasificación es: "+ str(clasificacion))
