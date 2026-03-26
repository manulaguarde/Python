class Sms:
    def __init__(self,nombre,telefono,mensaje):
        self._nombre=nombre
        self._telefono=telefono
        self._mensaje=mensaje #f"Hola {self.__nombre} Te llega este aviso por SMS"


class Email:
    def __init__(self, nombre, correo, asunto, mensaje):
        self._nombre = nombre
        self._correo = correo
        self._mensaje = mensaje#f"Hola {self.__nombre} Te llega este aviso por correo"
        self._asunto=asunto#"Aviso"


class NotificacionConjunta(Sms,Email):
    def __init__(self,nombre,telefono,correo,asunto,mensaje):
        super().__init__(nombre,telefono,mensaje)
        Email.__init__(nombre,correo,asunto,mensaje)
        



not1=Sms("Pepe potamo",123456879,"Factura")
not2=Email("Ines","Ines@asdkgjs.com","Factura","Tienes una factura")
not3=NotificacionConjunta("Oscar",456487978,"OscarRugeri@gmail.com","Factura","Tienes una factura")