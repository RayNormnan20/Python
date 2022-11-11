from Cuenta import  Cuenta

class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.interes = interes

    def imprimir(self):
        super().imprimir()
        print("Plazo en días: ", self.plazo)
        print("Interés: ", self.interes)
        self.gananciaInteres()

    def gananciaInteres(self):
        ganancia = self.monto * self.interes / 100
        print("Importe del interés: " , ganancia)

objPlazoFijo = PlazoFijo("Jose", 2550, 120, 0.2)
objPlazoFijo.imprimir()
            