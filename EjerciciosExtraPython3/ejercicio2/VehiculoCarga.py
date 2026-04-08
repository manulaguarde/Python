from abc import ABCMeta, abstractmethod
from datetime import datetime
class VehiculoCarga(metaclass=ABCMeta):
    def __init__(self,matricula,tara,anio_fab):
        self._matricula = matricula
        self._tara = tara
        self._antiguedad= datetime.now().year - anio_fab

    @abstractmethod
    def calcular_impuesto(self):
        pass

    def __str__(self):
        return f"Matricula: {self._matricula}\n"

class Camion(VehiculoCarga):
    def __init__(self,matricula,tara,max_capacidad,anio_fab):
        super().__init__(matricula,tara,anio_fab)
        self.__max_capacidad = max_capacidad

    def calcular_impuesto(self):
        base=100
        if self.__max_capacidad > 1000:
            base+=self.__max_capacidad*0.01
        if self._antiguedad > 10:
            base+=50

        return base

    def __str__(self):
        return super().__str__()+f"Tipo: Camión\nImpuesto: {self.calcular_impuesto()}"

class Furgoneta(VehiculoCarga):
    def __init__(self,matricula,tara,anio_fab,es_isotermica):
        super().__init__(matricula, tara, anio_fab)
        self.__es_isotermica = es_isotermica


    def calcular_impuesto(self):
        base=80
        if self.__es_isotermica:
            base+=40
        if self._antiguedad < 2:
            base-=base*0.20

        return base

    def __str__(self):
        return super().__str__() + f"Tipo: Furgoneta\nImpuesto: {self.calcular_impuesto()}"