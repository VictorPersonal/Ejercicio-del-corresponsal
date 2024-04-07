from datetime import datetime
#from Cuenta import Cuenta

class Reporte():

    """
    
    En la clase reporte se analiza el total de cuentas y la información como el numero de cuenta, saldo
    y la cedula del cliente.

    Atributes:

        fecha (str): [fecha]

    
    """

    def __init__(self):

        """
        
        Este método permite crear instancias u objetos de la clase Reporte, que representa.
        
        Args: 

            Param1: fecha (str): [fecha]

        """



        self.fecha = datetime.now()


    

    def generarReporte(self,listacuentas):

        """
        
        Esta función utiliza métodos los cuales le permiten saber el número de cuentas dentro de la lista de cuentas como además permite saber la cédula y el número de cuenta de tal manera que solo se visualice los ultimos 4 digitos.
        
        Args:
            listaCuentas (list): Una lista que contiene objetos de la clase Cuenta.

        Returns:
            None

        Prints:
            - El total de cuentas en la lista.
            - Información detallada de cada cuenta, incluyendo el número de cuenta oculto, cédula oculta y saldo.
        
        """

        totalc=len(listacuentas)
        print('El total de cuentas es: ',totalc)
        print("la informacion de las cuentas:")
        for cuenta in listacuentas: #Recorre la lista de las cuentas
            nCuenta = cuenta.getnumeroCuenta() #Se crea una variable para 'obligar' al programama a que solo busque o se interese en 'getnumeroCuenta() o getCedula() o getSaldo()' y que no me imprima después todos los datos que tiene el usuario
            if nCuenta: #Si encuentra a la cuenta con el atributo de número de cuenta
                cuentaOculta = '*' * (len(nCuenta)-4)+nCuenta[-4:] #Con las variables 'cuentaOculta' 'cedulaOculta' se oculta los digitos de cuenta y cédula por '*' teniendo en cuenta que el número de digitos se reemplazará con '*' Y que en la cadena de str de ced y cuenta se eliminarán los últimos 4 digtos. PERO se agregarán posteriormente normal mostrando lo que son.
            cedula = cuenta.getCedula()
            if cedula:
                cedulaOculta= '*' * (len(cedula)-4)+cedula[-4:]
            saldo = cuenta.getSaldo()
            print("numero de cuenta:",cuentaOculta)
            print("cedula cliente:",cedulaOculta)
            print("saldo de la cuenta:",saldo)
        