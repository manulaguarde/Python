#los decoradores hacen que la funcion se comporte distinta
#son envoltorios (wrapp)

class Persona():
    def __init__(self,nombre, apellido):
        self._nombre=nombre
        self._apellido=apellido

class Funcionario():
    def __init__(self, cuerpo):
        self._cuerpo=cuerpo


class Profesor(Persona, Funcionario):
    def __init__(self,nombre,apellido,cuerpo):
        super().__init__(nombre,apellido)
        Funcionario.__init__(self,cuerpo)

    #usamos un método mágico
    def __str__(self):
        return self._apellido + ", "+ self._nombre+"("+self._cuerpo+")"

    #Paso 2: tengo que crear una función que se llame igual que el decorador que creamos y le pasamos como argumento otra función
    def mi_decorador(funcion):
        def envoltorio():
            print("Buenos días")
            funcion()
            print("Que tengas un buen día")
            
        return envoltorio

    #creamos un decorador
    @mi_decorador
    def saludo(self):
        print("Hola ", self._nombre)

profe=Profesor("Jose Maria","Morales","Educacion")

profe.saludo()