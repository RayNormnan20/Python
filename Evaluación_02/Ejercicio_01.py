
#Ingreso de datos 

nota1=float(input("Ingrese la primera nota: "))
nota2=float(input("Ingrese la segundo nota: "))
nota3=float(input("Ingrese la tercer nota: "))
ExamenP=float(input("Ingrese Examen Parcial: "))
ExamenF=float(input("Ingrese Examen Final: "))

#Proceso
if nota1 < nota2 and nota2 < nota3:
    menor = nota1
    PP= (nota2 + nota3) / 2
elif nota2 < nota1 and nota2 < nota3:
    menor = nota2
    PP= (nota1+nota3) / 2
else: 
    menor = nota3
    PP= (nota1 + nota2) / 2

PP = PP * 20 / 100
Parcial = ExamenP  * 30 / 100
Final = ExamenF * 50 / 100
PromedioFinal = PP + Parcial + Final


#Mostrar resultados 

print("La que se elimina  es: " + str(menor))
print("El promedio es: " + str(PromedioFinal))