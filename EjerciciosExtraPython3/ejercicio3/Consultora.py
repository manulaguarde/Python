class Consultora:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__proyectos={}

    def vincular_proyecto(self,proyecto):
        if proyecto.id in self.__proyectos:
            raise Exception('Proyecto ya existente')
        self.__proyectos[proyecto.id]=proyecto

    def obtener_balance_total(self):
        total=[]
        for proyecto in self.__proyectos:
            total.append(self.__proyectos[proyecto].presupuesto)

        return sum(total)

    def informe_detallado(self):
        print("Informe detallado\nNombre Consultora: ",self.__nombre)
        print("Proyectos:")
        for proyecto in self.__proyectos:
            print("Nombre Proyecto: ",self.__proyectos[proyecto].nombre)
            print("Presupuesto: ",self.__proyectos[proyecto].presupuesto)
            if len(self.__proyectos[proyecto].miembros)==0:
                print("Sin personal asignado")
            else:
                for miembro in self.__proyectos[proyecto].miembros:
                    print("Nombre miembro: ",miembro)

    def extraer_proyectos_vip(self,umbral):
        proyectos_vip={}
        for proyecto in self.__proyectos:
            if self.__proyectos[proyecto].presupuesto>umbral:
                proyectos_vip[proyecto.id]=proyecto

        return proyectos_vip
