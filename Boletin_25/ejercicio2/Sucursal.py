from Cuenta import Cuenta
class Sucursal:
    def __init__(self, direccion,provincia,cod):
        codigo=str(cod)
        if len(codigo)>4 or len(codigo)<1:
            raise ValueError("El codigo no es valido")

        self.__codigo=codigo.zfill(4)
        self.__direccion=direccion
        self.__provincia=provincia
        self.__cuentas=[]

    def agregar_cuenta(self,cuenta):
        self.__cuentas.append(cuenta)

    def listar_sucursales(self):
        total=0
        texto=f"Cuentas de la Sucursal {self.__codigo} ({self.__provincia})"
        for cuenta in self.__cuentas:
            texto+=f"\n{Cuenta.codigo_banco} {self.__codigo} {cuenta.codigo} - Saldo: {cuenta.saldo}"
            total+=cuenta.saldo
        texto+=f"\n Saldo total:{total}"
        return texto

    @property
    def codigo(self):
        return self.__codigo
    @property
    def provincia(self):
        return self.__provincia
