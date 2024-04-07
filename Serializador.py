from Cuenta import Cuenta
class SerializadorCuenta():
  
    
    def __init__(self):
        self.archivo=open("Cuenta.txt", "a")

    def getArchivo(self):
        return self.archivo
    
    def escribirArchivoCuenta(self, texto):

        self.archivo=open("Cuenta.txt","a")
        self.archivo.write(texto)
        self.archivo.close()

    def eliminarArchivoCuenta(self, texto):
    
        self.archivo=open("Cuenta.txt","w")
        self.archivo.write(texto)
        self.archivo.close()
    

    def leerArchivoCuenta(self):

        numeroCuenta=""
        saldo=0.0
        cedula=""
        i=0
        listaCuentas=[]
        self.archivo=open("Cuenta.txt","r")
        for linea in self.archivo:
            if(i==0):
                numeroCuenta = linea.strip()
                i+=1
            elif(i==1):
                saldo = float((linea.strip()))
                i+=1   
            else:
                cedula = linea.strip()
                i=0
                cuentaNueva=Cuenta(numeroCuenta, saldo, cedula)
                listaCuentas.append(cuentaNueva)
        self.archivo.close()
        return listaCuentas
    
