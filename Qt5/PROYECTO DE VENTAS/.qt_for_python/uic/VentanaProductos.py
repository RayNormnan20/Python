# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ProyectoPuntoDeVenta\UI\VentanaProductos.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(926, 428)
        MainWindow.setStyleSheet("background-color: rgb(21, 130, 213);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 241, 81))
        self.label.setMaximumSize(QtCore.QSize(261, 16777215))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 26pt \"News706 BT\";")
        self.label.setObjectName("label")
        self.lblCodigo = QtWidgets.QLabel(self.centralwidget)
        self.lblCodigo.setGeometry(QtCore.QRect(20, 80, 51, 21))
        self.lblCodigo.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.lblCodigo.setObjectName("lblCodigo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 51, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(410, 160, 81, 21))
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.txtCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtCodigo.setGeometry(QtCore.QRect(20, 110, 321, 20))
        self.txtCodigo.setObjectName("txtCodigo")
        self.txtNombre = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNombre.setGeometry(QtCore.QRect(20, 190, 321, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.txtDescripcion = QtWidgets.QLineEdit(self.centralwidget)
        self.txtDescripcion.setGeometry(QtCore.QRect(410, 190, 511, 20))
        self.txtDescripcion.setObjectName("txtDescripcion")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 91, 16))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 250, 71, 21))
        self.label_6.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(410, 250, 101, 21))
        self.label_7.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 250, 101, 21))
        self.label_8.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(540, 250, 71, 21))
        self.label_9.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(740, 250, 61, 21))
        self.label_10.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.txtStockMinimo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtStockMinimo.setGeometry(QtCore.QRect(20, 280, 113, 20))
        self.txtStockMinimo.setObjectName("txtStockMinimo")
        self.txtStockActual = QtWidgets.QLineEdit(self.centralwidget)
        self.txtStockActual.setGeometry(QtCore.QRect(150, 280, 113, 20))
        self.txtStockActual.setObjectName("txtStockActual")
        self.txtPrecioCosto = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecioCosto.setGeometry(QtCore.QRect(280, 280, 113, 20))
        self.txtPrecioCosto.setObjectName("txtPrecioCosto")
        self.txtPrecioVenta = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPrecioVenta.setGeometry(QtCore.QRect(410, 280, 113, 20))
        self.txtPrecioVenta.setObjectName("txtPrecioVenta")
        self.cboProveedor = QtWidgets.QComboBox(self.centralwidget)
        self.cboProveedor.setGeometry(QtCore.QRect(540, 280, 181, 22))
        self.cboProveedor.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboProveedor.setObjectName("cboProveedor")
        self.cboProveedor.addItem("")
        self.cboProveedor.addItem("")
        self.cboProveedor.addItem("")
        self.cboProveedor.addItem("")
        self.cboAlmacen = QtWidgets.QComboBox(self.centralwidget)
        self.cboAlmacen.setGeometry(QtCore.QRect(740, 280, 181, 22))
        self.cboAlmacen.setStyleSheet("color: rgb(255, 255, 255);")
        self.cboAlmacen.setObjectName("cboAlmacen")
        self.cboAlmacen.addItem("")
        self.cboAlmacen.addItem("")
        self.cboAlmacen.addItem("")
        self.cboAlmacen.addItem("")
        self.tblProductos = QtWidgets.QTableWidget(self.centralwidget)
        self.tblProductos.setGeometry(QtCore.QRect(20, 310, 901, 241))
        self.tblProductos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tblProductos.setObjectName("tblProductos")
        self.tblProductos.setColumnCount(9)
        self.tblProductos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        item.setFont(font)
        self.tblProductos.setHorizontalHeaderItem(8, item)
        self.btnRegistrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegistrar.setGeometry(QtCore.QRect(20, 560, 141, 61))
        self.btnRegistrar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/registrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRegistrar.setIcon(icon)
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnModificar = QtWidgets.QPushButton(self.centralwidget)
        self.btnModificar.setGeometry(QtCore.QRect(210, 560, 141, 61))
        self.btnModificar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnModificar.setIcon(icon1)
        self.btnModificar.setObjectName("btnModificar")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(400, 560, 141, 61))
        self.btnConsultar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/consultar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConsultar.setIcon(icon2)
        self.btnConsultar.setObjectName("btnConsultar")
        self.btnEliminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnEliminar.setGeometry(QtCore.QRect(580, 560, 141, 61))
        self.btnEliminar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEliminar.setIcon(icon3)
        self.btnEliminar.setObjectName("btnEliminar")
        self.btnListar = QtWidgets.QPushButton(self.centralwidget)
        self.btnListar.setGeometry(QtCore.QRect(750, 560, 141, 61))
        self.btnListar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/listar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListar.setIcon(icon4)
        self.btnListar.setObjectName("btnListar")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(680, 40, 151, 121))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("d:\\ProyectoPuntoDeVenta\\UI\\../IMG/carrito de compra.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.btnGrabar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGrabar.setGeometry(QtCore.QRect(210, 560, 141, 61))
        self.btnGrabar.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 26, 10);")
        self.btnGrabar.setIcon(icon1)
        self.btnGrabar.setObjectName("btnGrabar")
        self.label.raise_()
        self.lblCodigo.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.txtCodigo.raise_()
        self.txtNombre.raise_()
        self.txtDescripcion.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.txtStockMinimo.raise_()
        self.txtStockActual.raise_()
        self.txtPrecioCosto.raise_()
        self.txtPrecioVenta.raise_()
        self.cboProveedor.raise_()
        self.cboAlmacen.raise_()
        self.tblProductos.raise_()
        self.btnConsultar.raise_()
        self.btnEliminar.raise_()
        self.btnListar.raise_()
        self.btnRegistrar.raise_()
        self.label_11.raise_()
        self.btnGrabar.raise_()
        self.btnModificar.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 926, 21))
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
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "   PRODUCTOS"))
        self.lblCodigo.setText(_translate("MainWindow", "Código:"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.label_4.setText(_translate("MainWindow", "Descripción:"))
        self.label_5.setText(_translate("MainWindow", "Stock Mínimo:"))
        self.label_6.setText(_translate("MainWindow", "Stock Actual:"))
        self.label_7.setText(_translate("MainWindow", "Precio de Venta:"))
        self.label_8.setText(_translate("MainWindow", "Precio de Costo:"))
        self.label_9.setText(_translate("MainWindow", "Proveedor:"))
        self.label_10.setText(_translate("MainWindow", "Almacén:"))
        self.cboProveedor.setItemText(0, _translate("MainWindow", "Seleccionar Proveedor"))
        self.cboProveedor.setItemText(1, _translate("MainWindow", "Proveedor 1"))
        self.cboProveedor.setItemText(2, _translate("MainWindow", "Proveedor 2"))
        self.cboProveedor.setItemText(3, _translate("MainWindow", "Proveedor 3"))
        self.cboAlmacen.setItemText(0, _translate("MainWindow", "Seleccionar Almacén"))
        self.cboAlmacen.setItemText(1, _translate("MainWindow", "Almacén 1"))
        self.cboAlmacen.setItemText(2, _translate("MainWindow", "Almacén 2"))
        self.cboAlmacen.setItemText(3, _translate("MainWindow", "Almacén 3"))
        item = self.tblProductos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tblProductos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tblProductos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripción"))
        item = self.tblProductos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stock Mínimo"))
        item = self.tblProductos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock Actual"))
        item = self.tblProductos.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Precio en IGV"))
        item = self.tblProductos.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Venta en IGV"))
        item = self.tblProductos.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Proveedor"))
        item = self.tblProductos.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Almacén"))
        self.btnRegistrar.setText(_translate("MainWindow", "REGISTRAR"))
        self.btnModificar.setText(_translate("MainWindow", "MODIFICAR"))
        self.btnConsultar.setText(_translate("MainWindow", "CONSULTAR"))
        self.btnEliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.btnListar.setText(_translate("MainWindow", "LISTAR"))
        self.btnGrabar.setText(_translate("MainWindow", "GRABAR"))