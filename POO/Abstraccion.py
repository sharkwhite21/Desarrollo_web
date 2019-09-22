'''Es muy importante empezar desde las cosas mas abstractas
    hasta las cosas mas directas, en la implementacion del codigo
    '''


class FilaBanco():
    usuarios= Hash()

    def siguiente_usuario(self,numero):
        #implementacion
        return self.usuarios.obtener(numero)

    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar(numero,usario)

class Hash():
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self,llave,valor):
        datos[llave]=valor

        
class Queue():
    datos = []

    def obtener(self,llave):
        datos[0]

    def agregar(self,llave,valor):
        datos[len(datos)-1] = valor
