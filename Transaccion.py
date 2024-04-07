class Transaccion():

    def __init__(self, numeroTransacccion, numeroCuenta, monto):
        self.numeroTransaccion = Transaccion.numeroTransaccion 
        self.numeroCuenta = numeroCuenta
        self.monto = monto
        
      
    def getnumeroTransaccion(self):
        return self.numeroTransaccion
    
    def setnumeroTransaccion(self, numeroTransacccion):
        self.numeroTransaccion=numeroTransacccion

    def getCuenta(self):
        return self.numeroCuenta
    
    def setCuenta(self, numeroCuenta):
        self.numeroCuenta=numeroCuenta

    def getMonto(self):
        return self.monto
    
    def setMonto(self, monto):
        self.monto= monto
    
    def realizarTransaccion(listaCuentas, deposito=True):
        pass