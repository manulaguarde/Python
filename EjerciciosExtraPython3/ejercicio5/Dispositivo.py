from abc import ABC, abstractmethod
from GestorEnergia import GestorEnergia
class Dispositivo(ABC):

    def __init__(self,nombre,consumo_base,estado):
        self._nombre = nombre
        self._consumo_base = consumo_base
        self._estado = estado
        GestorEnergia.agregar_dispositivo(self)

    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self,estado):
        self._estado = estado

    @abstractmethod
    def obtener_consumo(self):
        pass

class AireAcondicionado(Dispositivo):

    def __init__(self,nombre,consumo_base,estado,temperatura_objetivo):
        super().__init__(nombre,consumo_base,estado)
        self.__temperatura_objetivo = temperatura_objetivo

    def obtener_consumo(self):
        consumo=self._consumo_base
        diferencia=24-self.__temperatura_objetivo
        if self._estado:
            consumo+=diferencia*20
            return consumo
        else:
            return 0

    @property
    def temperatura_objetivo(self):
        return self.__temperatura_objetivo

    @temperatura_objetivo.setter
    def temperatura_objetivo(self,valor):
        self.__temperatura_objetivo=valor

class SensorPresencia(Dispositivo):
    def __init__(self,nombre,consumo_base,estado,detectado):
        super().__init__(nombre,consumo_base,estado)
        self.__detectado = detectado
        self.__dispositivos_vinculados=[]

    def obtener_consumo(self):
        if self._estado:
            return self._consumo_base
        else:
            return 0

    def vincular_dispositivo(self,dispositivo):
        self.__dispositivos_vinculados.append(dispositivo)

    def encender_dispositivos(self):
        if self.__detectado:
            for dispositivo in self.__dispositivos_vinculados:
                dispositivo._estado=True
        else:
            for dispositivo in self.__dispositivos_vinculados:
                dispositivo._estado=False

    @property
    def detectado(self):
        return self.__detectado

    @detectado.setter
    def detectado(self,detectado):
        self.__detectado = detectado
        self.encender_dispositivos()