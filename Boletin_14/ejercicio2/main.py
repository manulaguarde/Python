"""
Respuesta a la pregunta 1: B
Respuesta a la pregunta 2: C
Respuesta a la pregunta 3: A
Respuesta a la pregunta 4: A
Número de fallos: 3
SOLUCIÓN:
C) A) B) A)
Has tenido 3 fallos"""

from Examen import Examen
from Pregunta import Pregunta



p1=Pregunta("¿Qué señales son azules?","informativas","peligro","no hay señales azules")
p2=Pregunta("¿Puedo circular en caballo por autovía?","De ninguna forma","En casos especiales","Si, si llevas gorro de vaquero")
p3=Pregunta("¿Quién tiene preferencia en un cruce?","Quién esté señalizado. Si no, el de la derecha","Siempre el de la derecha","El que antes entre")
p4=Pregunta("¿Velocidad máxima en autopistas?","120","60","la que de tu coche")

numPreguntas=int(input("Numero de preguntas: "))
examen=Examen(numPreguntas)
#examen.seleccionarPreguntas(2)
examen.mostrarPreguntas()
respuestas=[]
"""for i in range(numPreguntas):
    #print(f"Respuesta a la pregunta {i+1}:")
    examen.setRespuestasUsuario(input(f"Respuesta a la pregunta {i+1}"))"""

examen.mostrarSolucion()
