from clase_tkinter import login_tk,gestor_admin_tk

def main():
    obj_login = login_tk.ventana()
    obj_login.mainloop()
    if obj_login.tipo_user == "Administrador":
        obj_gest = gestor_admin_tk.ventana()
        obj_gest.mainloop()
    elif obj_login.tipo_user == "Profesor":
        pass
    elif obj_login.tipo_user == "Estudiante":
        pass
    else:
        print("!Fallo de sesion")
    


if __name__ == "__main__":
    main()