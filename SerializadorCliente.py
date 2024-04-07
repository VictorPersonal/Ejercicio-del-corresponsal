from Cliente import Cliente
class SerializadorCliente():
    """
    
    Esta es la clase Serializador de Cliente, la cual agrega, modifica
    y lee los atributos de la clase 'Cliente'.
    
    """


    def __init__(self):
        
        """
        
        Constructor de la clase. Abre el archivo 'Cliente.txt' en modo 'a' (append)
        y guarda la referencia al archivo en la instancia.
        
        """
        
        self.archivo=open("Cliente.txt", "a")

    def getArchivo(self):
        """
        
        Retorna lo que se agregará en el arcivo.
        
        Return:

            Archivo(str): Referencia al archivo 'Cliente.txt'.
        
        """
        return self.archivo
    
    def escribirCliente(self,texto):
        """
        
        Agrega el texto proporsionado al final del archivo 'Cliente.txt'.

        Args: 
            
            texto(str): Texto a agregar al archivo.
        
        """
        self.archivo=open("Cliente.txt","a")
        self.archivo.write(texto)
        self.archivo.close()

    def leerCliente(self):
        """

        Lee el contenido del archivo 'Cliente.txt' y devuelve los mismos elementos que encontro al leer.

        Args:

            Ninguno.

        Returns:

            listaclientes(str): La lista que la función 'leerArchivo' encontro. 
        
        """
        nombre=""
        apellido=""
        cedula=""
        telefono=""
        correo_electronico=""

        i=0
        listaclientes=[]
        self.archivo=open("Cliente.txt","r")
        for linea in self.archivo:
            if(i==0):
                nombre = linea.strip()
                i += 1
            elif(i==1):
                apellido = linea.strip()
                i += 1
            elif(i==2):
                cedula = linea.strip()
                i += 1
            elif (i==3):
                telefono = linea.strip()
                i += 1
            else:
                correo_electronico = linea.strip()
                i=0
                clienteNuevo=Cliente(nombre, apellido, cedula, telefono, correo_electronico)
                listaclientes.append(clienteNuevo)
        self.archivo.close()
        return listaclientes
    
    def eliminarCliente(self, texto):
        """
        
        Modifica el texto proporcionado anteriormente en 'Cliente.txt'.

        Args:
            
            texto(str): Texto a modificar del archivo.
        
        """
        self.archivo=open("Cliente.txt", "w")
        self.archivo.write(texto)
        self.archivo.close()
            
