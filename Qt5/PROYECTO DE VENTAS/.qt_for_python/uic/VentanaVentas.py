# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Usuario\Desktop\ProyectoPuntoDeVenta\UI\VentanaVentas.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 592)
        MainWindow.setStyleSheet("background-color: rgb(15, 125, 209);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 491, 51))
        self.label.setStyleSheet("font: 75 26pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.txtCodigoCliente = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodigoCliente.setGeometry(QtCore.QRect(20, 110, 151, 20))
        self.txtCodigoCliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCodigoCliente.setObjectName("txtCodigoCliente")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.txtCodigoProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodigoProducto.setGeometry(QtCore.QRect(20, 180, 151, 20))
        self.txtCodigoProducto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCodigoProducto.setObjectName("txtCodigoProducto")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 70, 131, 31))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.txtNombres = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombres.setGeometry(QtCore.QRect(190, 110, 251, 20))
        self.txtNombres.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNombres.setObjectName("txtNombres")
        self.txtDescripcion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDescripcion.setGeometry(QtCore.QRect(190, 180, 251, 20))
        self.txtDescripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(190, 140, 101, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 140, 51, 31))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.txtStock = QtWidgets.QLineEdit(self.centralwidget)
        self.txtStock.setGeometry(QtCore.QRect(460, 180, 91, 20))
        self.txtStock.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtStock.setObjectName("txtStock")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(570, 140, 51, 31))
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.txtPrecio = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecio.setGeometry(QtCore.QRect(570, 180, 91, 20))
        self.txtPrecio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPrecio.setObjectName("txtPrecio")
        self.txtCantidad = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCantidad.setGeometry(QtCore.QRect(680, 180, 91, 20))
        self.txtCantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCantidad.setObjectName("txtCantidad")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 140, 61, 31))
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 70, 61, 31))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.txtFecha = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFecha.setGeometry(QtCore.QRect(680, 110, 91, 20))
        self.txtFecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtFecha.setObjectName("txtFecha")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 70, 21, 31))
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.txtNumeroDocumento = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNumeroDocumento.setGeometry(QtCore.QRect(430, 80, 121, 20))
        self.txtNumeroDocumento.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNumeroDocumento.setObjectName("txtNumeroDocumento")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(290, 50, 241, 16))
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.tblDetalle = QtWidgets.QTableWidget(self.centralwidget)
        self.tblDetalle.setGeometry(QtCore.QRect(20, 270, 751, 141))
        self.tblDetalle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblDetalle.setObjectName("tblDetalle")
        self.tblDetalle.setColumnCount(6)
        self.tblDetalle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblDetalle.setHorizontalHeaderItem(5, item)
        self.btnAgregar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAgregar.setGeometry(QtCore.QRect(640, 220, 131, 41))
        self.btnAgregar.setStyleSheet("background-color: rgb(200, 38, 9);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Usuario\\Desktop\\ProyectoPuntoDeVenta\\UI\\../IMG/registrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAgregar.setIcon(icon)
        self.btnAgregar.setObjectName("btnAgregar")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(560, 440, 71, 31))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.txtSubtotal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtSubtotal.setGeometry(QtCore.QRect(650, 440, 121, 31))
        self.txtSubtotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtSubtotal.setObjectName("txtSubtotal")
        self.txtIgv = QtWidgets.QLineEdit(self.centralwidget)
        self.txtIgv.setGeometry(QtCore.QRect(650, 480, 121, 31))
        self.txtIgv.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtIgv.setObjectName("txtIgv")
        self.txtTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(650, 520, 121, 31))
        self.txtTotal.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTotal.setObjectName("txtTotal")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 480, 81, 31))
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(530, 520, 101, 31))
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);font: 10pt \"MS Shell Dlg 2\";")
        self.label_14.setObjectName("label_14")
        self.btnCenerar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCenerar.setGeometry(QtCore.QRect(20, 450, 151, 41))
        self.btnCenerar.setStyleSheet("background-color: rgb(200, 38, 9);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btnCenerar.setObjectName("btnCenerar")
        self.btnImprimir = QtWidgets.QPushButton(self.centralwidget)
        self.btnImprimir.setGeometry(QtCore.QRect(190, 450, 181, 41))
        self.btnImprimir.setStyleSheet("background-color: rgb(200, 38, 9);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btnImprimir.setObjectName("btnImprimir")
        self.btnCerrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCerrar.setGeometry(QtCore.QRect(390, 450, 131, 41))
        self.btnCerrar.setStyleSheet("background-color: rgb(200, 38, 9);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.btnCerrar.setObjectName("btnCerrar")
        self.btnBuscarCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarCliente.setGeometry(QtCore.QRect(170, 110, 16, 23))
        self.btnBuscarCliente.setObjectName("btnBuscarCliente")
        self.btnBuscarProducto = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscarProducto.setGeometry(QtCore.QRect(170, 180, 16, 23))
        self.btnBuscarProducto.setObjectName("btnBuscarProducto")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "PUNTO DE VENTA EDUSISTEM"))
        self.label_2.setText(_translate("MainWindow", "Código Cliente:"))
        self.label_3.setText(_translate("MainWindow", "Código Producto:"))
        self.label_4.setText(_translate("MainWindow", "Nombres y Apellidos:"))
        self.label_5.setText(_translate("MainWindow", "Descripción:"))
        self.label_6.setText(_translate("MainWindow", "Stock:"))
        self.label_7.setText(_translate("MainWindow", "Precio:"))
        self.label_8.setText(_translate("MainWindow", "Cantidad:"))
        self.label_9.setText(_translate("MainWindow", "FECHA:"))
        self.label_10.setText(_translate("MainWindow", "N°"))
        self.label_11.setText(_translate("MainWindow", "VENTAS DE PRODUCTOS TECNOLÓGICOS"))
        item = self.tblDetalle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nro"))
        item = self.tblDetalle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Código de Producto"))
        item = self.tblDetalle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblDetalle.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tblDetalle.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tblDetalle.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total"))
        self.btnAgregar.setText(_translate("MainWindow", "AGREGAR"))
        self.label_12.setText(_translate("MainWindow", "SUB TOTAL:"))
        self.label_13.setText(_translate("MainWindow", "  IGV (18%):"))
        self.label_14.setText(_translate("MainWindow", "TOTAL A PAGAR:"))
        self.btnCenerar.setText(_translate("MainWindow", "GENERAR VENTA"))
        self.btnImprimir.setText(_translate("MainWindow", "IMPRIMIR FACTURA"))
        self.btnCerrar.setText(_translate("MainWindow", "CERRAR"))
        self.btnBuscarCliente.setText(_translate("MainWindow", "PushButton"))
        self.btnBuscarProducto.setText(_translate("MainWindow", "PushButton"))