class Pokemon:
    numPokemon=0

    @classmethod
    def coleccion(cls):
        print("Tienes",cls.numPokemon," Pokemon(s) en tu colección")

    #En python no podemos identificar y crear varios constructores, el constructor tiene que ser unico, tenemos que hacerlo dentro del mismo constructor
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

#HERENCIA
#LA CLASE POKEMON LEGENDARIO HEREDA DE POKEMON, ponemos la clase padre entre paréntesis
class PokemonLegendario(Pokemon):
    #contructor de la clase PokemonLegendario
    def __init__(self,num,nombre,*tipo):
        #invocamos constructor de la clase Pokemon
        super().__init__(num,nombre,*tipo)

    def verPokemon(self):
        print("Pokemon Legendario")
        super().verPokemon()
