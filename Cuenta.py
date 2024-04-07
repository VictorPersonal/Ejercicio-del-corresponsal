class Cuenta():

    def __init__(self, numeroCuenta, saldo, cedula):
        self.numeroCuenta = numeroCuenta
        self.saldo = 0
        self.cedula = cedula

    def getnumeroCuenta(self):

        return self.numeroCuenta
    
    def setnumeroCuenta(self, numeroCuenta):
        
  
        self.numeroCuenta=numeroCuenta
        
    def getSaldo(self):

        return self.saldo
    
    def setSaldo(self, saldo):

        self.saldo=saldo
    def getCedula(self):

 

        return self.cedula
    def setCedula(self, cedula):

  

        self.cedula=cedula

        