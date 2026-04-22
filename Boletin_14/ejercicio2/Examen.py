from Pregunta import Pregunta
import random

class Examen:
    diccionarioPreguntas={}
    respuestas_ordenadas={}
    solucion=[]

    def __init__(self,numPreguntas):
        self.__preguntasExamen=random.sample(Pregunta.mostrarPreguntas(),numPreguntas)
        self.__respuestas_correctas=[]
        for pregunta in self.__preguntasExamen:
            Examen.diccionarioPreguntas[pregunta.enunciado]=[pregunta.rsptaCorrecta,pregunta.rspta2,pregunta.rspta3]
            Examen.respuestas_ordenadas[pregunta.enunciado]=random.sample([1,2,3],3)
            self.__respuestas_correctas.append(pregunta.rsptaCorrecta)
        self.__respuestas_usuario=[]


    @classmethod
    def mostrarPreguntas(cls):
        i=0
        for pregunta,respuesta in cls.diccionarioPreguntas.items():
            car = ord('A')
            print(pregunta)
            cls.respuestas_ordenadas[car]=respuesta[i]
            i+=1
            random.shuffle(respuesta)
            for r in respuesta:
                print(f"{chr(car)}){r}")
                car+=1

    def setRespuestasUsuario(self,rsta):
        self.__respuestas_usuario.append(rsta)

    def corregirExamen(self):
        fallos=0
        for i in range (self.__respuestas_correctas):
            if self.__respuestas_correctas[i]!=self.__respuestas_usuario[i]:
                fallos+=1

        return fallos

    def mostrarRespuestas(self):
        for respuesta in self.__respuestas_correctas:
            print(respuesta,end=" ")

    def mostrarSolucion(self):
        for respuesta in self.solucion:
            print(respuesta,end=") ")