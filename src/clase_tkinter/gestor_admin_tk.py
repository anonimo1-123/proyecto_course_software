import tkinter as tk
from tkinter import Toplevel
import sys
import os


sys.path.append(os.path.abspath("..")+"/proyecto_de_software/src/modulos")
import  op


class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Calificaciones - Admin")
        self.geometry("400x400")
        self.configure(bg="#e3f2fd")  # Fondo azul claro

        # Título principal
        tk.Label(self, text="Panel Administrativo", font=("Helvetica", 18, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=20)

        # Botones
        botones_info = [
            ("Consultar Calificaciones", self.abrir_consulta),
            ("Aperturar Curso", self.abrir_apertura),
            ("Asignar Materia a Docente", self.abrir_asignacion),
            ("Gestionar Usuario", self.abrir_gestion_usuario),
            ("Salir", self.destroy)
        ]

        for texto, accion in botones_info:
            tk.Button(self, text=texto, command=accion, bg="#64b5f6", fg="white",
                      font=("Arial", 12), width=30, height=2, relief="raised").pack(pady=8)

    # Métodos para abrir nuevas ventanas
    def abrir_consulta(self):
        self.consultar_notas("Consulta de Calificaciones")

    def abrir_apertura(self):
        self.aperturar_curso("Aperturar Curso")
        
    def abrir_asignacion(self):
       self.asignar_profesor_curso("Asignar Curso a un profesor")

    def abrir_gestion_usuario(self):
        self.gestion_usuarios("Gestion de usuarios")



    def consultar_notas(self, titulo):
        win = Toplevel(self)
        win.title(titulo)
        win.geometry("400x400")
        win.configure(bg="#fce4ec")

        tk.Label(win, text=titulo, font=("Verdana", 14, "bold"), bg="#fce4ec", fg="#880e4f").pack(pady=10)

        frame_inputs = tk.Frame(win, bg="#fce4ec")
        frame_inputs.pack(pady=10)

        # Entradas
        tk.Label(frame_inputs, text="DNI Estudiante:", bg="#fce4ec").grid(row=0, column=0, padx=5, pady=5)
        dni_entry = tk.Entry(frame_inputs)
        dni_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame_inputs, text="ID Curso:", bg="#fce4ec").grid(row=1, column=0, padx=5, pady=5)
        curso_entry = tk.Entry(frame_inputs)
        curso_entry.grid(row=1, column=1, padx=5)

        tk.Label(frame_inputs, text="ID Periodo:", bg="#fce4ec").grid(row=2, column=0, padx=5, pady=5)
        periodo_entry = tk.Entry(frame_inputs)
        periodo_entry.grid(row=2, column=1, padx=5)

        tk.Button(win, text="Buscar", command=lambda: op.gestion_busqueda(dni_entry.get(), curso_entry.get(), periodo_entry.get()), bg="#64b5f6", fg="white").pack(pady=5)
        tk.Button(win, text="Exportar Boleta", command=lambda: op.exportar_boleta_notas(dni_entry.get(), periodo_entry.get()), bg="#4caf50", fg="white").pack(pady=5)



    def aperturar_curso(self,titulo):
        win = Toplevel(self)
        win.title(titulo)
        win.geometry("400x400")
        win.configure(bg="#e3f2fd")

        tk.Label(win, text="Aperturar Curso", font=("Helvetica", 16, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=15)

        frame = tk.Frame(win, bg="#e3f2fd")
        frame.pack(pady=10)
        # Entradas
        tk.Label(frame, text="Nombre del Curso:", bg="#e3f2fd").grid(row=0, column=0, sticky="e", pady=5)
        nombre_entry = tk.Entry(frame)
        nombre_entry.grid(row=0, column=1, pady=5)

        tk.Label(frame, text="Sección:", bg="#e3f2fd").grid(row=1, column=0, sticky="e", pady=5)
        seccion_entry = tk.Entry(frame)
        seccion_entry.grid(row=1, column=1, pady=5)

        tk.Label(frame, text="DNI Profesor:", bg="#e3f2fd").grid(row=2, column=0, sticky="e", pady=5)
        dni_prof_entry = tk.Entry(frame)
        dni_prof_entry.grid(row=2, column=1, pady=5)

        tk.Label(frame, text="ID Periodo:", bg="#e3f2fd").grid(row=3, column=0, sticky="e", pady=5)
        periodo_entry = tk.Entry(frame)
        periodo_entry.grid(row=3, column=1, pady=5)

        # Botón
        tk.Button(win, text="Aperturar", command=lambda: op.aperturar_curso(nombre_entry.get(),seccion_entry.get(),dni_prof_entry.get(),periodo_entry.get()), 
                bg="#4caf50", fg="white", font=("Arial", 11)).pack(pady=20)

   
   
    def asignar_profesor_curso(self,titulo):

        win = Toplevel(self)
        win.title(titulo)
        win.geometry("400x300")
        win.configure(bg="#fce4ec")

        tk.Label(win, text="Asignar Curso a Profesor", font=("Verdana", 14, "bold"), bg="#fce4ec", fg="#880e4f").pack(pady=15)

        frame = tk.Frame(win, bg="#fce4ec")
        frame.pack(pady=10)

        tk.Label(frame, text="DNI del Profesor:", bg="#fce4ec").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        dni_entry = tk.Entry(frame)
        dni_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(frame, text="ID del Curso:", bg="#fce4ec").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        curso_entry = tk.Entry(frame)
        curso_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(win, text="Asignar", command=lambda: op.asginar_materia(dni_entry.get(),curso_entry.get()), 
                bg="#010201", fg="white", font=("Arial", 11)).pack(pady=20)


    def gestion_usuarios(self,titulo):
        win = Toplevel(self)
        win.title(titulo)
        win.geometry("600x500")
        win.configure(bg="#e3f2fd")

        tk.Label(win, text="Gestión de Usuarios", font=("Helvetica", 16, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

        frame = tk.Frame(win, bg="#e3f2fd")
        frame.pack(pady=5)

        # Entradas
        tk.Label(frame, text="ID Usuario:", bg="#e3f2fd").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        id_entry = tk.Entry(frame)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Nombre Usuario:", bg="#e3f2fd").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        nombre_entry = tk.Entry(frame)
        nombre_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Password:", bg="#e3f2fd").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        pass_entry = tk.Entry(frame, show="*")
        pass_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID Rol:", bg="#e3f2fd").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        rol_entry = tk.Entry(frame)
        rol_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botones
        botones_frame = tk.Frame(win, bg="#e3f2fd")
        botones_frame.pack(pady=10)

        tk.Button(botones_frame, text="Crear Usuario", command=lambda: op.opciones_crud_user(1,id_entry.get(),nombre_entry.get(),pass_entry.get(),rol_entry.get()), 
                bg="#4caf50", fg="white", font=("Arial", 10), width=15).grid(row=0, column=2, padx=10)

        tk.Button(botones_frame, text="Editar Password", command=lambda:  op.opciones_crud_user(3,id_entry.get(),nombre_entry.get(),pass_entry.get(),rol_entry.get()), 
                bg="#ff9800", fg="white", font=("Arial", 10), width=15).grid(row=1, column=0, padx=10, pady=10)

        tk.Button(botones_frame, text="Visualizar Usuarios", command=lambda:  op.opciones_crud_user(2,id_entry.get(),nombre_entry.get(),pass_entry.get(),rol_entry.get()), 
                bg="#2196f3", fg="white", font=("Arial", 10), width=15).grid(row=1, column=3, padx=10, pady=10)


