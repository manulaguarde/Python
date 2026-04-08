from Consultora import Consultora
class Proyecto:
    def __init__(self,id,nombre,presupuesto,consultora):
        self.__id = id
        self.__nombre = nombre
        self.__presupuesto = presupuesto
        self.__miembros = []
        consultora.vincular_proyecto(self)

    def gestionar_miembro(self,nombre,accion):
        if accion == "añadir":
            if nombre in self.__miembros:
                print('Miembro ya existente')
            else:
                self.__miembros.append(nombre)
        if accion == "eliminar":
            if nombre in self.__miembros:
                self.__miembros.remove(nombre)
            else:
                print('Miembro no encontrado')


    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def presupuesto(self):
        return self.__presupuesto
    @property
    def miembros(self):
        return self.__miembros
