class Pokemon:
    numPokemon=0

    @classmethod
    def coleccion(cls):
        print("Tienes",cls.numPokemon," Pokemon(s) en tu colección")

    def __init__(self,num,nombre,*tipo): #asi permite que el número de tipos sea variable
        self.__numPokedex=num
        self.__pokemon_nombre=nombre
        self.__tipos=tipo
        Pokemon.numPokemon+=1

    @property
    def nombre(self):
        return self.__pokemon_nombre

    def verPokemon(self):
        print("#",self.__numPokedex, "-",self.__pokemon_nombre)
        print("Tipo(s): ",self.__tipos)