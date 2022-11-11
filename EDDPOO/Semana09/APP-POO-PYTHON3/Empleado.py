class Empleado:

    def __init__(self) :
        self.nombre = input("Ingrese el nombre del empleado: ")
        self.sueldo = float(input("Ingrese el sueldo: "))
    
    def imprimir(self):
        print("Nombre: " + self.nombre)
        print("Sueldo: " + str(self.sueldo))

    def pagarImpuesto(self):
        if self.sueldo > 3000:
            print("Debe pagra impuesto")
        else:
            print("No paga impuesto")
        
objEmpleado = Empleado()
objEmpleado.imprimir()
objEmpleado.pagarImpuesto()