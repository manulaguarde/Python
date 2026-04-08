class Estante:
    def __init__(self,codigo):
        self.__codigo = codigo
        self.__libros=[]

    def agregar_libro(self,libro):
        if len(self.__libros)<5:
            self.__libros.append(libro)
        else:
            print("El estante está completo")

    def mostrar_estante(self):
        for libro in self.__libros:
            libro.mostrar_info()

