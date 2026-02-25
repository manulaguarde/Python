"""Crear un programa o una función que reciba un diccionario con los datos de los clientes de una tienda
y su edad y los muestre por consola ordenados por nombre de pila. El diccionario, ya creado en el
código de tu programa, tendrá esta forma
clientes = { "Chuletón, José": 35, "Tosidad, Rubén": 27, "Rupto,
Francisco": 44, "Cotón, Carmelo": 56 }
Y la salida por consola así:
Carmelo Cotón (56)
Francisco Rupto (44)
José Chuletón (35)
Rubén Tosidad (27)"""

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

obtener_clientes(clientes)