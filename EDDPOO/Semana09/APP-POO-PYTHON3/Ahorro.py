from Cuenta import Cuenta

class Ahorro(Cuenta):

    def __init__(self, titular, monto):
        super().__init__(titular, monto)

    def interes_a_ganar(self):
        if self.monto > 1000:
            print("Gana 20% de interés anual")

        else:
            print("Gana 5% de interés anual")

objAhorro = Ahorro("Luis", 900)
objAhorro.interes_a_ganar()