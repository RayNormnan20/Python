
import sys 
from PyQt5 import QtWidgets, uic

class imcApp:

    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("FrmIMC.ui")
        self.ventana.show()
        self.ventana.btnCalcular.clicked.connect(self.actionCalcularIMC) 
        app.exec()
    
    def actionCalcularIMC(self):
        peso = float(self.ventana.txtPeso.text())
        talla = float(self.ventana.txtTalla.text())
        
        imc = peso / (talla**2)


        diagnostico = ""
        if imc >= 0 and imc <= 15.99:
            diagnostico = "Delgadez severa"
        elif imc >= 16.00 and imc <= 16.99:
            diagnostico = "Delgadez moderada"
        elif imc >= 17.00 and imc <= 18.49:
            diagnostico = "Delgadez leve"
        elif imc >= 18.50 and imc <= 24.99:
            diagnostico = "Normal"
        elif imc >=25.00 and imc <= 29.99:
            diagnostico = "Sobrepeso"
        elif imc >= 30.00 and imc <= 34.99:
            diagnostico = "Obesidad Leve"
        elif imc >= 35.00 and imc <= 39.99:
            diagnostico = "Obesidad media"
        elif imc >= 40.00:
            diagnostico = "Obesidad mórbida" 

        self.ventana.lblResIMC.setText("El valor de IMC: " + str(imc) + 
        " su diagnostico es: " + diagnostico)
    
imcApp()