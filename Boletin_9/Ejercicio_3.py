"""Por último, crea ahora una función que sume un año a la edad de un cliente. La llamada sería así:
cumpleCliente(clientes, “José”, “Chuletón”)
Si el cliente existe debería de sumar un año a su edad. Si no existe debería de informar de ello por
consola y no hacer nada"""

clientes = {"Chuletón,José": 35,
            "Tosidad,Rubén": 27,
            "Rupto,Francisco": 44,
            "Cotón,Carmelo": 56}


def muestraClientes(clientes):
    for item in clientes:
        print(f"{item[0]} {item[1]} ({item[2]})")


def obtener_clientes(clientes):
    clientesLista = []
    for nombre in clientes:
        nomYAp = nombre.split(",")
        edad = clientes[nombre]
        clientesLista.append([nomYAp[1], nomYAp[0], edad])
    clientesLista.sort()
    muestraClientes(clientesLista)


def nuevo_cliente(clientes, nombre, apellido, edad):
    nomYap = apellido + "," + nombre
    clientes[nomYap] = edad

def cumple_cliente(clientes, nombre, apellido):
    nomYap = apellido + "," + nombre
    if nomYap in clientes:
        clientes[nomYap]+=1
    else:
        print("Cliente no encontrado")

nuevo_cliente(clientes, "Felipe", "Lotas", 76)
cumple_cliente(clientes,"José","Chuletón")
cumple_cliente(clientes,"Manuel","Rey")
obtener_clientes(clientes)