"""1. Cada tarea tendra:
   - Nombre de la tarea.
   - Fecha limite en formato "dd/mm/YYYY".
   - Conjunto de etiquetas (por ejemplo: "urgente", "casa", "trabajo").
2. Pide al usuario 3 tareas y guarda cada una en un diccionario tareas asi:
   - Clave: nombre de la tarea.
   - Valor: diccionario con:
     - "fecha_limite": datetime.
     - "etiquetas": conjunto de etiquetas.
3. Usa try/except para validar las fechas.
4. Recorre las tareas y:
   - Muestra cada tarea formateada con f-strings:
     Tarea: NOMBRE - Limite: Lunes 25 de Marzo de 2025 - Etiquetas: {...}
   - Indica si la tarea esta:
     - Vencida (fecha limite anterior a hoy).
     - En plazo (fecha limite igual o posterior a hoy).
5. Pregunta al usuario una etiqueta (por ejemplo "urgente") y muestra solo las tareas que tengan esa etiqueta (usando la pertenencia a conjuntos).
"""

from datetime import datetime

tareas={}
def comprueba_fecha(fecha):
    try:
        fecha_formateada=datetime.strptime(fecha, "%d/%m/%Y")
        return fecha_formateada
    except ValueError:
        return False

def pide_tareas():

    for i in range(3):
        etiquetas = set()
        tarea=input("Ingresa una tarea")
        fecha=input("Ingresa la fecha de la tarea en formato dd/mm/YYYY: ")
        while not comprueba_fecha(fecha):
            fecha=input("Fecha incorrecta, vuelve a ingresar: ")
        print("Ingresa 3 etiquetas")
        for j in range(3):
            etiqueta=input(f"Ingresa la etiqueta número {j}")
            etiquetas.add(etiqueta)
        tareas[tarea]=comprueba_fecha(fecha), etiquetas

def esta_vencida(fecha):
    if fecha > datetime.today():
        return False
    else:
        return True
def muestra_tareas():
    for tarea in tareas:
        print(f"Tarea: {tarea} - LIMITE {tareas[tarea][0].strftime('%A %d de %B de %Y')} - Etiquetas: {tareas[tarea][1]}")
        if esta_vencida(tareas[tarea][0]):
            print("Vencida")
        else:
            print("En plazo")

def filtra_por_etiqueta(etiqueta):
    for tarea in tareas:
        coincidencia= etiqueta & tareas[tarea][1]
        if coincidencia != "":
            print(f"Tarea: {tarea} - LIMITE {tareas[tarea][0].strftime('%A %d de %B de %Y')} - Etiquetas: {tareas[tarea][1]}")

pide_tareas()
muestra_tareas()
etiqueta=set(input("Ingresa una etiqueta para filtrar tareas"))
filtra_por_etiqueta(etiqueta)