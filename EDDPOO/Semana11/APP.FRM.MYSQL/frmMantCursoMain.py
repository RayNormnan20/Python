
import sys 
from PyQt5 import QtWidgets , uic
from Conexionbd import *
from PyQt5.QtWidgets import QTableWidgetItem

class frmMantCursoMain :
    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("frmMantCurso.ui")
        self.ventana.show()
        self.datosTotal = Registro_Datos()
        app.exec()

frmMantCursoMain()