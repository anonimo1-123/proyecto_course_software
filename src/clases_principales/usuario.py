class Usuario:
    def __init__(self,name_user,type):
        self.__name_user = name_user
        self.__type = type


    @property
    def nombre_usuario(self):
        return self.__name_user

    @nombre_usuario.setter
    def nombre_usuario(self, value):
        self.__name_user = value

    @property
    def tipo_usuario(self):
        return self.__type

    @tipo_usuario.setter
    def tipo_usuario(self, value):
        self.__type = value
