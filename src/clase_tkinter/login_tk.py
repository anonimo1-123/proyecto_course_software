import tkinter as tk
from tkinter import messagebox
import sys
import os
sys.path.append(os.path.abspath("..")+"/proyecto_de_software/src/gestion_de_login")
import  login



class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("300x200")
        self.configure(bg="#f0f8ff")

        # Etiquetas y campos
        tk.Label(self, text="Usuario", bg="#f0f8ff", fg="#333", font=("Arial", 12)).pack(pady=5)
        self.entry_usuario = tk.Entry(self, font=("Arial", 12))
        self.entry_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña", bg="#f0f8ff", fg="#333", font=("Arial", 12)).pack(pady=5)
        self.entry_contraseña = tk.Entry(self, show="*", font=("Arial", 12))
        self.entry_contraseña.pack(pady=5)

        # Botón de inicio
        btn_iniciar = tk.Button(self, text="Iniciar Sesión", bg="#4caf50", fg="white",
                                font=("Arial", 12), command=self.iniciar_sesion)
        btn_iniciar.pack(pady=15)

        self.tipo_user= ""

    def iniciar_sesion(self):
        usuario = self.entry_usuario.get()
        contraseña = self.entry_contraseña.get()
        obj_login = login.login_(usuario,contraseña)
        respuesta,tipo=obj_login.comprobacion()
        if respuesta == True:
            messagebox.showinfo("Acceso permitido", "¡Bienvenido, " + usuario + "!")
            self.destroy()
            tipo_user = obj_login.comprobacion_type_user(tipo)
            self.tipo_user = tipo_user
            
        else :
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos.")
            self.destroy()
            

       



    
