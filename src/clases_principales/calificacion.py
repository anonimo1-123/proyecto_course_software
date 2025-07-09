class caficacion:
    def __init__(self,valor,name_estudiante,curso,docente):
        self.__valor = valor
        self.__name_estudiante = name_estudiante
        self.__curso = curso
        self.__docente = docente

    @property
    def calificacion(self):
        return self.__valor

    @calificacion.setter
    def calificacion(self, value):
        self.__valor = value

    @property
    def nombre_de_estudiante(self):
        return self.__name_estudiante

    @nombre_de_estudiante.setter
    def nombre_de_estudiante(self, value):
        self.__name_estudiante = value

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, value):
        self.__curso = value

    @property
    def docente(self):
        return self.__docente

    @docente.setter
    def docente(self, value):
        self.__docente = value
