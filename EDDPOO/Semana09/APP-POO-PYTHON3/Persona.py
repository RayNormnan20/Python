class Persona:

    def __init__(self) :
        self.dni = input("Ingrese su DNI: ")
        self.nombre = input("Ingrese su nombre: ")
        self.apellido = input("Ingrese su apellido: ")
        self.edad = int(input("Ingrese su edad: "))

    def imprimir(self):
        print("Datos del objeto: " + self.dni, self.nombre, self.apellido, self.edad)

#objPersona = Persona()
#objPersona.imprimir()
