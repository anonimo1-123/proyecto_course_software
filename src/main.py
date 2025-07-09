from clase_tkinter import login_tk
def main():
    obj_login = login_tk.ventana()
    obj_login.mainloop()
    print(obj_login.tipo_user)
    


if __name__ == "__main__":
    main()