def rectangulo (alto, ancho, caracter):
    for i in range (alto):
        print(caracter * ancho)


alto = int(input("Alto: "))
ancho  =int(input("Ancho: "))
caracter = input("Caracter: ")

rectangulo(alto,ancho,caracter)