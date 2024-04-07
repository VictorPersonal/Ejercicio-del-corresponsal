from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Transaccion import Transaccion

class RealizarRetiro():
    
    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def realizarRetiro(self):
        pass

    def __init__(self, menusec, corresponsal):
        self.ventana= tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Realizar Deposito")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal 
        self.contador=0

        self.listaCuentas=self.corresponsal.serializador.leerArchivo()

        self.titulo=Label(self.ventana, text="Realizar Retiro")
        self.lblNumCuenta= Label(self.ventana, text="N° Cuenta*:")
        self.txtNumCuenta= Entry(self.ventana, width=25)
        self.lblCantTransaccion=Label(self.ventana, text="Transacción N°*:")
        self.txtCantTransaccion=Entry(self.ventana, width=25)
        self.lblMonto= Label(self.ventana, text="Monto*:")
        self.txtMonto=Entry(self.ventana, width=25)
        self.lblCedula=Label(self.ventana, text="Cédula*:")
        self.txtCedula=Entry(self.ventana, width=25)
        self.btnDepositar=Button(self.ventana, text="Retirar", command=lambda:self.realizarRetiro())
        self.btnSalir=Button(self.ventana, text="Salir", command=lambda:self.salirSistema())
     
        self.titulo.grid(row=0, column=1, pady=10)
        self.lblNumCuenta.grid(row=1,column=0, pady=10)
        self.txtNumCuenta.grid(row=1,column=1, pady=10)
        self.lblCantTransaccion.grid(row=2, column=0, pady=10)
        self.txtCantTransaccion.grid(row=2, column=1, pady=10)
        self.lblMonto.grid(row=3,column=0, pady=10)
        self.txtMonto.grid(row=3,column=1, pady=10)
        self.lblCedula.grid(row=4,column=0, pady=10)
        self.txtCedula.grid(row=4,column=1, pady=10)
        self.btnDepositar.grid(row=5,column=1, padx=10, pady=10)
        self.btnSalir.grid(row=5,column=2, padx=10, pady=10)