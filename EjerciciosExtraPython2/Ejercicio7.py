"""1. Crea un diccionario llamado citas donde:
   - La clave sea el DNI del paciente (cadena).
   - El valor sea otro diccionario con:
     - "nombre" (cadena)
     - "fecha" (objeto datetime de la cita)
2. Pide al usuario que introduzca los datos de 3 pacientes:
   - DNI
   - Nombre
   - Fecha de cita en formato "dd/mm/YYYY HH:MM"
3. Convierte la fecha a datetime usando strptime y guarda la informacion en el diccionario.
4. Recorre el diccionario y muestra para cada paciente un mensaje con f-string:
   El paciente NOMBRE con DNI XXX tiene cita el Lunes 25 de Marzo de 2025 a las 10:30
   (formatea la fecha con strftime usando dia y mes en letra).
5. Compara cada fecha de cita con la fecha y hora actuales:
   - Si la cita ya ha pasado, indica: La cita de NOMBRE ya ha pasado hace X dias
   - Si la cita aun no ha pasado, indica: Faltan X dias para la cita de NOMBRE
"""

from datetime import datetime

clientes={}

for i in range (3):
    dni=input("ingrese DNI: ")
    nombre=input("ingrese nombre: ")
    fecha=input("ingrese fecha y hora de la cita en formato dd/mm/yyyy HH:MM: ")
    fechaCorrecta=False

    while not fechaCorrecta:
        try:
            fecha_formateada=datetime.strptime(fecha, "%d/%m/%Y %H:%M")
            fechaCorrecta=True
            clientes[dni] = (nombre,fecha_formateada )
        except ValueError:
            fecha=input("fecha no válida vuelve a ingresar: ")

for dni, cita in clientes.items():
    print(f"El paciente {cita[0]} con DNI {dni} tiene cita el {cita[1].strftime("%A %d de %B de %Y a las %H:%M")}")

hoy=datetime.today()
for dni in clientes:
    diferencia=clientes[dni][1] - hoy
    dias=diferencia.days
    if dias>0:
        print(f"Faltan {dias} dias para la cita de {clientes[dni][0]}")
    elif dias<0:
        print(f"La cita de {clientes[dni][0]} ya ha pasado hace {abs(dias)} dias")
    else:
        print(f"La cita de {clientes[dni][0]} es hoy")


