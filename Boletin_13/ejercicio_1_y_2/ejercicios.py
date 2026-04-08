from datetime import datetime,date
from abc import ABCMeta,abstractmethod

class Grupo:
    def __init__(self, nombre, ciclo, curso, tutor):
        self.__nombre=nombre
        self.__ciclo=ciclo
        self.__curso=curso
        self.__tutor=tutor
        self.__matriculados=[]

    @property
    def total_matriculados(self):
        return len(self.__matriculados)

    def agregarAlumno(self,alumno):
        self.__matriculados.append(alumno)

    def eliminarAlumno(self,alumno):
        if alumno not in self.__matriculados:
            raise ValueError("Alumno no existe")
        self.__matriculados.remove(alumno)

    def estadisticasFaltas(self):
        justificadas = 0
        injustificadas = 0

        # recorrer alumnos
        for alumno in self.__matriculados:
            # recorrer faltas de cada alumno
            for falta in alumno.faltas:
                if falta.justificada:
                    justificadas += 1
                else:
                    injustificadas += 1

        total = justificadas + injustificadas

        # porcentajes sobre 1000 horas
        porcentaje_justificadas = (justificadas / 1000) * 100
        porcentaje_injustificadas = (injustificadas / 1000) * 100
        porcentaje_total = (total / 1000) * 100

        print("Faltas justificadas:", justificadas)
        print("Faltas injustificadas:", injustificadas)
        print("Total faltas:", total)
        print(f"% Justificadas: {porcentaje_justificadas:.2f}%")
        print(f"% Injustificadas: {porcentaje_injustificadas:.2f}%")
        print(f"% Total: {porcentaje_total:.2f}%")

    def listarGrupo(self):
        print("Nombre del grupo:",self.__nombre)
        print("Ciclo del grupo:",self.__ciclo.nombre)
        print("Curso:",self.__curso)
        print("Tutor:",self.__tutor.nombre)
        print("Matriculados:")
        for alumno in self.__matriculados:
            print("Nombre completo:",alumno.apellido,alumno.nombre)
        print("Total de alumnos:",self.total_matriculados)
        print("Modulos y profesor que lo imparte: ")
        for modulo in self.__ciclo.modulos:
            print(f"Modulo: {modulo.nombre} - año {modulo.anio} - horas semanales: {modulo.horas_semanales}")
            print("Profesor que lo imparte",modulo.profesor.nombre)




class Persona(metaclass=ABCMeta):
    def __init__(self, nombre, apellido):
        self._nombre=nombre
        self._apellido=apellido

    @abstractmethod
    def nombre(self):
        pass

    @abstractmethod
    def apellido(self):
        pass


class Alumno(Persona):
    def __init__(self, nombre, apellido, edad,ciclo,grupo,repetidor):
        super().__init__(nombre, apellido)
        self.__edad=edad
        self.__ciclo=ciclo
        self.__grupo=grupo
        if self.__edad < 18:
            self.__mayor=False
        else:
            self.__mayor=True
        self.__repetidor=repetidor
        self.__faltas=[]
        self.__grupo.agregarAlumno(self)

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    @property
    def grupo(self):
        return self.__grupo

    @grupo.setter
    def grupo(self,gr):
        self.__grupo=gr

    @property
    def faltas(self):
        return self.__faltas

    def agregarFalta(self,falta):
      self.__faltas.append(falta)

class Profesor(Persona):

    def __init__(self, nombre, apellido, departamento,grupo=None):
        super().__init__(nombre, apellido)
        if departamento not in ["Informática","Empresa","Inglés"]:
            raise ValueError("Departamento incorrecto")
        self.__departamento=departamento
        self.__grupo=grupo

    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

class Modulo:
    def __init__(self, nombre, anio,horas_semanales,optativo,profesor):
        self.__nombre=nombre
        self.__anio=anio
        self.__horas_semanales=horas_semanales
        self.__optativo=optativo
        self.__profesor=profesor

    @property
    def optativo(self):
        return self.__optativo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def anio(self):
        return self.__anio
    @property
    def horas_semanales(self):
        return self.__horas_semanales
    @property
    def profesor(self):
        return self.__profesor

class Ciclo:
    def __init__(self, nombre, grado, *modulo):
        self.__nombre=nombre
        self.__grado=grado
        self.__modulos=modulo

    @property
    def nombre(self):
        return self.__nombre
    @property
    def grado(self):
        return self.__grado
    @property
    def modulos(self):
        return self.__modulos


class FaltasAsistencia:

    def __init__(self, fecha, justificada):
        formato_fecha=datetime.strptime(fecha,"%d/%m/%Y").date()
        self.__fecha=formato_fecha
        self.__justificada=justificada

    @property
    def justificada(self):
        return self.__justificada

    @justificada.setter
    def justificada(self,j):
        hoy = date.today()
        resultado=hoy-self.__fecha
        if resultado.days<= 7:
            self.__justificada=j
        else:
            raise ValueError ("No puede justificarse la falta")


profe1=Profesor("Jose","Morales","Informática")
ingles=Modulo("Inglés","Primero",30,True,profe1)
informatica=Modulo("Informática","Segundo",40,False,profe1)
empresa=Modulo("Empresa","Primero",50,False,profe1)
dam=Ciclo("Desarrollo de aplicaciones multiplataforma","Superior",ingles,informatica)
daw=Ciclo("Desarrollo de aplicaciones web","Superior",ingles,informatica)
estetica=Ciclo("Estetica","Superior",empresa,ingles)
#alu1=Alumno("Manuel","Rey",25,)



