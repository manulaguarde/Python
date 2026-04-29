class Contacto:
    def __init__(self, nombre, categoria, edad, apellido=""):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__categoria = categoria
        self.__edad = int(edad)

    def __str__(self):
        return f"Nombre: {self.__nombre}\nApellido: {self.__apellido}\nEdad: {self.__edad}\nCategoria: {self.__categoria}"