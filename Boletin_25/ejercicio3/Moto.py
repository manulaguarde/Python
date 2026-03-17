from ejercicio3.Vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, matricula, anio_venta, conductor):
        super().__init__(matricula,anio_venta,conductor)

    def seguro_todo_riesgo(self):
        return "No se hacen seguros a todo riesgo a motos"

    def seguro_contra_terceros(self):
        total_seguro=200
        edad = self.conductor.edad
        anios_carnet = self.conductor.anio_carnet
        if self.conductor.puntos<8:
            total_seguro+=150
        if edad<24:
            total_seguro+=25
        if anios_carnet<2:
            total_seguro+=50

        return total_seguro

    def mostrar_vehiculo(self):
        texto=(f"Vehículo: moto. Matricula: {self.matricula}. Año de compra: {self.anio_venta}\n"
               f"Conductor: {self.conductor.nombre}. Edad: {self.conductor.edad}. Años de carnet {self.conductor.anios_con_carnet}. Puntos: {self.conductor.puntos}\n"
               f"Precio del seguro a terceros: {self.seguro_contra_terceros()}\n"
               f"{self.seguro_todo_riesgo()}")

        return texto

"""Vehículo: coche. Matrícula: 6310NXB. Año de compra: 2024
Conductor: José María Morales. Edad: 57. Años de carnet: 39 . Puntos: 10
Precio del seguro a todo riesgo: 500€
Precio del seguro a teceros: 250€
"""