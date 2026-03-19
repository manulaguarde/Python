class Tarea:
    def __init__(self, id, titulo, prioridad):
        self.__id = id
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__completado = False

    @property
    def identificacion(self):
        return self.__id
    @property
    def titulo(self):
        return self.__titulo
    @property
    def prioridad(self):
        return self.__prioridad
    @property
    def completado(self):
        return self.__completado

    @completado.setter
    def completado(self, completado):
        self.__completado = completado






