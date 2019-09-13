'''class Curso(object):
    nombre= "Marlon"
    def Saludar(self,saludo):
        print( saludo +  self.nombre)

Marlon = Curso()

Marlon.Saludar("Hola mi nombre es ")
'''
class Usuario(object):
    """docstring for Curso."""

    def __init__(self, nombre):
        #Metodo constructor
        self.nombre = nombre

    def Saludar(self,saludo):
        print( saludo +  self.nombre)

Marlon = Usario("Marlon")

Marlon.Saludar("Hola mi nombre es ")
