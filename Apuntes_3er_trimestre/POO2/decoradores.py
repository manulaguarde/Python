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

    #Paso 2: tengo que crear una función que se llame igual que el decorador que creamos y le pasamos como argumento otra función, y devuelve una funcion
    #recibe como argumento la funcion que aparece debajo del decorador. (funcion=saludo)

    def mi_decorador(funcion):
        #aqui dentro hacemos la otra funcion que tiene que devolver
        def envoltorio(self):
            print("Buenos días cuerpo de",self._cuerpo) #esto es la decoración, es opcional
            funcion(self) #el momento que queremos que se ejecute nuestra función
            print("Que tengas un buen día") #otra decoración
            
        return envoltorio

    #creamos un decorador
    @mi_decorador
    def saludo(self):
        print("Hola ", self._nombre)

profe=Profesor("Jose Maria","Morales","Educacion")

profe.saludo()