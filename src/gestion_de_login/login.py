
import sys
import os
sys.path.append(os.path.abspath("..")+"/proyecto_de_software/src/conexion_sql")
import conexion

class login_:
    def __init__(self,user,contraseña):
        self.user=user
        self.contraseña = contraseña

    def comprobacion(self):
        conx = conexion.conexion_()
        consulta = conx.realizar_consultas(f"SELECT nombre_user ,password_,rol_idrol FROM usuario where nombre_user='{self.user}' and password_='{self.contraseña}'")
        listar_consulta = consulta.fetchall()
        conx.cerrar_conexion()
        if len(listar_consulta)!= 0:
            return True,listar_consulta[0][2]
        else :
            return False,None

    def comprobacion_type_user(self,type):
        conx = conexion.conexion_()
        consulta = conx.realizar_consultas(f"SELECT name_rol FROM rol where idrol='{type}'")
        listar_consulta = consulta.fetchall()
        conx.cerrar_conexion()
        return listar_consulta[0][0]
    


        