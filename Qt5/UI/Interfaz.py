#Constructor del llamdo de la interfaz
import sys
from PyQt5 import QtWidgets,uic

qtCreatorFile = "interfaz.ui" #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("interfaz.ui",self) #ruta donde esta estar la interfas UI
        self.btnSalir.clicked.connect(self.salir)
        self.btnProcesar.clicked.connect(self.procesar)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.show() #Muestra la ventana
    
    def procesar(self):
        self.lblTitulo.setText("Hola a todos...!!!")
    def limpiar(self):
        self.lblTitulo.setText("Pulsa otra vez...!!!")
    def salir(self):
        self.close()
        
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()

