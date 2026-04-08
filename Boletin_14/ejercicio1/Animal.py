from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    animales=[]
    def __init__(self, anio_nac, nombre=""):
        self._anio_nac = anio_nac
        self._nombre = nombre
        self._adoptado = False
        Animal.animales.append(self)

    @property
    def anio_nac(self):
        return self._anio_nac

    @property
    def nombre(self):
        return self._nombre

    @property
    def adoptado(self):
        return self._adoptado

    @adoptado.setter
    def adoptado(self, adoptado):
        self._adoptado = adoptado

    @classmethod
    def listarAnimalesNoAdoptados(cls):
        print("Animales no adoptados: ")
        for a in cls.animales:
            if not a.adoptado:
                print("Nombre :",a.nombre, a.anio_nac)

class Perro(Animal):
    def __init__(self, anio_nac, nombre,vacunado):
        super().__init__(anio_nac, nombre)
        self.__vacunado = vacunado

    @property
    def vacunado(self):
        return self.__vacunado

class Gato(Animal):
    def __init__(self, anio_nac, vacunado,nombre):
        super().__init__(anio_nac, nombre)
        self.__vacunado = vacunado

    @property
    def vacunado(self):
        return self.__vacunado

class Tortuga(Animal):
    def __init__(self, anio_nac,nombre):
        super().__init__(anio_nac, nombre)

