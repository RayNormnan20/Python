


class Alumno:

    def inicializar(self, nombre, apellido,  nota, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.nota = nota
        self.telefono = telefono

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Nota: ", self.nota)
        print("Telefono: ", self.telefono)

    def mostrarEstado(self):
        if self.nota > 4:
            print("Regular")
        else:
            print("Libre")

objAlumno1 = Alumno()
objAlumno1.inicializar("Luis","Meza", 10, "974354667")
objAlumno1.imprimir()
objAlumno1.mostrarEstado()


objAlumno2 = Alumno()
objAlumno2.inicializar("Maria","Alvarez", 11, "953624354")
objAlumno2.imprimir()
objAlumno2.mostrarEstado()


objAlumno3 = Alumno()
objAlumno3.inicializar("Jimena","Luna", 4, "963251234")
objAlumno3.imprimir()
objAlumno3.mostrarEstado()