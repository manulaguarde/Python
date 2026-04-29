def login(usuario, pwd):
    usuarios=[]
    contrasenias=[]
    try:
        with open("login.txt") as f:
            contenido=f.read()
            if contenido == "":
                print("Fichero vacío")
            else:
                for line in contenido.splitlines():
                    line=line.strip()
                    line=line.split(":")
                    usuarios.append(line[0])
                    contrasenias.append(line[1])

                if usuario not in usuarios:
                    print("Usuario no existe")

                elif pwd not in contrasenias:
                    print("Password no existe")

                for i in range(len(usuarios)):
                    if usuario == usuarios[i] and pwd == contrasenias[i]:
                        print("Login correcto")

    except FileNotFoundError:
        print("Fichero inexistente o imposible acceder a él")
    except :
        print("Error innesperado")

usuario=input("Usuario: ")
pws=input("Password: ")
login(usuario,pws)