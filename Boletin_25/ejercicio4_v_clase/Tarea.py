class Tarea:
    __listaTareas={}
    def __init__(self, id, titulo, prioridad):
        self.__id = id
        self.__titulo = titulo
        self.__prioridad = prioridad
        self.__completada = False
        if id in Tarea.__listaTareas:
            print("La tarea ya existe")
        else:
            Tarea.__listaTareas[id]=self

    @classmethod
    def mostrarListaTareasCompletadas(cls):
        print("TAREAS COMPLETADAS")
        contador=0
        for tarea in cls.__listaTareas.values():
            if tarea.__completada is True:
                print(f"[{tarea.__id}] {tarea.__titulo}")
                contador+=1
        if contador==0:
            print("No hay tareaas completadas")

    @classmethod
    def mostrarListaTareasNoCompletadas(cls):
        print("TAREAS NO COMPLETADAS")
        contador=0
        for tarea in cls.__listaTareas.values():
            if tarea.__completada is False:
                print(f"[{tarea.__id}] {tarea.__titulo}")
                contador+=1
        if contador==0:
            print("No hay tareas por completar")

    @classmethod
    def marcarComoCompletado(cls,id):
        if id in cls.__listaTareas:
            tarea=cls.__listaTareas[id]
            tarea.__completada=True
            print(f"Tarea {tarea.__titulo} ")
        else:
            print("La tarea no existe")


    @classmethod
    def eliminarTarea(cls,id):
        if id in Tarea.__listaTareas:
            Tarea.__listaTareas.pop(id)
            print(f"la tarea con id {id} fue eliminada")
        else:
            print(f"La tarea con id {id} no existe")



Tarea("P10","Hacer Duolingo",5)
Tarea("D055","Aprender Python",10)
Tarea("D055","Aprender Java",10) #esta está duplicada

Tarea.eliminarTarea("D055")
Tarea.eliminarTarea("D056")
Tarea.marcarComoCompletado("D055")

Tarea.mostrarListaTareasCompletadas()

