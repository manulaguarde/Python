articulo=input("Ingrese un artículo: ")
cantidad=input("Ingrese la cantidad: ")
precio=input("Ingrese el precio: ")
total=float(precio)*float(cantidad)
contador=1
contenido=f"{articulo} {cantidad}\n"
agregar=input("Desea agregar otro artículo?")
while agregar.lower()=="si":
    articulo = input("Ingrese un artículo: ")
    cantidad = input("Ingrese la cantidad: ")
    precio = input("Ingrese el precio: ")
    agregar = input("Desea agregar otro artículo?")
    contenido+=f"{articulo} {cantidad}\n"
    total+=float(precio)*float(cantidad)
    contador+=1

fichero="compra.txt"
print(f"Tu lista de compra se encuentra en el fichero '{fichero}'")
try:
    with open( fichero,"at") as f2:
        f2.write(contenido)
        f2.write(f"Total artículos en la lista: {contador}\n")
        f2.write(f"Precio de la compra: {total}")
except:
    print("El fichero no existe")

