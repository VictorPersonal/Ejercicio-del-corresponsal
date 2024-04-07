__autor__= "Víctor, David, John"
__copyright__= "Copyright 2023, Víctor, David, John"
__credits__= ["Víctor, David, John"]
__license__="GPL 1.0"
__version__="0.8.2.8"
__maintainer__="Víctor, David, John"
__email__= "tabares.victor@correounivalle.edu.co, david.valencia.restrepo@correounivalle.ed.co, john.esteban.giraldo@correounivalle.edu.co "
__status__= "Pruebas"

class Usuario():
    
    """
    
    Esta clase representa el Usuario, la cual es la que tiene como herederas, 'Corresponsal' y 'Clientes'.

    Donde de los 2 usuarios 'Corresponsal' es el que hace todo.
    
    Atributes: Privados.

        nombre (str): [nombre]
        apellido (str): [apellido]
        cedula (str): [cedula]
        telefono (str): [telefono]
        correo_electronico (str): [correo_electronico]

    """

    
    def __init__(self, nombre, apellido, cedula, telefono, correo_electronico):

        """
        
        Este método permite crear instancias u objetos de la clase Usuario, que representa.
        
        Args: Los atributos de esta clase son PRIVADOS.

            param1: nombre (str): [nombre]
            param2: apellido (str): [apellido]
            param3: cedula (str): [cedula]
            param4: telefono (str): [telefono]
            param5: correo_electronico (str): [correo_electronico]

        """

        self.__nombre = nombre
        self.__apellido = apellido
        self.__cedula = cedula
        self.__telefono = telefono 
        self.__correo_electronico = correo_electronico

    def getNombre(self):

        """
        
        Este método permite consultar el nombre de las usuarios.
        
        Args:

        Returns: 

            nombre (str): [nombre]
        
        """
        
        return self.__nombre
    def getApellido(self):

        """
        
        Este método permite consultar el apellido de las personas.
        
        Args:

        Returns: 

            apellido (str): [apellido]
        
        """

        return self.__apellido
    def getCedula(self):

        """
        
        Este método permite consultar la cédula de las personas.
        
        Args:

        Returns: 

            cedula (str): [cedula]
        
        """


        return self.__cedula
    def getTelefono(self):

        """
        
        Este método permite consultar el teléfono de las personas.
        
        Args:

        Returns: 

            telefono (str): [telefono]
        
        """

        return self.__telefono
    def getCorreoElectronico(self):

        """
        
        Este método permite consultar el correo electrónico de las personas.
        
        Args:

        Returns: 

            correoElectronico (str): [correoElectronico]
        
        """

        return self.__correo_electronico
    def setNombre(self, nombre):

        """
        
        Este método permite modificar el nombre de los usuarios.
        
        Args:

            param1: nombre (str): [nombre]

        Returns: 
            
        """

        self.__nombre=nombre
    def setApellido(self, apellido):

        """
        
        Este método permite modificar el apellido de los usuarios.
        
        Args:

            param1: apellido (str): [apellido]

        Returns: 
            
        """

        self.__apellido=apellido
    def setCedula(self, cedula):

        """
        
        Este método permite modificar la CC de los usuarios.
        
        Args:

            param1: cedula (str): [cedula]

        Returns: 
            
        """

        self.__cedula=cedula
    def setTelefono(self, telefono):

        """
        
        Este método permite modificar el teléfono de los usuarios.
        
        Args:

            param1: telefono (str): [telefono]

        Returns: 
            
        """

        self.__telefono=telefono
    def setCorreoElectronico(self, correo_electronico):
        
        """
        
        Este método permite modificar el correo electrónico de los usuarios.
        
        Args:

            param1: correoelectronico (str): [correoelectronico]

        Returns: 
            
        """
        
        self.__correo_electronico=correo_electronico

    def __str__(self):

        """
        
        Este método permite visualizar en la consola los datos de usuario. con un retorno de los mismos.

        Args:

            param1: nombre (str): [nombre]
            param2: apellido (str): [apellido]
            param3: cedula (str): [cedula]
            param4: telefono (str): [telefono]
            param5: correo_electronico (str): [correo_electronico]
        
        Returns:

            nombre (str): [nombre]
            apellido (str): [apellido]
            cedula (str): [cedula]
            telefono (str): [telefono]
            correo_electronico (str): [correo_electronico]

        """

        return f'Nombre/apellido: {self.__nombre} " " {self.__apellido}\nCédula: {self.__cedula}\nTeléfono: {self.__telefono}\nCorreo: {self.__correo_electronico}'
        
        