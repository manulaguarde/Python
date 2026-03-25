#METODOS MAGICOS (tambien llamados dundee)
#tienen dos subrayados delante y dos detras y el nombre en el medio, como __init__
#sirven para sobreescribir, redefinir
#no se pueden invocar directamente, hay que redefinir

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


profe=Profesor("Jose Maria","Morales","Educacion")
"""
print(profe) #no sale nada legible, necesito convertirlo a cadena
"""

#pero ahora sobrescribiendo el método str ya me lo imprime como un string (similar al toString)
print(profe)


