from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, dni,nombre):
        self._dni = dni
        self._nombre = nombre

    @abstractmethod
    def presentarse(self):
        pass

    @property
    def dni(self):
        return self._dni
    @property
    def nombre(self):
        return self._nombre

class Estudiante(Persona):
    def __init__(self, dni, nombre):
        super().__init__(dni, nombre)
        self.__notas={}

    def aniadir_nota(self,asignatura,nota):
        if nota < 0 or nota > 10:
            raise ValueError("La nota no puede ser mayor a 10 ni negativa")
        self.__notas[asignatura]=nota

    def presentarse(self):
        print(f"Estudiante: {self._nombre}")

    @property
    def notas(self):
        return self.__notas

class Profesor(Persona):
    def __init__(self, dni, nombre,especialidad):
        super().__init__(dni, nombre)
        self.__especialidad=especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    def presentarse(self):
        print(f"Profesor: {self._nombre}")

