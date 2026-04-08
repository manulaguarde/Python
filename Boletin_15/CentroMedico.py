
class CentroMedico:
    def __init__(self, nombre,codigo):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__pacientes=[]
        self.__medicos=[]
        self.__consultas=[]

    def agregarPaciente(self,p):
        self.__pacientes.append(p)

    def agregarMedico(self,m):
        self.__medicos.append(m)

    def eliminarPaciente(self,p):
        self.__pacientes.remove(p)

    def eliminarMedico(self,m):
        self.__medicos.remove(m)

    def agregarConsulta(self,c):
        self.__consultas.append(c)

    def listarPacientes(self):
        for p in self.__pacientes:
            print(p)

    def listarMedicos(self):
        for m in self.__medicos:
            print(m)


