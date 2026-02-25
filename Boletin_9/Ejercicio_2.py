"""Añade una función que sirva para añadir nombres al diccionario. La llamada a la función sería así:
nuevoCliente(clientes, “Felipe”, “Lotas”, 76)
Tu función debería de añadir el nuevo cliente al diccionario con el formato correcto. Si este cliente ya
existe debería de mostrar en consola un mensaje advirtiéndolo y preguntando si se quiere
sobreescribir la edad o no.
"""

clientes = { "Chuletón,José": 35,
             "Tosidad,Rubén": 27,
             "Rupto,Francisco": 44,
             "Cotón,Carmelo": 56 }
def muestraClientes(clientes):
    for item in clientes:
        print(f"{item[0]} {item[1]} ({item[2]})")

def obtener_clientes(clientes):
    clientesLista=[]
    for nombre in clientes:
        nomYAp=nombre.split(",")
        edad=clientes[nombre]
        clientesLista.append([nomYAp[1],nomYAp[0],edad])
    clientesLista.sort()
    muestraClientes(clientesLista)

def nuevo_cliente(clientes, nombre,apellido, edad):
    nomYap=apellido+","+nombre
    clientes[nomYap]=edad
    
nuevo_cliente(clientes,"Felipe","Lotas",76)
obtener_clientes(clientes)