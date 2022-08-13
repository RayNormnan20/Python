from Controlador.Productos import Producto

class ArregloProductos:

    def __init__(self):
        self.dataProductos = []
        self.cargar()
        
    
    def cargar(self):
        archivo = open("Modelo/Productos.txt","r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            codigo = columna[0]
            nombre = columna[1]
            descripcion = columna[2]
            stock_minimo = columna[3]
            stock_actual = columna[4]
            precio_costo = columna[5]
            precio_venta = columna[6]
            proveedor = columna[7]
            almacen = columna[8].strip()
            objPro = Producto(codigo, nombre, descripcion, stock_minimo,
            stock_actual,precio_costo, precio_venta, proveedor, almacen)
            self.adicionaProducto(objPro)
        archivo.close()


    def grabar(self):
        archivo = open("Modelo/Productos.txt","w", encoding = "utf-8")
        for i in range(self.tamañoArregloProducto()):
            archivo.write(str(self.devolverProducto(i).getCodigo())+ "," 
            + str(self.devolverProducto(i).getNombre()) + "," 
            + str(self.devolverProducto(i).getDescripcion()) + ","
            + str(self.devolverProducto(i).getStockMinimo()) + ","
            + str(self.devolverProducto(i).getStockActual()) + ","
            + str(self.devolverProducto(i).getPrecioCosto()) + ","
            + str(self.devolverProducto(i).getPrecioVenta()) + ","
            + str(self.devolverProducto(i).getProveedor()) + ","
            + str(self.devolverProducto(i).getAlmacen()) + "\n")
        archivo.close()

    
    def adicionaProducto(self, objPro):
        self.dataProductos.append(objPro)
    
    def devolverProducto(self, pos):
        return self.dataProductos[pos]
    
    def tamañoArregloProducto(self):
        return len(self.dataProductos)
    
    def buscarProducto(self, codigo):
        for i in range(self.tamañoArregloProducto()):
            if codigo == self.dataProductos[i].getCodigo():
                return i
        return -1
    
    def eliminarProducto(self, indice):
        del(self.dataProductos[indice])
    
    def actualizarStock(self, cantidad, codigoProducto):
        for i in range(self.tamañoArregloProducto()):
            if self.dataProductos[i].getCodigo() == codigoProducto:
                self.dataProducto[i].setStockActual(cantidad)
                
