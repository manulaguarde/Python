from ejercicio1.Animal import Tortuga, Gato, Perro


class Cliente:
    def __init__(self, nombre,apellido,edad,telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__telefono = telefono
        self.__animales=[]

    def adoptar(self,animal):
        perro=0
        gato=0
        tortuga=0
        for a in self.__animales:
            if isinstance(a,Tortuga):
                tortuga+=1
            elif isinstance(a,Perro):
                perro+=1
            elif isinstance(a,Gato):
                gato+=1

        if len(self.__animales) >= 4:
            return "No se puede adoptar mas de 4 animales"
        elif perro >= 2 and isinstance(animal,Perro):
            return "No se puede adoptar mas de 2 perros"
        elif gato >= 3 and isinstance(animal,Gato):
            return "No se puede adoptar mas de 3 gatos"
        elif tortuga >= 1 and isinstance(animal,Tortuga):
            return "No se puede adoptar mas de 1 tortuga"

        if animal.adoptado:
            return "El animal ya ha sido adoptado"

        animal.adoptado=True
        self.__animales.append(animal)

    def listarAnimales(self):
        for a in self.__animales:
            print("Nombre: ",a.nombre)
            print("Año de nacimiento: ",a.apellido)
            print("Vacunado: ", a.vacunado)

