from Usuario import Usuario
from Reporte import Reporte
from Deposito import Deposito
from Analizador import Analizador
from Retiro import Retiro
from Cliente import Cliente
from Transaccion import Transaccion
from Cuenta import Cuenta #Importamos la clase cuenta porque tiene los atributos necesarios para crear una cuenta 'numeroCuenta' y 'cedula'.
from Serializador import SerializadorCuenta
from SerializadorCliente import SerializadorCliente

class corresponsal(Usuario):
    
    def __init__(self,nombre, apellido, cedula, telefono, correo_electronico, nombreCorresponsal, direccionCorresponsal): #Definimos los atributos necesarios de la clase heredera

        Usuario.__init__(self, nombre, apellido, cedula, telefono, correo_electronico) #Hereda la clase 'Corresponsal' de 'Usuario'
        self.nombreCorresponsal = nombreCorresponsal #Atributos que solo tiene la clase 'Corresponsal'
        self.direccionCorresponsal = direccionCorresponsal #Definimos los atributos necesarios de la clase heredera
         #Se crearo listas que a su vez son atributos de 'Corresponsal'
        self.serializador=SerializadorCuenta()
        self.serializadorCliente=SerializadorCliente()
        self.cuentas = self.serializador.leerArchivoCuenta()

    def crearCliente(self, listaClientes, nombre, apellido, cedula, telefono, correo_electronico):


        nuevoCliente = Cliente(nombre, apellido, cedula, telefono, correo_electronico) #Se creo un objeto que va ha ser prácticamente el elemento que se guardará en la lista con los datos ingresados con el input
        listaClientes.append(nuevoCliente)
        self.serializadorCliente.escribirCliente(nombre+"\n")
        self.serializadorCliente.escribirCliente(apellido+"\n")
        self.serializadorCliente.escribirCliente(cedula+"\n")
        self.serializadorCliente.escribirCliente(telefono+"\n")
        self.serializadorCliente.escribirCliente(correo_electronico+"\n")
        
        
        print("Cliente creado con éxito. Los datos del cliente son:\nNombre del cliente: {}\nApellido: {}\nCédula: {}\nTeléfono: {}\nCorreo electrónico: {}\n".format(nombre, apellido, cedula, telefono, correo_electronico))
    
    def eliminarCliente(self, listaClientes):
            texto=""
            for cliente in listaClientes:
                texto+=cliente.getNombre()+"\n"
                texto+=cliente.getApellido()+"\n"
                texto+=cliente.getCedula()+"\n"
                texto+=cliente.getTelefono()+"\n"
                texto+=cliente.getCorreoElectronico()+"\n"
            self.serializadorCliente.eliminarCliente(texto)

    def crearCuenta(self, listaCuentas, numeroCuenta, saldo, cedula):
        cuentaNueva=Cuenta(numeroCuenta, saldo, cedula)
        listaCuentas.append(cuentaNueva)
        self.serializador.escribirArchivo(numeroCuenta+"\n")#Dentri del archivo de 'cuenta.txt' se escribiran el numeroCuenta el 'saldo' = a 0 y la 'cedula'
        self.serializador.escribirArchivo("0"+"\n")
        self.serializador.escribirArchivo(cedula+"\n")
        print("Cuenta creada con éxito!")

    def eliminarCuenta(self, listaCuentas):

            texto=""
            for cuenta in listaCuentas:
                texto+=cuenta.getnumeroCuenta()+"\n" 
                texto+=str(cuenta.getSaldo())+"\n"
                texto+=cuenta.getCedula()+"\n"
            self.serializador.eliminarArchivoCuenta(texto)
            
    

    def realizarDeposito(self, listaCuentas): #No se le agregan argumentos a la funcion porque DENTRO DE LA MISMA se le asignatian 
        texto="" 
        for cuenta in listaCuentas:
            texto=texto+cuenta.getnumeroCuenta()+"\n"
            texto=texto+str(cuenta.getSaldo())+"\n"
            texto=texto+cuenta.getCedula()+"\n"
        self.serializador.eliminarArchivoCuenta(texto)
             
    def realizarRetiro(self,listaCuentas):
        texto=""
        for cuenta in listaCuentas:
            texto+=cuenta.getnumeroCuenta()+"\n" 
            texto+=str(cuenta.getSaldo())+"\n"
            texto+=cuenta.getCedula()+"\n"
        self.serializador.eliminarArchivoCuenta(texto)


    def generarInforme(self):
        
        reporteCuentas=Reporte()
        reporteCuentas.generarReporte(self.cuentas)
                
            
    



        
