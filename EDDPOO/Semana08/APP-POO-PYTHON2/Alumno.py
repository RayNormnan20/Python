# Clase alumno   
#  La clase es única 
class Alumno():
    codigoAlumno = ""
    nombreAlumno = ""
    apellidoAlumno = ""
    edad = 0
    asistencia = False
    # Constructor 
    # _Se usa para definir los parametros
    def __init__(self, _codigoAlumno, _nombreAlumno, _apellidoAlumno, _edad):
        self.codigoAlumno = _codigoAlumno
        self.nombreAlumno = _nombreAlumno
        self.apellidoAlumno = _apellidoAlumno
        self.edad = _edad

    def datosPersonales(self):
        print(self.codigoAlumno, " ", self.nombreAlumno, " ", self.apellidoAlumno, " ", self.edad, " ", self.asistencia)

    def marcarAsistencia(self, _valorAsistencia):
        self.asistencia = _valorAsistencia

# Se puede hacer la referencia a varios objetos 
objalumno = Alumno("A001", "Jose", "Pintado", 20)
objalumno.marcarAsistencia(True)
objalumno.datosPersonales()

objalumno2 = Alumno("A002", "Jimena", "Meza", 23)
objalumno2.datosPersonales()

objalumno3 = Alumno("A003", "Francisco", "Godoy", 21)
objalumno3.datosPersonales()


