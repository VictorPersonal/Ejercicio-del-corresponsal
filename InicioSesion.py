from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MenuSec import Menu2
from SerializadorCorresponsal import SerializadorCorresponsal

class LogginCorresponsal():


    def SalirDelSistema(self):


        respuesta=messagebox.askquestion("Confirmación de salida", "¿Seguro de salir?") 
        if respuesta == "yes":
            self.ventana.destroy()#La ventana se cierra con.destroy



    def ValidarIngresoCorresponsal(self):
        usuario=self.txtUsuario.get()
        password=self.txtPassword.get()
        if len(usuario) >=5 and len(password) >=5:
            serializadorCorresponsal= SerializadorCorresponsal()
            listaCorresponsal=serializadorCorresponsal.leerCorresponsal()
            corresponsalEncontrado=None
            for corresponsal in listaCorresponsal:
                if(usuario==corresponsal.getNombre() and password==corresponsal.getCedula()):
                    corresponsalEncontrado=corresponsal
                    menusec=Menu2(self.ventana, corresponsal)
                    break
                if not corresponsalEncontrado:
                    messagebox.showwarning("ADVERTENCIA", "Usuario y/o Password incorrectos, intente nuevamente...")
        else:
            messagebox.showwarning("Advertencia", "Los campos Usuario y Password deben tener mínimo 5 caracteres!")
            #Verificar si el corresponsal esta en la lista


    def __init__(self):


        self.ventana=Tk()
        self.ventana.title("Inicia Sesión")
        self.ventana.resizable(0,0)
        self.lblTituloISesion = tk.Label(self.ventana, text="Inicia Sesión")
        self.lblTituloUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblTituloPassword = tk.Label(self.ventana, text="Password*:")
        self.txtUsuario = tk.Entry(self.ventana, width="25")
        self.txtPassword = tk.Entry(self.ventana, width="25", show="*")
        self.btnIngresarSistem = tk.Button(self.ventana, text="Ingresar", command=lambda:self.ValidarIngresoCorresponsal())
        self.btnSalir = tk.Button(self.ventana, text = "Salir",command=lambda:self.SalirDelSistema())
        self.btnAyuda = tk.Button(self.ventana, text = "Ayuda", command=lambda:self.SolicitarAyuda())


#Ubicación de botones, etiquetas, cajas/texto:
        
        """
        
        La posición de etiquetas se hace con .grid() con columnas y filas.
        
        """
        self.lblTituloISesion.grid(row=0,column=1)
        self.lblTituloUsuario.grid(row=2,column=0)
        self.lblTituloPassword.grid(row=3,column=0)
        self.txtUsuario.grid(row=2,column=1)
        self.txtPassword.grid(row=3,column=1)
        self.btnIngresarSistem.grid(row=4,column=1, padx=10, pady=10)
        self.btnSalir.grid(row=4,column=2, padx=10, pady=10)
        self.btnAyuda.grid(row=0, column=3, padx=10, pady=10)




        self.ventana.mainloop()
        