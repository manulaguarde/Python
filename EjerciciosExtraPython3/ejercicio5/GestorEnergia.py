from ejercicio5.Dispositivo import AireAcondicionado, SensorPresencia


class GestorEnergia:
    __dispositivos=[]

    @classmethod
    def agregar_dispositivo(cls,dispositivo):
        cls.__dispositivos.append(dispositivo)

    @classmethod
    def conocer_consumo(cls):
        total=0
        for dispositivo in cls.__dispositivos:
            total+=dispositivo.obtener_consumo()

        return total
    @classmethod
    def reporte_critico(cls):
        if cls.conocer_consumo()>2000:
            for dispositivo in cls.__dispositivos:
                if isinstance(dispositivo,AireAcondicionado):
                    dispositivo.temperatura_objetivo=24

        if cls.conocer_consumo()>2000:
            for dispositivo in cls.__dispositivos:
                if not isinstance(dispositivo,SensorPresencia):
                    dispositivo.estado=False



