class EmpresaLogistica:
    def __init__(self,nombre):
        self.__nombre = nombre
        self.__lista_vehiculos=[]

    def registrar_vehiculo(self,v):
        self.__lista_vehiculos.append(v)

    def generar_informe(self):
        gasto_total=0
        for vehiculo in self.__lista_vehiculos:
            print(vehiculo)
            gasto_total+=vehiculo.calcular_impuesto()

        print(f"Gasto total en impuestos: {gasto_total:.2f}€")