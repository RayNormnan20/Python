

def calcularMenor(a,b):
    if a<b:
        return a
    elif b<a:
        return b
    else:
        return "Los números son iguales"


numero1 = int(input("1er número: "))
if numero1>0:
    numero2 = int(input("2do número: "))
    if numero2>0:
        menor=calcularMenor(numero1,numero2)
        print("El menor es: ",menor)
    else:
        print("El 2do número debe ser positivo")
else:
    print("El 1er número debe ser positivo")


