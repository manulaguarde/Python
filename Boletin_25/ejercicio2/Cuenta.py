class Cuenta:
    codigo_banco="ES68 1234"
    def __init__(self, cod,saldo,sucursal,*titulares):

        codigo=str(cod)
        if len(codigo)>12 or len(codigo)<1:
            raise ValueError("El codigo no es valido")

        if len(titulares)>2 or len(titulares)<1:
            raise ValueError("Tienen que haber 1 o 2 titulares")

        self.__codigo=codigo.zfill(12)
        self.__saldo=saldo
        self.__sucursal=sucursal
        self.__titulares=titulares

        sucursal.agregar_cuenta(self)

        for titular in titulares:
            titular.agregar_cuenta(self)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def saldo(self):
        return self.__saldo