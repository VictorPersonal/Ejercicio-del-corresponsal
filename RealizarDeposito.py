from tkinter import*
from tkinter import messagebox
import tkinter as tk

class RealizarDeposito():
     
    def salirSistema(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def buscarCuenta(self):
        numeroCuenta=self.txtNumCuenta.get()
        numeroCuentaEncontrado=None
        for cuenta in self.listaCuentas:
            if numeroCuenta == cuenta.getnumeroCuenta():
                numeroCuentaEncontrado = numeroCuenta
                self.listaCuentas=self.corresponsal.serializador.leerArchivoCuenta()
                messagebox.showinfo("Correcto","Número de cuenta encontrado!!")
                self.txtMonto.config(state="normal")
                self.txtCedula.config(state="normal")
                self.btnDepositar.config(state="normal")
                self.txtMonto.insert("end", str(cuenta.getSaldo()))
                self.txtCedula.insert("end", str(cuenta.getCedula()))
                self.txtMonto.config(state="normal")
                self.txtCedula.config(state="disabled")
                break
            else:
                messagebox.showerror("Incorrecto","Número de cuenta no encontrado!!")

    def realizarDeposito(self):
        numeroCuenta=self.txtNumCuenta.get()
        encontrado=False
        for cuenta in self.listaCuentas:
            if numeroCuenta == cuenta.getnumeroCuenta():
                encontrado=True
                monto=float(self.txtMonto.get())
                saldo=monto+cuenta.getSaldo()
                cuenta.setSaldo(saldo)

                self.corresponsal.realizarDeposito(self.listaCuentas)
                messagebox.showinfo("Informacion","Depositaste correctamente")
                break
        if encontrado==False:
            messagebox.showerror("Advertencia", "Cuenta no encontrada")

    def __init__(self, menusec, corresponsal):
        self.ventana= tk.Toplevel(menusec)
        self.ventana.focus_set()
        self.ventana.title("Realizar Deposito")
        self.ventana.resizable(0,0)
        self.corresponsal=corresponsal 

        self.listaCuentas=self.corresponsal.serializador.leerArchivoCuenta()
        


        self.titulo=Label(self.ventana, text="Realizar Deposito")
        self.lblNumCuenta= Label(self.ventana, text="N° Cuenta*:")
        self.txtNumCuenta= Entry(self.ventana, width=25)
        self.lblCantTransaccion=Label(self.ventana, text="Transacción N°*:")
        self.txtCantTransaccion=Entry(self.ventana, width=25, state="disabled")
        self.lblMonto= Label(self.ventana, text="Monto*:")
        self.txtMonto=Entry(self.ventana, width=25, state="disabled")
        self.lblCedula=Label(self.ventana, text="Cédula*:")
        self.txtCedula=Entry(self.ventana, width=25, state="disabled")
        self.btnDepositar=Button(self.ventana, text="Depositar", state="disabled",command=lambda:self.realizarDeposito())
        self.btnSalir=Button(self.ventana, text="Salir", command=lambda:self.salirSistema())
        self.btnBuscar=Button(self.ventana, text="Buscar", command=lambda:self.buscarCuenta())
     
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
        self.btnBuscar.grid(row=1,column=2, pady=10)

        self.ventana.mainloop()