import random
class Pokemon:

    def __init__(self,codigo,nombre,*tipo,peso_menor,peso_mayor,altura_minima,altura_maxima):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__tipo=tipo
        self.__peso=random.randint(peso_menor,peso_mayor)
        self.__altura=random.randint(altura_minima,altura_maxima)

    @property
    def verPokemon(self):
        return (f"#{self.__codigo}"
                f"Nombre: {self.__nombre}"
                f"Tipo(s): {self.__tipo}"
                f"Peso: {self.__peso}"
                f"Altura: {self.__altura}")

poke1=Pokemon("1","pikachu","electrico",2,4,50,80)


