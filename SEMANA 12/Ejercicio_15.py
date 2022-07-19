def factorial(n):
    producto = 1
    for i in range (n,0,-1):
        producto *= i
    return producto

numero = int(input("Ingrese un número: "))
print("El factorial de {} es: {}".format(numero,factorial(numero)))