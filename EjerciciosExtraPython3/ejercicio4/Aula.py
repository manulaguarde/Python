class Aula:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = []
        self.__profesores={}

    def matricular_estudiante(self,estudiante):
        self.__estudiantes.append(estudiante)

    def asignar_profesor(self,profesor):
        self.__profesores[profesor.especialidad]=profesor

    def generar_acta(self):
        print("Estudiantes")

        for estudiante in self.__estudiantes:
            print(f"DNI: {estudiante.dni}")
            print(f"Nombre: {estudiante.nombre}")

            try:
                lista_notas=list(estudiante.notas.values())
                if len(lista_notas)==0:
                    media=0
                    print(f"Nota media: {media}")
                else:
                    media=sum(lista_notas)/len(lista_notas)
                    print(f"Nota media: {media:.2f}")
            except TypeError:
                print("Error")

        print("Profesores responsables en cada especialidad:")
        for profesor in self.__profesores.values():
            print(f"Nombre: {profesor.nombre}, Especialidad: {profesor.especialidad}")
