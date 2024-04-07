from Corresponsal import corresponsal
class SerializadorCorresponsal():
    def __init__(self):
        self.archivo=open("Corresponsal.txt", "a")

    def getArchivo(self):
        return self.archivo
    
    def escribirCorresponsal(self, texto):
        self.archivo=open("Corresponsal.txt", "a")
        self.archivo.write(texto)
        self.archivo.close()

    def leerCorresponsal(self):
        nombre=""
        apellido=""
        cedula=""
        telefono=""
        correo_electronico=""
        nombreCorresponsal=""
        direccionCorresponsal=""
        listaCorresponsal=[]
        i=0
        self.archivo=open("Corresponsal.txt", "r")
        for linea in self.archivo:
            if(i==0):
                nombre=linea.strip()
                i+=1
            elif(i==1):
                apellido=linea.strip()
                i+=1
            elif(i==2):
                cedula=linea.strip()
                i+=1
            elif(i==3):
                telefono=linea.strip()
                i+=1
            elif(i==4):
                correo_electronico=linea.strip()
                i+=1
            elif(i==5):
                nombreCorresponsal=linea.strip()
                i+=1
            else:
                direccionCorresponsal=linea.strip()
                i=0
                miCorresponsal=corresponsal(nombre, apellido, cedula, telefono, correo_electronico, nombreCorresponsal, direccionCorresponsal)
                listaCorresponsal.append(miCorresponsal)
        self.archivo.close()
        return listaCorresponsal
    
    def modificarCorresponsal(self, texto):
        self.archivo = open("Corresponsal.txt", "w")
        self.archivo.write(texto)
        self.archivo.close()