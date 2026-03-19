from Tareas import Tareas
from Tarea import Tarea

tareas=Tareas()

tareas.agregar_tarea(Tarea("E25","Enviar email al jefe",5))
tareas.agregar_tarea(Tarea("P33","Aprender Python",2))
tareas.agregar_tarea(Tarea("F47","Revisar facturas",7))

print(tareas.agregar_tarea(Tarea("P10","Comprar billetes",9)))
print(tareas.agregar_tarea(Tarea("P10","Comprar billetes",9)))
print(tareas.eliminar_tarea("P10"))
print(tareas.eliminar_tarea("X1005"))

print(tareas.marcar_como_completadas("W088"))

print(tareas.mostrar_tareas_completadas())

print(tareas.mostrar_tareas_no_completadas())



"""[E25] Enviar email al jefe (Prioridad: 5)
[P33] Aprender Python (Prioridad: 2)
[F47] Revisar facturas (Prioridad: 7)
Tarea ID D055 'Completar retos de Duolingo'
Tarea 'Comprar billetes' (ID: P10"""

"""
ID X1005
ID W088
"""