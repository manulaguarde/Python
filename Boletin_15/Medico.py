from Persona import Persona
class Medico(Persona):
    def __init__(self, nombre, apellido,centro,especialidad,num_colegiado):
        super().__init__(nombre, apellido,centro)
        self.__especialidad = especialidad
        if len(num_colegiado) != 6:
            raise ValueError("El numero de colegiado es incorrecto")
        self.__num_colegiado = num_colegiado
        self.__consultas=[]
        self._centro.agregarMedico(self)


    @property
    def centro(self):
        return self._centro

    def cambiarCentro(self,centro):
        self._centro.eliminarMedico(self)
        self._centro = centro
        self._centro.agregarMedico(self)
    def agregarConsulta(self,consulta):
        self.__consultas.append(consulta)

    def __str__(self):
        return (f"Médico {self._apellido}, {self._nombre}"
                f"\nEspecialidad: {self.__especialidad}"
                f"\nNum. Colegiado: {self.__num_colegiado}")

    def listarConsultas(self):
        for consulta in self.__consultas:
            print(consulta)