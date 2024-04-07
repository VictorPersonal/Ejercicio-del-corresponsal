from Transaccion import Transaccion

class Deposito():
    def realizarTransaccion(listaCuentas):
        Transaccion.realizarTransaccion(listaCuentas, deposito=True)
