class Sucursal:
    codigo_banco = "ES68 1234"
    def __init__(self, direccion,provincia,cod):
        codigo=str(cod)
        if len(codigo)>4 or len(codigo)<1:
            raise ValueError("El codigo no es valido")

        self.__codigo=codigo.zfill(4)
        self.__direccion=direccion
        self.__provincia=provincia
        self.__cuentas=[]

    def cuentas(self):
        return self.__cuentas

    def listarCuentas(self):
        print("Sucursal: ",self.__codigo)
        for cuenta in self.__cuentas:
            print(cuenta.codigo)


class Cliente:
    def __init__(self,nombre,apellidos,nif,telefono,sucursal):
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__nif=nif
        self.__telefono=telefono
        self.__sucursal=sucursal
        self.__cuentas=[]

    def listarCuentas(self):
        print(self.__nombre,self.__apellidos)
        for cuenta in self.__cuentas:
            print(cuenta.codigo)

    @property
    def cuentas(self):
        return self.__cuentas

class Cuenta:

    def __init__(self, cod,saldo,sucursal,titular1,titular2=None):

        """codigo=str(cod)
        if len(codigo)>12 or len(codigo)<1:
            raise ValueError("El codigo no es valido")

        if len(titulares)>2 or len(titulares)<1:
            raise ValueError("Tienen que haber 1 o 2 titulares")"""

        self.__codigo=cod.zfill(12)
        self.__saldo=saldo
        self.__sucursal=sucursal
        sucursal.cuentas.append(self)
        self.__titular1=titular1
        titular1.cuentas.append(self)
        if titular2 is not None:
            self.__titular2=titular2
            titular2.cuentas.append(self)

    @property
    def codigo(self):
        return self.__codigo



sucursal1= Sucursal("calle del pez","Madrid","0012")
cliente1=Cliente("Jose", "Morales", "123", "666", sucursal1)
cliente2=Cliente("Ana", "Lopez", "456", "777", sucursal1)

cuenta1=Cuenta("012345678912",120.50,sucursal1,cliente1)
cuenta2=Cuenta("987654321098",250,sucursal1,cliente1,cliente2)

cliente1.listarCuentas()
sucursal1.listarCuentas()

