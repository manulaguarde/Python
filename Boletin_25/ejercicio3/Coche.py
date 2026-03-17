from Vehiculo import Vehiculo


class Coche(Vehiculo):
    def __init__(self, matricula, anio_venta, conductor):
        super().__init__(matricula, anio_venta,conductor)

    def seguro_todo_riesgo(self):
        total_seguro=0
        diferencia=Vehiculo.anio_actual-self.anio_venta
        if diferencia==1:
            total_seguro+=400
        elif diferencia==2:
            total_seguro+=500
        elif diferencia==3:
            total_seguro+=700
        else:
            total_seguro+=diferencia*250

        if self.conductor.puntos<8:
            total_seguro+=100

        return total_seguro

    def seguro_contra_terceros(self):
        total_seguro=250
        edad=self.conductor.edad
        anios_carnet=self.conductor.anios_con_carnet
        if self.conductor.puntos<8:
            total_seguro+=100
        if edad<24:
            total_seguro+=50
        if anios_carnet<2:
            total_seguro+=75

        return total_seguro

    def mostrar_vehiculo(self):
        texto = (f"Vehículo: coche. Matricula: {self.matricula}. Año de compra: {self.anio_venta}\n"
                 f"Conductor: {self.conductor.nombre}. Edad: {self.conductor.edad}. Años de carnet {self.conductor.anios_con_carnet}. Puntos: {self.conductor.puntos}\n"
                 f"Precio del seguro a todo riesgo: {self.seguro_todo_riesgo()}\n"
                 f"Precio del seguro a terceros: {self.seguro_contra_terceros()}\n")

        return texto
