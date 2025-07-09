import mysql.connector



class conexion_():
    def __init__(self):
        self.__database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="haker",
            database= "proyecto_software"
        )
        self.__cursor =self.database.cursor()

    @property
    def database(self):
        return self.__database


    @property
    def cursor(self):
        return self.__cursor

 


    def realizar_consultas(self,consulta):
        self.cursor.execute(consulta)
        return self.cursor

    def cerrar_conexion(self):
        self.cursor.close()
        self.database.close()
