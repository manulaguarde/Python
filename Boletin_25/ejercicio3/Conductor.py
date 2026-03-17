from datetime import date
class Conductor:
    anio_actual=date.today().year
    def __init__(self, nombre, nif, anio_nacimiento, anio_carnet, puntos):
        self.__nombre = nombre
        self.__nif = nif
        self.__anio_nacimiento = anio_nacimiento
        self.__anio_carnet = anio_carnet
        self.__puntos = puntos

    @property
    def anio_carnet(self):
        return self.__anio_carnet
    @property
    def puntos(self):
        return self.__puntos
    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento

    @property
    def edad(self):
        return Conductor.anio_actual-self.__anio_nacimiento

    @property
    def anios_con_carnet(self):
        return Conductor.anio_actual-self.__anio_carnet

    @property
    def nombre(self):
        return self.__nombre