from Usuario import Usuario
__autor__= "Víctor, David, John"
__copyright__= "Copyright 2023, Víctor, David, John"
__credits__= ["Víctor, David, John"]
__license__="GPL 1.0"
__version__="0.8.2.8"
__maintainer__="Víctor, David, John"
__email__= "tabares.victor@correounivalle.edu.co, david.valencia.restrepo@correounivalle.ed.co, john.esteban.giraldo@correounivalle.edu.co "
__status__= "Pruebas"

class Cliente(Usuario):

    """
    
    Esta es la clase cliente, hereda de la clase Usuario todos sus atributos.

    Esta clase servirá para la creación de las cuentas.

    Atributes: Privados.
    
        nombre (str): [nombre]
        apellido (str): [apellido]
        cedula (str): [cedula]
        telefono (str): [telefono]
        correo_electronico (str): [correo_electronico]
        
        """


    def __init__(self, nombre, apellido, cedula, telefono, correo_electronico): #Definimos los atributos necesarios de la clase heredera
        Usuario.__init__(self, nombre, apellido, cedula, telefono, correo_electronico)

        """
        
        Este método permite crear instancias u objetos de la clase Cliente, que representa.
        
        Args: Hereda de la clase Usuario.
        
        param1: nombre (str): [nombre]
        param2: apellido (str): [apellido]
        param3: cedula (str): [cedula]
        param4: telefono (str): [telefono]
        param5: correo_electronico (str): [correo_electronico]

        """
      