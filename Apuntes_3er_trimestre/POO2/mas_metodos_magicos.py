class Cuenta():
    def __init__(self, saldo):
        self.__saldo=saldo

    def __str__(self):
        return "Saldo en cuenta: "+str(self.__saldo)

    #sobreescribimos el método add
    def __add__(self, cuenta2):
        #aca estoy sumando un objeto mas otro objeto
        self.__saldo=self.__saldo + cuenta2.__saldo
        #tengo que devolver el objerto que es el resultado de sumar los objetos
        return self

    def __gt__(self,cuenta2):
        mayor= True
        if cuenta2.__saldo >= self.__saldo:
            mayor= False
        return mayor


cuenta1=Cuenta(100)
cuenta2=Cuenta(250)
print(cuenta1)
"""
#Paso 1: intentamos sumar dos cuentas. pero da error porque el operador no está redefinido para hacer esta operación
cuenta1=cuenta1 + cuenta2
"""

cuenta1=cuenta1+cuenta2
print(cuenta1)

if cuenta1 > cuenta2:
    print("La cuenta 1 tiene más dinero")


