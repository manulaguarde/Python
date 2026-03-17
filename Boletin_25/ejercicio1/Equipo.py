class Equipo:
    def __init__(self,nombre_equipo,entrenador,*pokemons):
        if not len(pokemons)==3:
            raise ValueError("El equipo debe tener 3 pokemons")

        self.__nombre_equipo=nombre_equipo
        self.__entrenador=entrenador
        self.__pokemons=pokemons

    def verEquipo(self):
        texto=(f"Nombre del equipo: {self.__nombre_equipo}\n"
               f"Entrenador: {self.__entrenador}\n")
        for pokemon in self.__pokemons:
            texto += f"Pokemon: {pokemon.verPokemon}\n"

        return texto