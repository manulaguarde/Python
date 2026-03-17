from abc import ABCMeta, abstractmethod
from datetime import date
class Vehiculo(metaclass=ABCMeta):
    anio_actual=date.today().year
    def __init__(self, matricula, anio_venta, conductor):
        self.__matricula = matricula
        self.__anio_venta = anio_venta
        self.__conductor = conductor

    @abstractmethod
    def seguro_todo_riesgo(self):
        pass
    @abstractmethod
    def seguro_contra_terceros(self):
        pass

    @abstractmethod
    def mostrar_vehiculo(self):
        pass

    @property
    def matricula(self):
        return self.__matricula
    @property
    def anio_venta(self):
        return self.__anio_venta

    @property
    def conductor(self):
        return self.__conductor
