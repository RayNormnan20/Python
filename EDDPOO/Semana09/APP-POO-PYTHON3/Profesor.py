#Herencia

from Persona import Persona

class Profesor(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo =  float(input("Ingrese el sueldo: "))
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo: " + str(self.sueldo))
    def pagarImpuesto(self):
        if self.sueldo > 2000:
            print("El profesor debe pagar impuesto")
        else:
            print("El profesor no debe pagar impuesto")

objProfesor = Profesor()
objProfesor.imprimir()
objProfesor.pagarImpuesto()
