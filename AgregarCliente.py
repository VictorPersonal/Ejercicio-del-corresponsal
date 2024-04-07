from tkinter import *
from tkinter import messagebox
import tkinter as tk


class AgregarCliente():
    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass
    
    def guardarCliente(self):
        nombre=self.txtNombreCliente.get()
        apellido=self.txtApellidoCliente.get()
        cedula=self.txtCedulaCliente.get()
        telefono=self.txtTelefonoCliente.get()
        correo_electronico=self.txtCorreoCliente.get()


        if not nombre or not apellido or not cedula or not telefono or not correo_electronico:
            messagebox.showerror("Error", "Por favor complete todos los campos")
            return
        else:
            listaClientes=self.corresponsal.serializadorCliente.leerCliente()
            self.corresponsal.crearCliente(listaClientes, nombre, apellido, cedula, telefono, correo_electronico)
            messagebox.showinfo("Confirmación", "Cliente agregado con éxito")

    def __init__(self, menusec, corresponsal):
        self.ventana=tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Agregar cliente")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal
        self.listaClientes=self.corresponsal.serializadorCliente.leerCliente() #
        self.titulo= tk.Label(self.ventana, text="Agregar Cliente")
        self.lblNombreCliente= tk.Label(self.ventana, text="Nombre*:")
        self.txtNombreCliente= tk.Entry(self.ventana, width=25)
        self.lblApellidoCliente= tk.Label(self.ventana, text="Apellido*:")
        self.txtApellidoCliente= tk.Entry(self.ventana, width=25)
        self.lblCedulaCliente= tk.Label(self.ventana, text="Cédula*:")
        self.txtCedulaCliente= tk.Entry(self.ventana, width=25)
        self.lblTelefonoCliente= tk.Label(self.ventana, text="Telefono*:")
        self.txtTelefonoCliente= tk.Entry(self.ventana, width=25)
        self.lblCorreoCliente= tk.Label(self.ventana, text="E-mail*:")
        self.txtCorreoCliente= tk.Entry(self.ventana, width=25)
        self.btnGuardarCliente=tk.Button(self.ventana, text="Guardar", command=lambda:self.guardarCliente())
        self.btnSalir=tk.Button(self.ventana, text="Salir", command=lambda:self.salirSistema())
        
        self.titulo.grid(row=0,column=1)
        self.lblNombreCliente.grid(row=1, column=0)
        self.txtNombreCliente.grid(row=1,column=1)
        self.lblApellidoCliente.grid(row=2, column=0)
        self.txtApellidoCliente.grid(row=2,column=1)
        self.lblCedulaCliente.grid(row=3,column=0)
        self.txtCedulaCliente.grid(row=3,column=1)
        self.lblTelefonoCliente.grid(row=4,column=0)
        self.txtTelefonoCliente.grid(row=4,column=1)
        self.lblCorreoCliente.grid(row=5,column=0)
        self.txtCorreoCliente.grid(row=5,column=1)
        self.btnGuardarCliente.grid(row=6,column=0)
        self.btnSalir.grid(row=6,column=1)
        self.ventana.mainloop()