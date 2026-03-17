import random
class Pokemon:

    def __init__(self,codigo,nombre,peso_menor,peso_mayor,altura_minima,altura_maxima,*tipo):
        if len(tipo)>2 or len(tipo)<1:
            raise ValueError("El pókemon debe tener 1 o 2 tipos")

        self.__codigo=codigo
        self.__nombre=nombre
        self.__tipo = tipo
        self.__peso=random.randint(peso_menor,peso_mayor)
        self.__altura=random.randint(altura_minima,altura_maxima)

    @property
    def verPokemon(self):
        if len(self.__tipo)==1:
            tipo_texto=self.__tipo[0]
        else:
            tipo_texto=self.__tipo[0]+" / "+self.__tipo[1]
        return (f"#{self.__codigo}. "
                f"Nombre: {self.__nombre}. "
                f"Tipo(s): {tipo_texto}. "
                f"Peso: {self.__peso}Kg. "
                f"Altura: {self.__altura}cm")



