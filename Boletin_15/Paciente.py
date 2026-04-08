from Persona import Persona
class Paciente(Persona):
    def __init__(self, nombre, apellido,centro,dni,telefono):
        super().__init__(nombre, apellido,centro)
        self.__dni = dni
        self.__telefono = telefono
        self.__consultas=[]
        self._centro.agregarPaciente(self)


    @property
    def centro(self):
        return self._centro

    def cambiarCentro(self,centro):
        self._centro.eliminarPaciente(self)
        self._centro = centro
        self._centro.agregarPaciente(self)

    def agregarConsulta(self,consulta):
        self.__consultas.append(consulta)

    def __str__(self):
        return (f" Paciente: {self._apellido},{self._nombre}"
                f"\nDNI: {self.__dni}"
                f"\nTelefono: {self.__telefono}")

    def listarConsultas(self):
        for consulta in self.__consultas:
            print(consulta)
