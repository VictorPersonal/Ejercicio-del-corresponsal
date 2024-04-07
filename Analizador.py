from datetime import datetime

class Analizador():
    """

    Esta clase representa un analizador de cuentas, donde calcula en sí el saldo promedio dentro de la lista de cuentas.
    Atributes:
        fecha (str)=[Fecha actual]  
    
    """
    def __init__(self):
        """
        Este método permite crar instancias u objetos de la clase Analizador, que representa.
        Args:
            param1: fecha(str): [fecha actual]
        
        """
        self.fecha = datetime.now()

    def getFecha(self):
        
        """
        
        Este metodo permite consultar la fecha de análisis.
        
        Args:

        Returns: 
            fecha (str): [fecha]

        """
        
        return self.fecha
        
    
    def calcularSaldoPromedio(self, lista):#Como no se le coloco de atributo la lista cuentas como 'self.cuentas' entonces accedemos a ella con el nombre de lista
        
        """
        
        Este método permite calcular el promedio del total/suma de los saldos de cada una de las cuentas, con la ayuda de un ciclo que recorre cuenta por cuenta y suma todos los saldos y el resultado lo divide entre el N° de cuentas.

        
        print:
        
            El promedio de los saldos y la fecha actual de cuando se hizo el análisis.
        """

        saldoTotal=0
        promedio=0
        if not lista: #Si no encuentra nada lista de cuentas entonces que me muestre el print de linea 11
            print("No hay cuentas para calcularle e saldo promedio")
        
        else:
            
            for cuenta in lista: #Con el for recorre en la lista de cuentas. CUENTA POR CUENTA.
                saldoTotal+= cuenta.getSaldo()
            promedio=saldoTotal/len(lista)
            print("El promedio del saldo total de las cuentas es {}\nReporte realizado en la fecha: {}".format(promedio,self.getFecha()))



        
    

