class Cuenta:


    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def imprimir(self):
        print("Titular de la cuenta: ", self.titular)
        print("Monto: ", self.monto)
