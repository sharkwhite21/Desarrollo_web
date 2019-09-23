from abc import ABC,abstractmethod


#Classe asbtracta
class EstructuraAbstracta(ABC):

    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


class Hash():
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self,llave,valor):
        datos[llave]=valor


class Queue(EstructuraAbstracta):
    datos = []

    def obtener(self,llave):
        datos[0]

    def agregar(self,llave,valor):
        datos[len(datos)-1] = valor

class FilaBanco():
    def __init__(self,almacen_usuarios):
        if not isinstance(almacen_usuarios,EstructuraAbstracta):
            raise ValueError('Store is not soported')
        self.usuarios = almacen_usuarios

    def siguiente_usuario(self,numero):
        #implementacion
        return self.usuarios.obtener(numero)

    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar(numero,usario)
FilaBanco(Queue())
