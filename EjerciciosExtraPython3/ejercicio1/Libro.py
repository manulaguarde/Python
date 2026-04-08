import random

class Libro:
    def __init__(self,codigo,titulo,max_numero_paginas,min_numero_paginas,max_peso,min_peso,*genero):
        self.__codigo = codigo
        self.__titulo = titulo
        if len(genero) < 1:
            raise ValueError("Debe tener al menos un género")
        self.__genero = []
        if len(genero) > 3:
            for i in range (3):
                self.__genero.append(genero[i])
        self.__num_paginas= random.randint(min_numero_paginas, max_numero_paginas)
        self.__peso= random.randint(min_peso, max_peso)

    def mostrar_info(self):
        print("Codigo: ",self.__codigo)
        print("Titulo: ",self.__titulo)
        print("Genero: ",end="")
        for g in self.__genero:
            print(g)
        print("Peso: ",self.__peso)
        print("Número de páginas: ",self.__num_paginas)