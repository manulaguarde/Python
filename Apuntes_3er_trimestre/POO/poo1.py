#Se trata de identificar elementos de la realidad con elementos de programación, elementos que tienen una identidad, o son tangibles
#Y modelarlo con código

#Una clase es un modelo que representa una identidad. Y un objeto es cada instancia de esa clase, en la clase alumno cada alumno en concreto seria un objeto

class Alumno: #se definen en singular y en mayúscula
    #constructor
    def __init__(self,edad): #siempre se tiene que hacer el constructor de esta manera
        self.edad=edad
        pass

trista = Alumno(33) #son copias y cada uno se particulariza y tiene un espacio separado
galdeano=Alumno(28) #Alumno() es el constructor
nicolle=Alumno(26)