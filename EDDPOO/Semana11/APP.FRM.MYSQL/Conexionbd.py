
import mysql.connector 

class Registro_Datos:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(
        host= 'localhost',
        database = 'bdnotas',
        user = 'root',
        password = '12345678')

    def Insertar_Curso(self, idcurso, nomcurso, credito):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO curso(idcurso, nomcurso, credito)
        VALUES ('{}','{}','{}')'''.format(idcurso, nomcurso, credito)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def Listar_Cursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM curso"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro