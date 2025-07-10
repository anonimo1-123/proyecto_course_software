from clase_tkinter import login_tk,gestor_admin_tk,gestor_alumno_tk,gestor_profesor_tk

def main():
    obj_login = login_tk.ventana()
    obj_login.mainloop()
    if obj_login.tipo_user == "admin":
        obj_gest = gestor_admin_tk.ventana()
        obj_gest.mainloop()
    elif obj_login.tipo_user == "profesor":
        obj_gest = gestor_profesor_tk.ventana()
        obj_gest.mainloop()
    elif obj_login.tipo_user == "estudiante":
        obj_gest = gestor_alumno_tk.ventana()
        obj_gest.mainloop()
    else:
        print("!Fallo de sesion")
    


if __name__ == "__main__":
    main()