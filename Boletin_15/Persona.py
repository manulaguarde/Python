from abc import ABCMeta, abstractmethod
class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido,centro):
        self._nombre = nombre
        self._apellido = apellido
        self._centro = centro


    @abstractmethod
    def __str__(self):
        pass

