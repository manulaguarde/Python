from Cuenta import Cuenta

class Cliente:
    def __init__(self,nombre,apellidos,nif,telefono,sucursal):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__nif=nif
        self.__telefono=telefono
        self.__sucursal=sucursal
        self.__cuentas=[]

    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def listar_clientes(self):
        total=0
        texto= f"{self.__nombre} {self.__apellidos}. Cliente de la sucursal {self.__sucursal.codigo} ({self.__sucursal.provincia})"

        for cuenta in self.__cuentas:
            texto+=f"\n{Cuenta.codigo_banco} {self.__sucursal.codigo} {cuenta.codigo} - Saldo: {cuenta.saldo}€"
            total+=cuenta.saldo

        texto+=f"\nSaldo total: {total}"
        return texto


