class Pregunta:
    preguntas=[]
    def __init__(self, enunciado, rsptaCorrecta, rspta2, rspta3):
        self.__enunciado = enunciado
        self.__rsptaCorrecta = rsptaCorrecta
        self.__rspta2 = rspta2
        self.__rspta3 = rspta3

        Pregunta.preguntas.append(self)

    @property
    def enunciado(self):
        return self.__enunciado

    @property
    def rsptaCorrecta(self):
        return self.__rsptaCorrecta

    @property
    def rspta2(self):
        return self.__rspta2

    @property
    def rspta3(self):
        return self.__rspta3

    @classmethod
    def mostrarPreguntas(cls):
        return cls.preguntas