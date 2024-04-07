from tkinter import *
import tkinter as tk
from tkinter import messagebox

class GenerarReporte():
    def Salir(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def generarReporte(self):
        for cuenta in self.listaCuentas:
            numeroCuenta=cuenta.getnumeroCuenta()
            if numeroCuenta:
                cuentaOculta= '*' * (len(numeroCuenta)-4)+numeroCuenta[-4:]
            cedula=cuenta.getCedula()
            if cedula:
                cedulaOculta= '*' * (len(cedula)-4)+cedula[-4:]
            saldo=cuenta.getSaldo()
            self.lblNumC.config({cuentaOculta})
            self.lblCc.config({cedulaOculta})
            self.sl({saldo})

    def __init__(self, menusec, corresponsal):
        self.ventana=tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Gestionar Reporte")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal
        self.listaCuentas=self.corresponsal.serializador.leerArchivo()
        self.titulo=Label(text="Gestionar Reporte")
        self.titulo.grid(row=0,column=0)
        self.contenedor=Frame(self.ventana, bg="white")
        self.contenedor.grid(row=1, column=1)
        self.cedulaCuenta=Label(self.contenedor, text="Titular")
        self.cedulaCuenta.grid(row=0,column=0)
        self.lblCc=Label(self.contenedor)
        self.lblCc.grid(row=1, column=0)
        self.lblNumeroDeCuenta=Label(self.contenedor, text="Cuenta")
        self.lblNumeroDeCuenta.grid(row=0, column=1)
        self.lblNumC=Label(self.contenedor)
        self.lblNumC.grid(row=1,column=1)
        self.saldo=Label(self.contenedor, text="Saldo")
        self.saldo.grid(row=0,column=2)
        self.sl=Label(self.contenedor)
        self.sl.grid(row=1,column=2)
        self.btnGR=Button(self.ventana, text="Generar Reporte")
        self.btnGR.grid(row=3,column=2)
        self.btnSalir=Button(self.ventana, text="Salir",command=lambda:self.Salir())
        self.btnSalir.grid(row=3,column=1)
        self.ventana.mainloop()