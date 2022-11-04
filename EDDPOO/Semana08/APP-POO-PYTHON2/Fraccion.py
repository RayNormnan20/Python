class Fraccion:
    numerador = 3
    denominador = 4

    def imprime(self):
        print(self.numerador,"/", self.denominador)

    def suma(self):
        print(self.numerador + self.denominador)

    def fraccion(self):
        print(self.numerador * self.denominador)

fracc = Fraccion()
fracc.imprime()
fracc.suma()
fracc.fraccion()

