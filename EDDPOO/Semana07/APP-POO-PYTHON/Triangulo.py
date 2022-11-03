class Triangulo:

    def inicializar(self):
        self.lado1 = int(input("Ingrese primer lado: "))
        self.lado2 = int(input("Ingrese segundo lado: "))
        self.lado3 = int(input("Ingrese tercer lado: "))

    def imprimir (self):
        print("========================================")
        print("Valores de los lados de los triangulos: ")
        print("========================================")

        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)

    def ladoMayor(self):
        print("Lado Mayor: ")
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

triangulo = Triangulo()
triangulo.inicializar()
triangulo.imprimir()
triangulo.ladoMayor()

