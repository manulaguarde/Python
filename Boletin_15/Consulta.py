from datetime import datetime
class Consulta:
    def __init__(self,paciente,medico,consulta,diagnostico):
        self.__fecha_consulta=datetime.now()
        self.__consultaPaciente=consulta
        self.__respuestaMedico=diagnostico
        self.__paciente=paciente
        self.__medico=medico
        medico.centro.agregarConsulta(self)
        paciente.agregarConsulta(self)
        medico.agregarConsulta(self)

    def __str__(self):
        return (f"Consulta: {self.__consultaPaciente}\n"
                f"Diagnostico: {self.__respuestaMedico}\n")



