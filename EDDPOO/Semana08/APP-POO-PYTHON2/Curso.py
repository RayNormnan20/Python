class Curso:

    codigoCurso = ""
    nombreCurso = ""
    creditoCurso = 0
    descripCurso = ""

    def __init__(self, _codigoCurso, _nombreCurso, _creditoCurso, _descripCurso):
        self.codigoCurso = _codigoCurso
        self.nombreCurso = _nombreCurso
        self.creditoCurso = _creditoCurso
        self.descripCurso = _descripCurso

    def inscripcion (self, codigoAlumno):
        print("Alumno registrado al curso: ", codigoAlumno)
        print("El nombre del curso es: ", self.nombreCurso)
        print("Creditos del curso: ", self.creditoCurso,)
        print("Descripcion del curso: ", self.descripCurso)

    def cantidadTemas(self):
        print("Este curso tiene 23 temas")


# haciendo la referencia a la clase Curso
objCurso = Curso("C001", "Python", 3, "Desarrollo de aplicaciones en Python")
objCurso.inscripcion("A001")
objCurso.cantidadTemas()

    