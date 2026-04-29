from Contacto import Contacto
def procesar_agenda_variable(nombre_fichero):
    lista_contactos = []
    categorias_validas = ["Familia", "Amigo", "Conocido"]

    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            lineas = [l.strip() for l in f if l.strip()]

        i = 0
        while i < len(lineas):
            nombre = lineas[i]
            # La siguiente línea podría ser el Apellido O la Categoría
            siguiente = lineas[i + 1]

            if siguiente in categorias_validas:
                # CASO: Nombre -> Categoría -> Edad (3 líneas)
                categoria = siguiente
                edad = lineas[i + 2]
                nuevo = Contacto(nombre, categoria, edad)
                i += 3
            else:
                # CASO: Nombre -> Apellido -> Categoría -> Edad (4 líneas)
                apellido = siguiente
                categoria = lineas[i + 2]
                edad = lineas[i + 3]

                # Validación extra: si aquí no está la categoría, el formato es erróneo
                if categoria not in categorias_validas:
                    print(f"Error: Se esperaba una categoría válida en la línea {i + 3}")
                    return None

                nuevo = Contacto(nombre, categoria, edad, apellido)
                i += 4

            # Validación final de la edad
            if not edad.isdigit():
                print(f"Error: Edad no válida para {nombre}")
                return None

            lista_contactos.append(nuevo)

        return lista_contactos

    except (FileNotFoundError, IndexError):
        print("Error: El fichero terminó inesperadamente o no existe.")
        return None


# --- PRUEBA ---
agenda = procesar_agenda_variable('C:/ProyectosGit/EjerciciosPython/Boletin_23/agenda_nueva.txt')
if agenda:
    for c in agenda:
        print(c)