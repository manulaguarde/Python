def procesar_fichero(ruta):
    resultados = []
    with open(ruta, 'r') as f:
        for linea in f:
            # 1. Limpiar saltos de línea y separar por el delimitador #
            partes = linea.strip().split('#')

            # 2. Manipulación de cadenas y limpieza individual
            id_user = partes[0].strip()
            nombre = partes[1].strip().capitalize()
            apellido = partes[2].strip().capitalize()
            email = partes[3].strip().lower()

            # 3. Guardar en estructura de datos (Diccionario)
            resultados.append({
                "id": id_user,
                "nombre_completo": f"{nombre} {apellido}",
                "email": email
            })
    return resultados