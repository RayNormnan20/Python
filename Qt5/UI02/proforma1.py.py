import sys
from PyQt5 import QtWidgets,uic

qtCreatorFile = "Proforma1.ui" #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)
        uic.loadUi("Proforma1.ui",self) #ruta donde esta estar la interfas UI

        #Aquí van los botones
        self.btnCalcular.clicked.connect(self.calcular)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnSalir.clicked.connect(self.salir)
        
        self.show() #Muestra la ventana

    def calcular (self):

        #Entrada de datos
        precio = float(self.txtPrecio.text())
        cantidad = int(self.spbCantidad.value())

        #Calculamos el importe
        importe = precio * cantidad

        #Calculamos el porcentaje del descuento
        porcentajeDescuento = 0    
        if self.rbMayorista.isChecked() == True:
            porcentajeDescuento = 4.5 / 100
        if self.rbMinorista.isChecked() == True:
            porcentajeDescuento = 1.9 / 100
        
        #Calculamos el descuento 
        descuento = importe * porcentajeDescuento

        #calculamos el porcentaje de interés 
        porcentajeInteres = 0
        if self.rbInteres1.isChecked() == True:
            porcentajeInteres = 0 / 100
        if self.rbInteres2.isChecked() == True:
            porcentajeInteres = 8.5 / 100
        if self.rbInteres3.isChecked() == True:
            porcentajeInteres = 12.5 / 100
        
        #Calculamos el interés
        interes = importe * porcentajeInteres

        #Calculamos el total
        total = importe - descuento + interes

        #Salida de resultados 

        self.txtImporte.setText("S/. " + str("{:.2f}".format(importe)))
        self.txtDescuento.setText("S/. " +str("{:.2f}".format(descuento)))
        self.txtInteres.setText("S/. " + str("{:.2f}".format(interes)))
        self.txtTotal.setText("S/. " + str("{:.2f}".format(total)))

        self.txtS.setText("==========".center(70))
        self.txtS.append(" PROFORMA ".center(80))
        self.txtS.append(" ==========\n".center(70))
        self.txtS.append("CÓDIGO DEL CLIENTE: " + self.txtCodigoCliente.text())
        self.txtS.append("NOMBRE DEL CLIENTE: " + self.txtNombreCliente.text() + "\n")

        self.txtS.append("PRODUCTO: " + self.txtProducto.text())
        self.txtS.append("CANTIDAD: " + str(cantidad))
        self.txtS.append("EL IMPORTE DE LA COMPRA ES: " + str(importe))
        self.txtS.append("EL DESCUENTO POR LA COMPRA ES: " + str("{:.2f}".format(descuento)))
        self.txtS.append("EL INTERÉS POR LA COMPRA ES: " + str("{:.2f}".format(interes)))
        self.txtS.append("EL TOTAL A PAGAR ES: "  + str("{:.2f}".format(total)))

    def limpiar(self):
        self.txtCodigoCliente.setText("")
        self.txtNombreCliente.setText("")
        self.txtProducto.setText("")
        self.txtPrecio.setText("")

        self.txtS.setText("")   #Para limpiar

        self.spbCantidad.setValue(0)   #Para que se limpie debe volver a 0
        self.rbInteres1.setChecked(True)
        self.rbMayorista.setChecked(True)

    def salir(self):
        self.close()
    
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()