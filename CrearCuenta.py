from tkinter import *
import tkinter as tk
from tkinter import messagebox
class CrearCuenta():

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass


    def buscarCliente(self):
        
        cedula=self.txtCedula.get()
        listaClientes=self.corresponsal.serializadorCliente.leerCliente()
        
        CedulaEncontrada=None
        for cliente in listaClientes:
            if cliente.getCedula() == self.txtCedula.get():
                CedulaEncontrada=cedula
                listaClientes=self.corresponsal.serializadorCliente.leerCliente()
                messagebox.showinfo("Información", "Cliente encontrado con éxito")
                break
            
        else:
            messagebox.showerror("Información", "La cédula no corresponde a ningún cliente")

    def crearCuenta(self):
        #Se establece un Estado 'NORMAL' en la caja de texto, para que permita insertar el 0 y como aparece en el pdf del trabajo se deshabilita el campo/texto.
        self.txtNumCuenta.config(state="normal")
        self.txtSaldo.config(state="normal")
        self.txtSaldo.delete(0, tk.END)  
        self.txtSaldo.insert(0, "0")    
        self.txtSaldo.config(state="disabled")

        numeroCuenta=self.txtNumCuenta.get()
        saldo=self.txtSaldo.get()
        cedula=self.txtCedula.get()


        listaCuentas=self.corresponsal.serializador.leerArchivo()
        self.corresponsal.crearCuenta(listaCuentas, numeroCuenta,saldo, cedula)
        messagebox.showinfo("Confirmación", "Cuenta agregada con éxito")

        #messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

    def __init__(self, menusec, corresponsal):
        self.ventana= tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Agregar Cuenta")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal

        self.listaClientes=self.corresponsal.serializadorCliente.leerCliente()
        self.listaCuentas=self.corresponsal.serializador.leerArchivo()
        
        self.titulo= tk.Label(self.ventana, text="Agregar Cuenta")
        self.lblCedula=Label(self.ventana, text="Cédula*:")
        self.txtCedula=Entry(self.ventana, width=25)
        self.lblNumCuenta= Label(self.ventana, text="N° Cuenta*:")
        self.txtNumCuenta= Entry(self.ventana, width=25)
        self.lblSaldo= Label(self.ventana, text="Saldo*:")
        self.txtSaldo=Entry(self.ventana, width=25,state="disabled")
        self.txtSaldo.insert(0, "0")
        self.btnGuardarCuenta=Button(self.ventana, text="Crear", command=lambda:self.crearCuenta())
        self.btnSalir=Button(self.ventana, text="Salir", command=lambda:self.salirSistema())
        self.btnBuscarCliente=Button(self.ventana, text="Buscar", command=lambda:self.buscarCliente())

        self.titulo.grid(row=0, column=1, pady=10)
        self.lblCedula.grid(row=1,column=0, pady=10)
        self.txtCedula.grid(row=1,column=1, pady=10)
        self.lblNumCuenta.grid(row=2,column=0, pady=10)
        self.txtNumCuenta.grid(row=2,column=1, pady=10)
        self.lblSaldo.grid(row=3,column=0, pady=10)
        self.txtSaldo.grid(row=3,column=1, pady=10)
        self.btnGuardarCuenta.grid(row=4,column=1, padx=10, pady=10)
        self.btnSalir.grid(row=4,column=2, padx=10, pady=10)
        self.btnBuscarCliente.grid(row=1,column=2, padx=10, pady=10)
        self.ventana.mainloop()