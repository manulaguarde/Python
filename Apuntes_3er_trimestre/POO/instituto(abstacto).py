from abc import ABCMeta, abstractmethod


#CLASE ABSTACTA, ponemos entre paréntesis metaclass=ABCMeta y lo importamos
class Persona(metaclass=ABCMeta):
    def __init__(self, nombre,apellidos,tlf):
        self.nombre=nombre
        self.apellidos=apellidos
        self.telefono=tlf

    #decorador método abstracto
    @abstractmethod
    @property #puedo poner dos decoradores siempre que tengan sentido (no puedo poner decorador de metodo de clase y metodo estático)
    def verDatos(self):
        pass


class Profesor(Persona):
    def __init__(self, nombre, apellidos, tlf):
        super().__init__(nombre,apellidos,tlf)

    def verDatos(self):
        print(self.apellidos,", ",self.nombre)

class Alumno(Persona):
    def __init__(self,nombre,apellidos,tlf):
        super().__init__(nombre,apellidos,tlf)

    def verDatos(self):
        print(self.apellidos,", ",self.nombre)


profesor = Profesor("Pepe","Potamo",123456789)
alumno = Alumno("John","Doe",897654321)
#persona=Persona("Antonio","Cortés",147258369

profesor.verDatos()
alumno.verDatos()