class Tareas:
    def __init__(self):
        self.__tareas={}

    def agregar_tarea(self,tarea):
        if self.__tareas.get(tarea.identificacion) is None:
            self.__tareas[tarea.identificacion]=[tarea.titulo,tarea.prioridad,tarea.completado]
            return f"Tarea {tarea.titulo} ('{tarea.identificacion}') añadida"

        return f"Error: {tarea.identificacion} ya existente"

    def eliminar_tarea(self,id):
        tarea=self.__tareas.pop(id,None)
        if tarea is None:
            return f"Error: No se encontró una tarea con ID {id}"
        return f"Tarea con ID {id} ('{tarea[0]}') eliminada"

    def marcar_como_completadas(self,id):
        if self.__tareas.get(id) is not None:
            self.__tareas[id][2]=True
            return f"Tarea ID {id} '{self.__tareas[id][0]}' marcada como completada."
        return f"Error: No se encontró una tarea con ID {id}"

    def mostrar_tareas_completadas(self):
        contador_tareas=0
        print("- LISTADO DE TAREAS")
        for key, value in self.__tareas.items():
            if value[2] is True:
                print(f"[{key}] {value[0]} (Prioridad: {value[1]})")
                contador_tareas += 1
        if contador_tareas==0:
            print("No hay tareas completadas.")

    def mostrar_tareas_no_completadas(self):
        contador_tareas=0
        print("- LISTADO DE TAREAS")
        for key, value in self.__tareas.items():
            if value[2] is False:
                print(f"[{key}] {value[0]} (Prioridad: {value[1]})")
                contador_tareas += 1
        if contador_tareas==0:
            print("No hay tareas completadas.")