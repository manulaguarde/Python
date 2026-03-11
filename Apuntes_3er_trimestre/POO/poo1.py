#Se trata de identificar elementos de la realidad con elementos de programación, elementos que tienen una identidad, o son tangibles
#Y modelarlo con código

#Una clase es un modelo que representa una identidad. Y un objeto es cada instancia de esa clase, en la clase alumno cada alumno en concreto seria un objeto

class Alumno: #se definen en singular y en mayúscula
    #En Python no hay que inicializar las variables

    numAlumnos=0 #es un atributo estático que pertenece a toda la clase, lo comparten todos los objetos de la clase

    #constructor
    def __init__(self,nombre,edad,dni): #siempre se tiene que hacer el constructor de esta manera
        #Aca se inicializan las variables, en el mismo momento que se usan y con el self que equivale al this de Java
        self.__edad=edad # __ asi es un aatributo privado
        self.__nombre=nombre
        self.__dni=dni
        Alumno.numAlumnos+=1 #Para utilizar un atributo de clase, hay que poner el nombre de la clase y un punto antes.

    #el self tiene que aparecer siempre en el primer lugar, (en la definición, no cuando invocamos el metodo)
    def verDatos(self):
        print("Nombre: ",self.__nombre, "Edad: ",self.__edad,"DNI: ",self.__dni)

    """    
    #GETTERS Y SETTERS (similar a Java)
    def setEdad(self,edad):
        self.__edad=edad
        
    def getEdad(self):
        return self.__edad"""

    #GETTERS Y SETTERS EN PYTHON
    #hay que usar lo que se llama un decorador (un elemento que empieza con un arroba)
    # 'property' es un decorador que indica que a continuación vamos a definir un getter
    @property
    def edad(self): #llamo al metodo igual que el atributo (pero sin el doble underline)
        return self.__edad

    @edad.setter # este es el decorador para setters
    def edad(self,ed):
        self.__edad=ed

    #METODOS ESTATICOS Y METODOS DE CLASE
    #en los metodos de clase puedo utilizar atributos de clase, pero no atributos de objetos
    @classmethod
    def matriculados(cls): #cls hace referencia a la clase, seria igual que poner Alumno.numAlumnos
        return cls.numAlumnos

    #EN LOS ESTÁTICOS NO PUEDO UTILIZAR ATRIBUTOS DE CLASE NI ATRIBUTOS DE OBJETOS
    @staticmethod
    def matriculados2():
        return Alumno.matriculados #NO funciona porque llama a un metodo de clase

trista = Alumno("Leandro Trista",33,"11222333X") #son copias y cada uno se particulariza y tiene un espacio separado
galdeano=Alumno("Tomas",28,"12356134F") #Alumno() es el constructor, es el nombre de la clase no del constructor
nicolle=Alumno("Nicolle",26,"534453451T")

"""
#como en Java
#trista.setEdad(55)
print(trista.getEdad)"""


#UTILIZACIÓN GETTERS Y SETTERS EN PYTHON
print(trista.edad) #aparenta trabajar directamente con el atributo pero realmente es el metodo lo que estoy invocando
trista.edad=55
print(trista.edad)

#print(Alumno.numAlumnos)

print(Alumno.matriculados())

