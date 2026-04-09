from abc import ABCMeta,abstractmethod

class Personaje(metaclass=ABCMeta):

    def __init__(self,nombre):
        self._nombre=nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nom):
        self._nombre=nom

    @abstractmethod
    def __str__(self):
        pass

    @classmethod
    def mostrar_personajes(cls,lista_personajes):
        for personaje in lista_personajes:
            print(personaje)


class Futbolista(Personaje):
    def __init__(self,nombre,num_dorsal,altura,equipo,edad):
        super().__init__(nombre)
        self.__num_dorsal=num_dorsal
        self.__altura=altura
        self.__equipo=equipo
        self.__edad=edad

    def __str__(self):
        cad = f"Nombre: {self._nombre}\n"
        cad+=f"Altura: {self.__altura}\nEquipo: {self.__equipo}\nEdad: {self.__edad} años\nDorsal habitual: {self.__num_dorsal}\n"
        return cad

class PjAnime(Personaje):
    def __init__(self,nombre,anime,mangaka):
        super().__init__(nombre)
        self.__anime=anime
        self.__mangaka=mangaka

    def __str__(self):
        cad = f"Nombre: {self._nombre}\n"
        cad+=f"Anime {self.__anime}\nMangaka: {self.__mangaka}\n"
        return cad


class Superheroe(Personaje):
    def __init__(self,nombre,nom_superheroe,editorial):
        super().__init__(nombre)
        self.__superheroe=nom_superheroe
        self.__editorial=editorial

    def __str__(self):
        cad = f"Nombre: {self._nombre}\n"
        cad+=f"Superhéroe: {self.__superheroe}\nEditorial: {self.__editorial}"
        return cad


personaje1=Futbolista("Lamine Yamal",19,1.79,"Futbol Club Barcelona",18)
personaje2=PjAnime("Shinji Ikari","Neon Genesis Evangelion","Yoshiyuki Sadamoto")
personaje3=Superheroe("Peter Parker","Spiderman","Marvel")

print(personaje1.nombre)
print() #pongo esto para separar acá para que sea mas legible
print(personaje1) #estos ya están debidamente separados en el método mágico
print(personaje2)
print(personaje3)
print() #otro print solo para legibilidad

lista=[personaje1,personaje2,personaje3]
Personaje.mostrar_personajes(lista)
