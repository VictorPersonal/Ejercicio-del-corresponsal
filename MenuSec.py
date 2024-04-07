from tkinter import *
from tkinter import messagebox
import tkinter as tk
from AgregarCliente import AgregarCliente
from EliminarCliente import EliminarCliente
from CrearCuenta import CrearCuenta
from EliminarCuenta import EliminarCuenta
from RealizarDeposito import RealizarDeposito
from RealizarRetiro import RealizarRetiro
from GenerarReporte import GenerarReporte
class Menu2():
    def agregarCliente(self):
        agregarCl = AgregarCliente(self.ventana, self.corresponsal)
    
    def crearCuenta(self):
        crearCu = CrearCuenta(self.ventana, self.corresponsal)

    def eliminarCliente(self):
        eliminarCl= EliminarCliente(self.ventana, self.corresponsal)

    def eliminarCuenta(self):
        eliminarCu= EliminarCuenta(self.ventana, self.corresponsal)

    def retirar(self):
        retirarCu= RealizarRetiro(self.ventana, self.corresponsal)
    
    def depositar(self):
        depositarCu= RealizarDeposito(self.ventana, self.corresponsal)
    
    def generarReporte(self):
        reportarDatos= GenerarReporte(self.ventana, self.corresponsal)

    def __init__(self, iniciosesion, corresponsal):
        self.ventana=tk.Toplevel(iniciosesion)
        self.ventana.geometry("500x450")
        self.ventana.title("Menú principal")
        self.ventana.resizable(0,0)
        self.ventana.focus_set()
        self.corresponsal= corresponsal
        self.menu2=tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu2)
        menuCorresponsal=tk.Menu(self.menu2)
        self.menu2.add_cascade(label="Gestionar clientes", menu=menuCorresponsal)
        menuCorresponsal.add_command(label="Agregar Cliente", command=lambda:self.agregarCliente())
        menuCorresponsal.add_command(label="Eliminar Cliente", command=lambda:self.eliminarCliente())
        self.ventana.config(menu=self.menu2)

#Menu de cuentas:
        menuCuenta=tk.Menu(self.menu2)
        self.menu2.add_cascade(label="Gestionar Cuenta", menu=menuCuenta)
        menuCuenta.add_command(label="Agregar  Cuenta", command=lambda:self.crearCuenta())
        menuCuenta.add_command(label="Eliminar Cuenta", command=lambda:self.eliminarCuenta())

#Menu transacciones:
        menuCuenta=tk.Menu(self.menu2)
        self.menu2.add_cascade(label="Elegir transacción", menu=menuCuenta)
        menuCuenta.add_command(label="Hacer Depósito", command=lambda:self.depositar())
        menuCuenta.add_command(label="Hacer Retiro", command=lambda:self.retirar())


#Menu Reportes:
        menuCuenta=tk.Menu(self.menu2)
        self.menu2.add_cascade(label="Consultr informes", menu=menuCuenta)
        menuCuenta.add_command(label="Generar reporte", command=lambda:self.generarReporte())
        self.ventana.mainloop()

        
