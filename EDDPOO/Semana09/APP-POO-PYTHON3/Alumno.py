from Persona import Persona

class Alumno(Persona):
    def __init__(self):
        super().__init__()

    def mayorEdad(self):
        if self.edad >=18:
            print("El alumno es mayor edad")
        else:
            print("El alumno de menor edad")

objAlumno = Alumno()
objAlumno.mayorEdad()