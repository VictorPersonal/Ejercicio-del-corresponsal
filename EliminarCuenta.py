from tkinter import *
import tkinter as tk
from tkinter import messagebox
class EliminarCuenta():

    def limpiarCasilla(self):
        self.txtNumeroCuenta.delete(0, tk.END)

    def eliminar(self):
        numeroCuenta=self.txtNumeroCuenta.get()
        encontrado=False
        for cuenta in self.listaCuentas:
            if cuenta.getnumeroCuenta() == self.txtNumeroCuenta.get():
                self.listaCuentas.remove(cuenta)
                self.corresponsal.eliminarCuenta(self.listaCuentas)
                encontrado=True
                messagebox.showinfo("Información", "Cuenta encontrada con éxito")

        if(encontrado==False):
            messagebox.showerror("Información", "El numero de cuenta no corresponde a ningún cliente")

    

    def __init__(self, menusec, corresponsal):
        self.ventana=tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Eliminar Cuenta")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal
        self.listaCuentas=self.corresponsal.serializador.leerArchivo()
        self.titulo=Label(self.ventana, text="Eliminar Cuenta")
        self.lblNumeroCuenta= Label(self.ventana, text="N° Cuenta*:")
        self.txtNumeroCuenta= Entry(self.ventana, width=25)
        self.lblSaldo= Label(self.ventana, text="Saldo*:")
        self.txtSaldo= Entry(self.ventana, width=25, state="disabled")
        self.lblCedula= Label(self.ventana, text="Cédula*:")
        self.txtCedula= Entry(self.ventana, width=25, state="disabled")
        self.btnBorrar= Button(self.ventana, text="Eliminar", command=lambda:self.eliminar())
        self.btnLimpiar= Button(self.ventana, text="Limpiar", command=lambda:self.limpiarCasilla())

        self.titulo.grid(row=0,column=0)
        self.lblNumeroCuenta.grid(row=1,column=0)
        self.txtNumeroCuenta.grid(row=1, column=1)
        self.lblSaldo.grid(row=2,column=0)
        self.txtSaldo.grid(row=2, column=1)
        self.lblCedula.grid(row=3,column=0)
        self.txtCedula.grid(row=3,column=1) 
        self.lblCedula.grid(row=4,column=0)
        self.txtCedula.grid(row=4,column=1) 
        self.btnBorrar.grid(row=5, column=1) 
        self.ventana.mainloop()  