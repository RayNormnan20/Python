from Controlador.Clientes import Cliente

class ArregloClientes:
    
    def __init__(self):
         self.dataClientes = []
         self.cargar()
    
    def cargar(self):
        archivo = open("Modelo/Clientes.txt","r", encoding = "utf-8")
        for linea in archivo.readlines():
            columna = str(linea).split(",")
            dniCliente = columna[0]
            nombreCliente = columna[1]
            apellidoPaternoCliente = columna[2]
            apellidoMaternoCliente = columna[3]
            direccionCliente = columna[4]
            telefonoCliente = columna[5].strip()
            objCli= Cliente(dniCliente, nombreCliente, apellidoPaternoCliente, apellidoMaternoCliente,
            direccionCliente, telefonoCliente)
            self.adicionaCliente(objCli)
        archivo.close()
    
    def grabar(self):
        archivo = open("Modelo/Clientes.txt","w", encoding = "utf-8")
        for i in range(self.tamañoArregloCliente()):
            archivo.write(str(self.devolverCliente(i).getDNI())+ "," 
            + str(self.devolverCliente(i).getNombre()) + "," 
            + str(self.devolverCliente(i).getApellidoPaterno()) + ","
            + str(self.devolverCliente(i).getApellidoMaterno()) + ","
            + str(self.devolverCliente(i).getDireccion()) + ","
            + str(self.devolverCliente(i).gettelefono()) + "\n")
        archivo.close()
      
    def adicionaCliente(self, objCli):
         self.dataClientes.append(objCli)

    def devolverCliente(self, pos):
        return self.dataClientes[pos]

    def tamañoArregloCliente(self):
        return len(self.dataClientes)

    def buscarCliente(self, dni):
        for i in range(self.tamañoArregloCliente()):
         if dni == self.dataClientes[i].getDNI():
           return i
        return -1

    def eliminarCliente(self, indice):
        del(self.dataClientes[indice])
