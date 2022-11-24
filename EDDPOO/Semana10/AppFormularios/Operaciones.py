
import sys 
from PyQt5 import QtWidgets, uic

class iniciaApp:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("FrmOperaciones.ui")
        self.ventana.show()
        self.ventana.btnCalcular.clicked.connect(self.actionCalcular)
        
        app.exec()
    
    def actionCalcular(self):
        numero1 = int(self.ventana.txtNum1.text())
        numero2 = int(self.ventana.txtNum2.text())

        suma = numero1 + numero2
        resta = numero1 - numero2
        multiplicacion = numero1 * numero2
        division = numero1 / numero2
        #self.ventana.lblResSuma.setText("Hola mundo")

        self.ventana.lblResSuma.setText("El resultado de la suma es: " + str(suma))
        self.ventana.lblResResta.setText("El resultado de la resta es: " + str(resta))
        self.ventana.lblResMultiplicacion.setText("El resultado de la multiplicación es: " + str(multiplicacion))
        self.ventana.lblResDivision.setText("El resultado de la división es: " + str(division))

iniciaApp()