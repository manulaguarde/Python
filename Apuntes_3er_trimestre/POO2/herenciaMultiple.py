class Persona():
    def __init__(self,nombre, apellido):
        self._nombre=nombre
        self._apellido=apellido

class Funcionario():
    def __init__(self, cuerpo):
        self._cuerpo=cuerpo

# Cuando hereda de dos padres se ponen ambas clases separados por coma
class Profesor(Persona, Funcionario):
    #cuando llamo con super me refiero a la clase principal (o la primera que le pasamos) y para la otra tengo que llamar a la clase
    def __init__(self,nombre,apellido,cuerpo):
        super().__init__(nombre,apellido)
        Funcionario.__init__(self,cuerpo)


profe=Profesor("Jose Maria","Morales","Educacion")
