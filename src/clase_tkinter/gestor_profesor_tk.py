import tkinter as tk
from tkinter import Toplevel
import sys
import os


sys.path.append(os.path.abspath("..")+"/proyecto_de_software/src/modulos")
import  op


class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Calificaciones - PROFESOR")
        self.geometry("400x400")
        self.configure(bg="#e3f2fd")  # Fondo azul claro

        # Título principal
        tk.Label(self, text="Panel Administrativo", font=("Helvetica", 18, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=20)

        # Botones
        botones_info = [
            ("INGRESAR CALIFICACION ",self.abir_ingreso_notas),
            ("ACTUALIZAR CALIFICACION",self.abrir_actualizacion_de_calificaciones ),
            ("CONSULTAR CALIFICACION",self.abrir_consulta ),
            ("Salir", self.destroy) 
        ]

        for texto, accion in botones_info:
            tk.Button(self, text=texto, command=accion, bg="#64b5f6", fg="white",
                      font=("Arial", 12), width=30, height=2, relief="raised").pack(pady=8)

    # Métodos para abrir nuevas ventanas
    def abir_ingreso_notas(self):
        self.ingresar_notas("Consulta de Calificaciones")

    def abrir_consulta(self):
        self.consultar_notas("Consulta de Calificaciones")


    def abrir_actualizacion_de_calificaciones(self):
       self.actualizar_notas("Asignar Curso a un profesor")



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



    def ingresar_notas(self,titulo):
        
        win = Toplevel(self)
        win.title(titulo)
        win.geometry("400x400")
        win.configure(bg="#e8f5e9")

        tk.Label(win, text=titulo, font=("Verdana", 14, "bold"), bg="#e8f5e9", fg="#1b5e20").pack(pady=10)

        frame = tk.Frame(win, bg="#e8f5e9")
        frame.pack(pady=10)

        tk.Label(frame, text="DNI Estudiante:", bg="#e8f5e9").grid(row=0, column=0, padx=5, pady=5)
        dni_entry = tk.Entry(frame)
        dni_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="ID Curso:", bg="#e8f5e9").grid(row=1, column=0, padx=5, pady=5)
        curso_entry = tk.Entry(frame)
        curso_entry.grid(row=1, column=1, padx=5)


        tk.Label(frame, text="Nota:", bg="#e8f5e9").grid(row=3, column=0, padx=5, pady=5)
        nota_entry = tk.Entry(frame)
        nota_entry.grid(row=3, column=1, padx=5)

        tk.Button(win, text="Guardar Nota", command=lambda: op.registrar_notas(nota_entry.get(),dni_entry.get(),curso_entry.get()), 
                bg="#388e3c", fg="white").pack(pady=15)


   
    def actualizar_notas(self,titulo):
    
        win = Toplevel(self)
        win.title(titulo)
        win.geometry("400x400")
        win.configure(bg="#fff8e1")

        tk.Label(win, text=titulo, font=("Verdana", 14, "bold"), bg="#fff8e1", fg="#ff6f00").pack(pady=10)

        frame = tk.Frame(win, bg="#fff8e1")
        frame.pack(pady=10)

        tk.Label(frame, text="ID calificacion:", bg="#fff8e1").grid(row=0, column=0, padx=5, pady=5)
        id_cal_entry = tk.Entry(frame)
        id_cal_entry.grid(row=0, column=1, padx=5)



        tk.Label(frame, text="Nueva Nota:", bg="#fff8e1").grid(row=3, column=0, padx=5, pady=5)
        nueva_entry = tk.Entry(frame)
        nueva_entry.grid(row=3, column=1, padx=5)

        tk.Button(win, text="Actualizar Nota", command=lambda: op.actualizar_notas(id_cal_entry.get(),nueva_entry.get()), 
                bg="#f57c00", fg="white").pack(pady=15)
