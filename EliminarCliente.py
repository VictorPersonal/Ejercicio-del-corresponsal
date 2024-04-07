import tkinter as tk
from tkinter import messagebox
from tkinter import *

class EliminarCliente:

    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def limpiarcelda(self):
        self.txtCedulaCliente.delete(0, tk.END)

    def eliminar_cliente(self):
        cedula=self.txtCedulaCliente.get()
        listaClientes=self.corresponsal.serializadorCliente.leerCliente()
        CedulaEncontrada=None
        for cliente in listaClientes:
            if cliente.getCedula() == self.txtCedulaCliente.get():
                CedulaEncontrada=cedula
                listaClientes.remove(cliente)
                self.corresponsal.eliminarCliente(listaClientes)
                print("Cliente eliminado con éxito!!")
                break
        if not CedulaEncontrada:
            messagebox.showinfo("No existe el usuario con ese N° de cédula")

    def __init__(self, menusec, corresponsal):
        self.ventana=tk.Toplevel(menusec)
        self.ventana.title("Eliminar Cliente")
        self.ventana.resizable(0,0)
        self.ventana.focus_set()
        self.corresponsal=corresponsal
        self.listaClientes=self.corresponsal.serializadorCliente.leerCliente() #
        self.titulo= tk.Label(self.ventana, text="Eliminar Cliente")
        self.lblCedulaCliente= tk.Label(self.ventana, text="Cédula*:")
        self.txtCedulaCliente= tk.Entry(self.ventana, width=25)
        self.lblNombreCliente= tk.Label(self.ventana, text="Nombre*:")
        self.txtNombreCliente= tk.Entry(self.ventana, width=25, state="disabled")
        self.lblApellidoCliente= tk.Label(self.ventana, text="Apellido*:")
        self.txtApellidoCliente= tk.Entry(self.ventana, width=25, state="disabled")
        self.lblTelefonoCliente= tk.Label(self.ventana, text="Telefono*:")
        self.txtTelefonoCliente= tk.Entry(self.ventana, width=25, state="disabled")
        self.lblCorreoCliente= tk.Label(self.ventana, text="E-mail*:")
        self.txtCorreoCliente= tk.Entry(self.ventana, width=25, state="disabled")
        self.btnBorrarCliente= Button(self.ventana, text="Borrar", command=lambda:self.eliminar_cliente())
        self.btnLimpiarCliente= Button(self.ventana, text="Limpiar", command=lambda:self.limpiarcelda())
        self.btnSalirCliente= Button(self.ventana, text="Salir", command=lambda:self.salirSistema())

        self.titulo.grid(row=0,column=0)
        self.lblCedulaCliente.grid(row=1,column=0)
        self.txtCedulaCliente.grid(row=1, column=1)
        self.lblNombreCliente.grid(row=2,column=0)
        self.txtNombreCliente.grid(row=2, column=1)
        self.lblApellidoCliente.grid(row=3,column=0)
        self.txtApellidoCliente.grid(row=3,column=1)
        self.lblTelefonoCliente.grid(row=4,column=0)
        self.txtTelefonoCliente.grid(row=4,column=1)
        self.lblCorreoCliente.grid(row=4,column=0)
        self.txtCorreoCliente.grid(row=4,column=1)
        self.btnBorrarCliente.grid(row=5,column=0)
        self.btnLimpiarCliente.grid(row=5,column=1)
        self.btnSalirCliente.grid(row=5,column=2)


        self.ventana.mainloop()